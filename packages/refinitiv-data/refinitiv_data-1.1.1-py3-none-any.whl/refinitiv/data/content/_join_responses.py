__all__ = "ContentUsageLoggerMixin"

from types import SimpleNamespace
from typing import List, Callable

import pandas as pd

from ._content_data import Data
from ..delivery._data._parsed_data import ParsedData
from ..delivery._data._response import Response


def join_responses(
    responses: List[Response],
    join_dataframes: Callable = pd.concat,
    response_class=Response,
    data_class=Data,
    reset_index=False,
    limit: int = None,
) -> Response:
    def build_df(*args, **kwargs):
        dfs = []
        df = None

        for response in responses:
            dfs.append(response.data.df)

        all_dfs_is_none = all(a is None for a in dfs)
        if not all_dfs_is_none:
            df = join_dataframes(dfs)

        if reset_index and df is not None:
            df = df.reset_index(drop=True)
        if limit:
            df = df[:limit]
        return df

    if len(responses) == 1:
        return responses[0]

    raws = []
    http_statuses = []
    http_headers = []
    request_messages = []
    http_responses = []
    errors = []
    is_successes = []

    for response in responses:
        raws.append(response.data.raw)
        http_statuses.append(response.http_status)
        http_headers.append(response.http_headers)
        request_messages.append(response.request_message)
        http_responses.append(response.http_response)
        is_successes.append(response.is_success)

        if response.errors:
            errors += response.errors

    raw_response = SimpleNamespace()
    raw_response.headers = http_headers
    raw_response.request = request_messages
    is_success = any(is_successes)
    data_factory = SimpleNamespace()
    response = response_class(
        is_success, ParsedData(http_statuses, raw_response), data_factory
    )
    data_factory.create_data = lambda *args, **kwargs: data_class(
        raws, build_df, owner_=response
    )
    response.errors += errors
    response.http_response = http_responses

    return response
