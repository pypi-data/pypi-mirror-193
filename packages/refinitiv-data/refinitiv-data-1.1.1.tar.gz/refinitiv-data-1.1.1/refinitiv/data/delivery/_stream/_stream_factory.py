import itertools
from dataclasses import dataclass
from typing import Dict, Type, Optional, TYPE_CHECKING, Union

from ._omm_stream import _OMMStream
from ._protocol_type import ProtocolType
from ._rdp_stream import _RDPStream
from ._stream_cxn_config_provider import get_cxn_config, release_cxn_cfg_provider
from .contrib._stream_connection import OffStreamContribConnection
from .omm_stream_connection import OMMStreamConnection
from .rdp_stream_connection import RDPStreamConnection
from .._data._api_type import APIType
from ... import _log as log, get_config
from ..._content_type import ContentType
from ..._types import OptDict, OptStr, Strings, ExtendedParams, OptCall

if TYPE_CHECKING:
    from ._stream_cxn_config_data import StreamCxnConfig
    from . import StreamConnection
    from ..._core.session import Session
    from .contrib._offstream import _OffStreamContrib


def logger():
    return log.root_logger().getChild("stream-factory")


protocol_type_by_name: Dict[str, ProtocolType] = {
    "OMM": ProtocolType.OMM,
    "RDP": ProtocolType.RDP,
}

api_config_key_by_api_type: Dict[APIType, str] = {
    APIType.STREAMING_FINANCIAL_CONTRACTS: "apis.streaming.quantitative-analytics.endpoints.financial-contracts",
    APIType.STREAMING_PRICING: "apis.streaming.pricing.endpoints.main",
    APIType.STREAMING_TRADING: "apis.streaming.trading-analytics.endpoints.redi",
    APIType.STREAMING_BENCHMARK: "apis.streaming.benchmark.endpoints.resource",
    APIType.STREAMING_CUSTOM_INSTRUMENTS: "apis.streaming.custom-instruments.endpoints.resource",
    APIType.STREAMING_CONTRIB: "apis.streaming.contrib.endpoints.main",
}
service_config_key_by_api_type = {
    APIType.STREAMING_FINANCIAL_CONTRACTS: "apis.streaming.quantitative-analytics.service",
    APIType.STREAMING_PRICING: "apis.streaming.pricing.service",
    APIType.STREAMING_TRADING: "apis.streaming.trading-analytics.service",
    APIType.STREAMING_BENCHMARK: "apis.streaming.benchmark.service",
    APIType.STREAMING_CUSTOM_INSTRUMENTS: "apis.streaming.custom-instruments.service",
    APIType.STREAMING_CONTRIB: "apis.streaming.contrib.service",
}

api_type_by_content_type: Dict[ContentType, APIType] = {
    ContentType.STREAMING_CHAINS: APIType.STREAMING_PRICING,
    ContentType.STREAMING_PRICING: APIType.STREAMING_PRICING,
    ContentType.STREAMING_TRADING: APIType.STREAMING_TRADING,
    ContentType.STREAMING_CONTRACTS: APIType.STREAMING_FINANCIAL_CONTRACTS,
    ContentType.STREAMING_CUSTOM_INSTRUMENTS: APIType.STREAMING_CUSTOM_INSTRUMENTS,
    ContentType.STREAMING_CONTRIB: APIType.STREAMING_CONTRIB,
    ContentType.STREAMING_OFF_CONTRIB: APIType.STREAMING_CONTRIB,
}

connection_id_iterator = itertools.count(0)

stream_class_by_protocol_type: Dict[
    ProtocolType, Type[Union[_OMMStream, _RDPStream]]
] = {
    ProtocolType.OMM: _OMMStream,
    ProtocolType.RDP: _RDPStream,
}


@dataclass
class StreamDetails:
    content_type: ContentType
    protocol_type: ProtocolType
    api_type: APIType
    api_config_key: str = ""

    @property
    def api_type_as_str(self):
        if self.api_type is ContentType.STREAMING_CUSTOM:
            return f"{self.api_type}.{self.api_config_key}"
        else:
            return str(self.api_type)


