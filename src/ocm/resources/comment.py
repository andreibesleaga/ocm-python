# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import comment_submit_params
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
from ..types.comment_submit_response import CommentSubmitResponse

__all__ = ["CommentResource", "AsyncCommentResource"]


class CommentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#accessing-raw-response-data-eg-headers
        """
        return CommentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#with_streaming_response
        """
        return CommentResourceWithStreamingResponse(self)

    def submit(
        self,
        *,
        charge_point_id: int,
        checkin_status_type_id: int | Omit = omit,
        comment: str | Omit = omit,
        comment_type_id: int | Omit = omit,
        rating: int | Omit = omit,
        related_url: str | Omit = omit,
        user_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentSubmitResponse:
        """
        Submit a user comment or checkin for a specific charging location

        Args:
          charge_point_id: This must be a valid POI ID

          checkin_status_type_id: Optional valid CheckStatusTypeID to indicate overall catgeory and
              success/failure to use equipment e.g. 10 = Charged Successfully.

          comment: This is an optional comment to describe the charging experience, may include
              guidance for future users.

          comment_type_id: This must be a valid Comment Type ID as per UserCommentTypes found in Core
              Reference Data. If left as null then General Comment will be used.

          rating: Optional integer rating between 1 = Worst, 5 = Best.

          related_url: Optional website URL for related information

          user_name: This is an optional name to associate with the submission, for authenticated
              users their profile username is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/comment",
            body=maybe_transform(
                {
                    "charge_point_id": charge_point_id,
                    "checkin_status_type_id": checkin_status_type_id,
                    "comment": comment,
                    "comment_type_id": comment_type_id,
                    "rating": rating,
                    "related_url": related_url,
                    "user_name": user_name,
                },
                comment_submit_params.CommentSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentSubmitResponse,
        )


class AsyncCommentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#with_streaming_response
        """
        return AsyncCommentResourceWithStreamingResponse(self)

    async def submit(
        self,
        *,
        charge_point_id: int,
        checkin_status_type_id: int | Omit = omit,
        comment: str | Omit = omit,
        comment_type_id: int | Omit = omit,
        rating: int | Omit = omit,
        related_url: str | Omit = omit,
        user_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentSubmitResponse:
        """
        Submit a user comment or checkin for a specific charging location

        Args:
          charge_point_id: This must be a valid POI ID

          checkin_status_type_id: Optional valid CheckStatusTypeID to indicate overall catgeory and
              success/failure to use equipment e.g. 10 = Charged Successfully.

          comment: This is an optional comment to describe the charging experience, may include
              guidance for future users.

          comment_type_id: This must be a valid Comment Type ID as per UserCommentTypes found in Core
              Reference Data. If left as null then General Comment will be used.

          rating: Optional integer rating between 1 = Worst, 5 = Best.

          related_url: Optional website URL for related information

          user_name: This is an optional name to associate with the submission, for authenticated
              users their profile username is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/comment",
            body=await async_maybe_transform(
                {
                    "charge_point_id": charge_point_id,
                    "checkin_status_type_id": checkin_status_type_id,
                    "comment": comment,
                    "comment_type_id": comment_type_id,
                    "rating": rating,
                    "related_url": related_url,
                    "user_name": user_name,
                },
                comment_submit_params.CommentSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentSubmitResponse,
        )


class CommentResourceWithRawResponse:
    def __init__(self, comment: CommentResource) -> None:
        self._comment = comment

        self.submit = to_raw_response_wrapper(
            comment.submit,
        )


class AsyncCommentResourceWithRawResponse:
    def __init__(self, comment: AsyncCommentResource) -> None:
        self._comment = comment

        self.submit = async_to_raw_response_wrapper(
            comment.submit,
        )


class CommentResourceWithStreamingResponse:
    def __init__(self, comment: CommentResource) -> None:
        self._comment = comment

        self.submit = to_streamed_response_wrapper(
            comment.submit,
        )


class AsyncCommentResourceWithStreamingResponse:
    def __init__(self, comment: AsyncCommentResource) -> None:
        self._comment = comment

        self.submit = async_to_streamed_response_wrapper(
            comment.submit,
        )
