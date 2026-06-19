# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import mediaitem_create_params
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
from ..types.mediaitem_create_response import MediaitemCreateResponse

__all__ = ["MediaitemResource", "AsyncMediaitemResource"]


class MediaitemResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediaitemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/ocm-python#accessing-raw-response-data-eg-headers
        """
        return MediaitemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaitemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/ocm-python#with_streaming_response
        """
        return MediaitemResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        charge_point_id: int,
        image_data_base64: str,
        comment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaitemCreateResponse:
        """
        Submit a photo for a specific charging location

        Args:
          charge_point_id: ID value for the OCM site (POI) this image relates to.

          image_data_base64: BASE64 encoded data

          comment: Optional description of image or context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mediaitem",
            body=maybe_transform(
                {
                    "charge_point_id": charge_point_id,
                    "image_data_base64": image_data_base64,
                    "comment": comment,
                },
                mediaitem_create_params.MediaitemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaitemCreateResponse,
        )


class AsyncMediaitemResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediaitemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/ocm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaitemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaitemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/ocm-python#with_streaming_response
        """
        return AsyncMediaitemResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        charge_point_id: int,
        image_data_base64: str,
        comment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaitemCreateResponse:
        """
        Submit a photo for a specific charging location

        Args:
          charge_point_id: ID value for the OCM site (POI) this image relates to.

          image_data_base64: BASE64 encoded data

          comment: Optional description of image or context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mediaitem",
            body=await async_maybe_transform(
                {
                    "charge_point_id": charge_point_id,
                    "image_data_base64": image_data_base64,
                    "comment": comment,
                },
                mediaitem_create_params.MediaitemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaitemCreateResponse,
        )


class MediaitemResourceWithRawResponse:
    def __init__(self, mediaitem: MediaitemResource) -> None:
        self._mediaitem = mediaitem

        self.create = to_raw_response_wrapper(
            mediaitem.create,
        )


class AsyncMediaitemResourceWithRawResponse:
    def __init__(self, mediaitem: AsyncMediaitemResource) -> None:
        self._mediaitem = mediaitem

        self.create = async_to_raw_response_wrapper(
            mediaitem.create,
        )


class MediaitemResourceWithStreamingResponse:
    def __init__(self, mediaitem: MediaitemResource) -> None:
        self._mediaitem = mediaitem

        self.create = to_streamed_response_wrapper(
            mediaitem.create,
        )


class AsyncMediaitemResourceWithStreamingResponse:
    def __init__(self, mediaitem: AsyncMediaitemResource) -> None:
        self._mediaitem = mediaitem

        self.create = async_to_streamed_response_wrapper(
            mediaitem.create,
        )
