# coding: utf8

import asyncio
import time
from enum import Enum, unique
from typing import Callable, List, Union, TYPE_CHECKING, Optional

from ._data_grid_type import (
    DataGridType,
    determine_content_type_and_flag,
)
from .._content_data import Data
from .._content_provider_layer import ContentUsageLoggerMixin
from ..._content_type import ContentType
from .._df_build_type import DFBuildType
from ..._core.session import get_valid_session
from ..._tools import ArgsParser, make_convert_to_enum_arg_parser, try_copy_to_list
from ..._tools import create_repr
from ...delivery._data._data_provider import DataProviderLayer, BaseResponse
from ...errors import RDError

if TYPE_CHECKING:
    from ..._types import ExtendedParams, OptDict, StrStrings
    from ..._core.session import Session


@unique
class RowHeaders(Enum):
    DATE = "date"


OptRowHeaders = Optional[Union[str, List[str], RowHeaders, List[RowHeaders]]]

row_headers_enum_arg_parser = make_convert_to_enum_arg_parser(RowHeaders)


def parse_row_headers(value) -> Union[RowHeaders, List[RowHeaders]]:
    if value is None:
        return []

    value = row_headers_enum_arg_parser.parse(value)

    return value


row_headers_arg_parser = ArgsParser(parse_row_headers)


def get_layout(row_headers: List[RowHeaders], content_type: ContentType) -> dict:
    layout = None

    is_rdp = content_type is ContentType.DATA_GRID_RDP
    is_udf = content_type is ContentType.DATA_GRID_UDF

    if is_udf:
        layout = {
            "layout": {
                "columns": [{"item": "dataitem"}],
                "rows": [{"item": "instrument"}],
            }
        }
    elif is_rdp:
        layout = {"output": "Col,T|Va,Row,In|"}

    if RowHeaders.DATE in row_headers:
        if is_udf:
            layout["layout"]["rows"].append({"item": "date"})

        elif is_rdp:
            output = layout["output"]
            output = output[:-1]  # delete forward slash "|"
            output = f"{output},date|"
            layout["output"] = output

    else:
        layout = ""

    if layout is None:
        raise ValueError(
            f"Layout is None, row_headers={row_headers}, content_type={content_type}"
        )

    return layout


def get_dfbuild_type(row_headers: List[RowHeaders]) -> DFBuildType:
    dfbuild_type = DFBuildType.INDEX

    if RowHeaders.DATE in row_headers:
        dfbuild_type = DFBuildType.DATE_AS_INDEX

    return dfbuild_type