def content_type_to_details(content_type: ContentType) -> StreamDetails:
    api_type = api_type_by_content_type.get(content_type, APIType.STREAMING_CUSTOM)

    if content_type is ContentType.STREAMING_CUSTOM:
        raise ValueError("Cannot create StreamDetails, without api.")

    return StreamDetails(content_type, ProtocolType.NONE, api_type)


def convert_api_config_key_to_content_type(api_config_key: str) -> ContentType:
    """
    >>> api_type_by_api_config_key
    {
        'streaming/quantitative-analytics/financial-contracts': <APIType.STREAMING_FINANCIAL_CONTRACTS: 3>,
        'streaming/pricing/main': <APIType.STREAMING_PRICING: 8>,
        'streaming/trading-analytics/redi': <APIType.STREAMING_TRADING: 11>
    }
    >>> content_type_by_api_type
    {
        <APIType.STREAMING_PRICING: 8>: <ContentType.STREAMING_PRICING: 17>,
        <APIType.STREAMING_TRADING: 11>: <ContentType.STREAMING_TRADING: 39>,
        <APIType.STREAMING_FINANCIAL_CONTRACTS: 3>: <ContentType.STREAMING_CONTRACTS: 6>
    }
    """
    api_type_by_api_config_key = {v: k for k, v in api_config_key_by_api_type.items()}
    api_type = api_type_by_api_config_key.get(api_config_key)
    content_type_by_api_type = {v: k for k, v in api_type_by_content_type.items()}
    content_type = content_type_by_api_type.get(api_type)

    if not content_type:
        content_type = ContentType.STREAMING_CUSTOM

    return content_type


def get_valid_content_type(content_type: ContentType, api: str = "") -> ContentType:
    if content_type in {ContentType.STREAMING_CUSTOM, ContentType.NONE}:
        if not api:
            raise ValueError("api cannot be None")

        content_type = convert_api_config_key_to_content_type(api)

    return content_type


def create_omm_stream(
    content_type: ContentType,
    session: "Session",
    name: str,
    api: OptStr = None,
    domain: OptStr = None,
    service: OptStr = None,
    fields: Optional[Strings] = None,
    key: OptDict = None,
    extended_params: "ExtendedParams" = None,
    on_refresh: OptCall = None,
    on_status: OptCall = None,
    on_update: OptCall = None,
    on_complete: OptCall = None,
    on_error: OptCall = None,
    on_ack: OptCall = None,
) -> _OMMStream:
    if content_type is ContentType.NONE and not api:
        content_type = ContentType.STREAMING_PRICING

    else:
        content_type = get_valid_content_type(content_type, api)

    api_type = api_type_by_content_type.get(content_type, APIType.STREAMING_CUSTOM)
    details = StreamDetails(content_type, ProtocolType.OMM, api_type, api)
    if not service:
        service = session.config.get(service_config_key_by_api_type.get(api_type))

    stream_id = next(session._omm_stream_counter)
    stream = _OMMStream(
        stream_id=stream_id,
        session=session,
        name=name,
        domain=domain,
        service=service,
        fields=fields,
        key=key,
        extended_params=extended_params,
        on_refresh=on_refresh,
        on_status=on_status,
        on_update=on_update,
        on_complete=on_complete,
        on_error=on_error,
        on_ack=on_ack,
        details=details,
    )
    logger().debug(f" + Created stream: {stream.classname}")
    return stream


