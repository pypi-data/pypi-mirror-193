from .._content_data_provider import ContentDataProvider
from .._error_parser import ErrorParser
from .._universe_content_validator import UniverseContentValidator
from ..._tools import universe_arg_parser
from ...delivery._data._data_provider import (
    RequestFactory,
    ValidatorContainer,
)


# ---------------------------------------------------------------------------
#   Request
# ---------------------------------------------------------------------------


class ESGRequestFactory(RequestFactory):
    def get_query_parameters(self, *args, **kwargs):
        query_parameters = []

        #
        # universe
        #
        universe = kwargs.get("universe")
        if universe:
            universe = universe_arg_parser.get_str(universe, delim=",")
            query_parameters.append(("universe", universe))

        #
        # start
        #
        start = kwargs.get("start")
        if start is not None:
            query_parameters.append(("start", start))

        #
        # end
        #
        end = kwargs.get("end")
        if end is not None:
            query_parameters.append(("end", end))

        return query_parameters


# ---------------------------------------------------------------------------
#   Provider
# ---------------------------------------------------------------------------

esg_data_provider = ContentDataProvider(
    request=ESGRequestFactory(),
    validator=ValidatorContainer(content_validator=UniverseContentValidator()),
    parser=ErrorParser(),
)