class Definition(
    ContentUsageLoggerMixin[BaseResponse[Data]], DataProviderLayer[BaseResponse[Data]]
):
    """
    This class describe the universe (list of instruments), the fields
    (a.k.a. data items) and parameters that will be requested to the data platform

    Parameters:
    ----------
    universe : str or list of str
        The list of RICs
    fields : str or list of str
        List of fundamental field names
    parameters : dict, optional
        Global parameters for fields
    row_headers : str, list of str, list of RowHeaders enum
        When this parameter is used, the output/layout parameter will be added
        to the underlying request to DataGrid RDP or UDF
    use_field_names_in_headers : bool, optional
        If value is True we add field names in headers.
    extended_params : dict, optional
        Other parameters can be provided if necessary

    Examples
    --------
     >>> from refinitiv.data.content import fundamental_and_reference
     >>> definition = fundamental_and_reference.Definition(["IBM"], ["TR.Volume"])
     >>> definition.get_data()

     Using get_data_async
     >>> import asyncio
     >>> task = definition.get_data_async()
     >>> response = asyncio.run(task)
    """

    _USAGE_CLS_NAME = "FundamentalAndReference.Definition"

    def __init__(
        self,
        universe: "StrStrings",
        fields: "StrStrings",
        parameters: "OptDict" = None,
        row_headers: OptRowHeaders = None,
        use_field_names_in_headers: bool = False,
        extended_params: "ExtendedParams" = None,
    ):
        self.universe = try_copy_to_list(universe)
        self.fields = try_copy_to_list(fields)
        self.parameters = parameters
        self.use_field_names_in_headers = use_field_names_in_headers
        self.extended_params = extended_params
        self.row_headers = try_copy_to_list(row_headers)
        super().__init__(
            data_type=ContentType.DEFAULT,
            universe=self.universe,
            fields=self.fields,
            parameters=self.parameters,
            row_headers=self.row_headers,
            use_field_names_in_headers=self.use_field_names_in_headers,
            extended_params=self.extended_params,
        )

    def _update_content_type(self, session: "Session"):
        content_type, changed = determine_content_type_and_flag(session)
        changed and session.debug(
            f"UDF DataGrid service cannot be used with platform sessions, RDP DataGrid will be used instead. "
            f"The \"/apis/data/datagrid/underlying-platform = '{DataGridType.UDF.value}'\" "
            f"parameter will be discarded, meaning that the regular RDP DataGrid "
            f"service will be used for Fundamental and Reference data requests."
        )
        self._initialize(content_type, **self._kwargs)
        row_headers = self._kwargs.get("row_headers")
        row_headers = row_headers_arg_parser.get_list(row_headers)
        layout = get_layout(row_headers, content_type)
        dfbuild_type = get_dfbuild_type(row_headers)
        self._kwargs["layout"] = layout
        self._kwargs["__dfbuild_type__"] = dfbuild_type

    @staticmethod
    def make_on_response(callback: Callable) -> Callable:
        def on_response(response, data_provider, session):
            if response and response.data and response.data.raw.get("ticket"):
                return
            callback(response, data_provider, session)

        return on_response

    @staticmethod
    def _get_duration(raw_response: dict) -> Union[int, None]:
        """
        Compute the duration to sleep before next retry to request ticket status

        :param raw_response: request's response
        :type raw_response: dict
        :return: duration if response contains "estimatedDuration", None otherwise
        """
        ticket_duration = raw_response.get("estimatedDuration")
        if ticket_duration:
            ticket_duration = int(min(ticket_duration, 15000) / 1000)
            return ticket_duration
        return None

    def get_data(
        self,
        session: Optional["Session"] = None,
        on_response: Optional[Callable] = None,
    ):
        """
        Returns a response to the data platform

        Parameters
        ----------
        session : Session, optional
            Means default session would be used
        on_response : Callable, optional
            Callable object to process retrieved data

        Returns
        -------
        Response

        Raises
        ------
        AttributeError
            If user didn't set default session.
        """
        session = get_valid_session(session)
        self._update_content_type(session)
        if self._content_type == ContentType.DATA_GRID_UDF:
            on_response_filter = on_response and self.make_on_response(on_response)
            response = super().get_data(session, on_response_filter)

            while response.data:
                ticket = response.data.raw.get("ticket")
                if ticket:
                    sleep_duration = self._get_duration(response.data.raw)
                    if sleep_duration:
                        time.sleep(sleep_duration)
                    else:
                        raise RDError(
                            -1,
                            "Receive ticket response from DataGrid without estimatedDuration",
                        )
                    self._kwargs["ticket"] = ticket
                    response = super().get_data(session, on_response_filter)
                else:
                    break
        else:
            response = super().get_data(session, on_response)
        return response

    async def get_data_async(
        self,
        session: Optional["Session"] = None,
        on_response: Optional[Callable] = None,
    ):
        """
        Returns a response asynchronously to the data platform

        Parameters
        ----------
        session : Session, optional
            Means default session would be used
        on_response : Callable, optional
            Callable object to process retrieved data

        Returns
        -------
        Response

        Raises
        ------
        AttributeError
            If user didn't set default session.

        """
        session = get_valid_session(session)
        self._update_content_type(session)

        if self._content_type == ContentType.DATA_GRID_UDF:
            on_response_filter = on_response and self.make_on_response(on_response)
            response = await super().get_data_async(session, on_response_filter)

            while response.data:
                ticket = response.data.raw.get("ticket")
                if ticket:
                    sleep_duration = self._get_duration(response.data.raw)
                    if sleep_duration:
                        await asyncio.sleep(sleep_duration)
                    else:
                        raise RDError(
                            -1,
                            "Receive ticket response from DataGrid without estimatedDuration",
                        )
                    self._kwargs["ticket"] = ticket
                    response = await super().get_data_async(session, on_response_filter)
                else:
                    break

        else:
            response = await super().get_data_async(session, on_response)
        return response

    def __repr__(self):
        return create_repr(
            self,
            content=f"{{"
            f"universe='{self.universe}', "
            f"fields='{self.fields}', "
            f"parameters='{self.parameters}', "
            f"row_headers='{self.row_headers}'"
            f"}}",
        )