def create_rdp_stream(
    content_type: ContentType,
    session: "Session",
    universe: Union[list, dict],
    view: list,
    extended_params: "ExtendedParams",
    parameters: OptDict = None,
    service: OptStr = None,
    api: str = "",
    on_ack: OptCall = None,
    on_response: OptCall = None,
    on_update: OptCall = None,
    on_alarm: OptCall = None,
) -> _RDPStream:
    content_type = get_valid_content_type(content_type, api)
    api_type = api_type_by_content_type.get(content_type, APIType.STREAMING_CUSTOM)
    if not service:
        service = session.config.get(service_config_key_by_api_type.get(api_type))

    details = StreamDetails(content_type, ProtocolType.RDP, api_type, api)
    stream_id = next(session._rdp_stream_counter)
    stream = _RDPStream(
        stream_id=stream_id,
        session=session,
        service=service,
        universe=universe,
        view=view,
        parameters=parameters,
        extended_params=extended_params,
        on_ack=on_ack,
        on_response=on_response,
        on_update=on_update,
        on_alarm=on_alarm,
        details=details,
    )
    logger().debug(f" + Created stream: {stream.classname}")
    return stream


def get_protocol_type_by_name(protocol_name: str) -> ProtocolType:
    protocol_type = protocol_type_by_name.get(protocol_name)

    if not protocol_type:
        raise ValueError(f"Can't find protocol type by name: {protocol_name}")

    return protocol_type


cxn_class_by_protocol_type: Dict[
    ProtocolType,
    Type[Union[OMMStreamConnection, RDPStreamConnection]],
] = {
    ProtocolType.OMM: OMMStreamConnection,
    ProtocolType.OMM_OFF_CONTRIB: OffStreamContribConnection,
    ProtocolType.RDP: RDPStreamConnection,
}


def load_config(details: StreamDetails, session: "Session") -> "StreamCxnConfig":
    content_type = details.content_type

    if content_type is ContentType.STREAMING_CUSTOM:
        api_config_key = details.api_config_key

        if not api_config_key:
            raise ValueError(
                "For ContentType.STREAMING_CUSTOM, api_config_key cannot be None"
            )

        file_config = get_config()
        if not api_config_key.startswith("apis."):
            api_config_key = f"apis.{api_config_key}"
        if api_config_key.endswith(".path"):
            api_config_key = api_config_key[:-5]

        if not file_config.get(api_config_key):
            raise ValueError(
                f"Not an existing path {api_config_key} to url into config file"
            )
        end_word = api_config_key.rsplit(".", 1)[-1]
        if not end_word or end_word == "endpoints":
            raise ValueError(
                f"Not a valid format, use `apis.streaming.xxx.endpoints.xxx"
            )
        api_type = api_config_key

    else:
        api_type = api_type_by_content_type.get(content_type)
        api_config_key = api_config_key_by_api_type.get(api_type)

    config: "StreamCxnConfig" = get_cxn_config(api_config_key, session)
    logger().debug(f"Loaded config for {api_type}, {config}")
    release_cxn_cfg_provider(session)
    return config


def create_stream_cxn(details: StreamDetails, session: "Session") -> "StreamConnection":
    content_type = details.content_type
    protocol_type = details.protocol_type
    config = load_config(details, session)
    session_id = session.session_id
    connection_id = next(connection_id_iterator)
    name = f"{protocol_type.name}{content_type.name}_{session_id}.{connection_id}"
    cxn_class = cxn_class_by_protocol_type.get(protocol_type)
    cxn = cxn_class(
        connection_id=connection_id,
        name=name,
        session=session,
        config=config,
    )
    logger().debug(f" + Created: \n\tcxn    : {cxn}\n\tconfig : {config}")
    return cxn


def create_offstream_contrib(
    session: "Session",
    name: str,
    api: OptStr = None,
    domain: OptStr = None,
    service: OptStr = None,
) -> "_OffStreamContrib":
    from .contrib._offstream import _OffStreamContrib

    content_type = ContentType.STREAMING_OFF_CONTRIB
    stream = _OffStreamContrib(
        post_id=next(session._contrib_post_id_counter),
        session=session,
        name=name,
        details=StreamDetails(
            content_type,
            ProtocolType.OMM_OFF_CONTRIB,
            api_type_by_content_type[content_type],
            api,
        ),
        service=service,
        domain=domain,
    )
    logger().debug(f" + Created offstream contrib={stream.classname}")
    return stream
