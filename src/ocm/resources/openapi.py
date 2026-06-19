# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["OpenAPIResource", "AsyncOpenAPIResource"]


class OpenAPIResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpenAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/ocm-python#accessing-raw-response-data-eg-headers
        """
        return OpenAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/ocm-python#with_streaming_response
        """
        return OpenAPIResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Retrieve the current OpenAPI format (YAML) definition for this API.

        This is
        useful for documentation tools, mocking, testing and client generation.
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/openapi",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOpenAPIResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpenAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/ocm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpenAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/ocm-python#with_streaming_response
        """
        return AsyncOpenAPIResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Retrieve the current OpenAPI format (YAML) definition for this API.

        This is
        useful for documentation tools, mocking, testing and client generation.
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/openapi",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OpenAPIResourceWithRawResponse:
    def __init__(self, openapi: OpenAPIResource) -> None:
        self._openapi = openapi

        self.retrieve = to_raw_response_wrapper(
            openapi.retrieve,
        )


class AsyncOpenAPIResourceWithRawResponse:
    def __init__(self, openapi: AsyncOpenAPIResource) -> None:
        self._openapi = openapi

        self.retrieve = async_to_raw_response_wrapper(
            openapi.retrieve,
        )


class OpenAPIResourceWithStreamingResponse:
    def __init__(self, openapi: OpenAPIResource) -> None:
        self._openapi = openapi

        self.retrieve = to_streamed_response_wrapper(
            openapi.retrieve,
        )


class AsyncOpenAPIResourceWithStreamingResponse:
    def __init__(self, openapi: AsyncOpenAPIResource) -> None:
        self._openapi = openapi

        self.retrieve = async_to_streamed_response_wrapper(
            openapi.retrieve,
        )
