# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import referencedata_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.referencedata_retrieve_response import ReferencedataRetrieveResponse

__all__ = ["ReferencedataResource", "AsyncReferencedataResource"]


class ReferencedataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferencedataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#accessing-raw-response-data-eg-headers
        """
        return ReferencedataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferencedataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#with_streaming_response
        """
        return ReferencedataResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        countryid: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferencedataRetrieveResponse:
        """
        Returns the core reference data used for looking up IDs such as Connection
        Types, Operators, Countries etc.

        This information is useful for UIs such as editing systems or for fetching
        results in the lighter non-verbose mode, then hydrating POI results back into
        complex objects.

        Args:
          countryid: Optional filter on countryid, exact match on a given numeric country id (comma
              separated list)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/referencedata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"countryid": countryid}, referencedata_retrieve_params.ReferencedataRetrieveParams
                ),
            ),
            cast_to=ReferencedataRetrieveResponse,
        )


class AsyncReferencedataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferencedataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReferencedataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferencedataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#with_streaming_response
        """
        return AsyncReferencedataResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        countryid: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferencedataRetrieveResponse:
        """
        Returns the core reference data used for looking up IDs such as Connection
        Types, Operators, Countries etc.

        This information is useful for UIs such as editing systems or for fetching
        results in the lighter non-verbose mode, then hydrating POI results back into
        complex objects.

        Args:
          countryid: Optional filter on countryid, exact match on a given numeric country id (comma
              separated list)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/referencedata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"countryid": countryid}, referencedata_retrieve_params.ReferencedataRetrieveParams
                ),
            ),
            cast_to=ReferencedataRetrieveResponse,
        )


class ReferencedataResourceWithRawResponse:
    def __init__(self, referencedata: ReferencedataResource) -> None:
        self._referencedata = referencedata

        self.retrieve = to_raw_response_wrapper(
            referencedata.retrieve,
        )


class AsyncReferencedataResourceWithRawResponse:
    def __init__(self, referencedata: AsyncReferencedataResource) -> None:
        self._referencedata = referencedata

        self.retrieve = async_to_raw_response_wrapper(
            referencedata.retrieve,
        )


class ReferencedataResourceWithStreamingResponse:
    def __init__(self, referencedata: ReferencedataResource) -> None:
        self._referencedata = referencedata

        self.retrieve = to_streamed_response_wrapper(
            referencedata.retrieve,
        )


class AsyncReferencedataResourceWithStreamingResponse:
    def __init__(self, referencedata: AsyncReferencedataResource) -> None:
        self._referencedata = referencedata

        self.retrieve = async_to_streamed_response_wrapper(
            referencedata.retrieve,
        )
