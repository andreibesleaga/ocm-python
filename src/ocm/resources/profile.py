# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import profile_authenticate_params
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
from ..types.profile_authenticate_response import ProfileAuthenticateResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def authenticate(
        self,
        *,
        emailaddress: str | Omit = omit,
        password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileAuthenticateResponse:
        """
        Perform user authentication, returning a model which includes the users profile
        and a JWT auth token to re-use in subsequent requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/profile/authenticate",
            body=maybe_transform(
                {
                    "emailaddress": emailaddress,
                    "password": password,
                },
                profile_authenticate_params.ProfileAuthenticateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileAuthenticateResponse,
        )


class AsyncProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def authenticate(
        self,
        *,
        emailaddress: str | Omit = omit,
        password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileAuthenticateResponse:
        """
        Perform user authentication, returning a model which includes the users profile
        and a JWT auth token to re-use in subsequent requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/profile/authenticate",
            body=await async_maybe_transform(
                {
                    "emailaddress": emailaddress,
                    "password": password,
                },
                profile_authenticate_params.ProfileAuthenticateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileAuthenticateResponse,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.authenticate = to_raw_response_wrapper(
            profile.authenticate,
        )


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.authenticate = async_to_raw_response_wrapper(
            profile.authenticate,
        )


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.authenticate = to_streamed_response_wrapper(
            profile.authenticate,
        )


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.authenticate = async_to_streamed_response_wrapper(
            profile.authenticate,
        )
