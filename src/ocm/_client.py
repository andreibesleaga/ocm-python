# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import poi, comment, openapi, profile, mediaitem, referencedata
    from .resources.poi import PoiResource, AsyncPoiResource
    from .resources.comment import CommentResource, AsyncCommentResource
    from .resources.openapi import OpenAPIResource, AsyncOpenAPIResource
    from .resources.profile import ProfileResource, AsyncProfileResource
    from .resources.mediaitem import MediaitemResource, AsyncMediaitemResource
    from .resources.referencedata import ReferencedataResource, AsyncReferencedataResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Ocm", "AsyncOcm", "Client", "AsyncClient"]


class Ocm(SyncAPIClient):
    # client options
    api_key: str | None
    api_key_header: str | None
    bearer: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_key_header: str | None = None,
        bearer: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Ocm client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `OCM_API_KEY`
        - `api_key_header` from `OCM_API_KEY`
        - `bearer` from `OCM_USERNAME`
        """
        if api_key is None:
            api_key = os.environ.get("OCM_API_KEY")
        self.api_key = api_key

        if api_key_header is None:
            api_key_header = os.environ.get("OCM_API_KEY")
        self.api_key_header = api_key_header

        if bearer is None:
            bearer = os.environ.get("OCM_USERNAME")
        self.bearer = bearer

        if base_url is None:
            base_url = os.environ.get("OCM_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openchargemap.io/v3"

        custom_headers_env = os.environ.get("OCM_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def poi(self) -> PoiResource:
        from .resources.poi import PoiResource

        return PoiResource(self)

    @cached_property
    def referencedata(self) -> ReferencedataResource:
        from .resources.referencedata import ReferencedataResource

        return ReferencedataResource(self)

    @cached_property
    def profile(self) -> ProfileResource:
        from .resources.profile import ProfileResource

        return ProfileResource(self)

    @cached_property
    def comment(self) -> CommentResource:
        from .resources.comment import CommentResource

        return CommentResource(self)

    @cached_property
    def mediaitem(self) -> MediaitemResource:
        from .resources.mediaitem import MediaitemResource

        return MediaitemResource(self)

    @cached_property
    def openapi(self) -> OpenAPIResource:
        from .resources.openapi import OpenAPIResource

        return OpenAPIResource(self)

    @cached_property
    def with_raw_response(self) -> OcmWithRawResponse:
        return OcmWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OcmWithStreamedResponse:
        return OcmWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_header, **self._user_authentication}

    @property
    def _api_key_header(self) -> dict[str, str]:
        api_key_header = self.api_key_header
        if api_key_header is None:
            return {}
        return {"X-API-Key": api_key_header}

    @property
    def _user_authentication(self) -> dict[str, str]:
        bearer = self.bearer
        if bearer is None:
            return {}
        return {"Authorization": f"Bearer {bearer}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "key": self.api_key if self.api_key is not None else Omit(),
            **self._custom_query,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_key_header: str | None = None,
        bearer: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            api_key_header=api_key_header or self.api_key_header,
            bearer=bearer or self.bearer,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOcm(AsyncAPIClient):
    # client options
    api_key: str | None
    api_key_header: str | None
    bearer: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_key_header: str | None = None,
        bearer: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncOcm client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `OCM_API_KEY`
        - `api_key_header` from `OCM_API_KEY`
        - `bearer` from `OCM_USERNAME`
        """
        if api_key is None:
            api_key = os.environ.get("OCM_API_KEY")
        self.api_key = api_key

        if api_key_header is None:
            api_key_header = os.environ.get("OCM_API_KEY")
        self.api_key_header = api_key_header

        if bearer is None:
            bearer = os.environ.get("OCM_USERNAME")
        self.bearer = bearer

        if base_url is None:
            base_url = os.environ.get("OCM_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openchargemap.io/v3"

        custom_headers_env = os.environ.get("OCM_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def poi(self) -> AsyncPoiResource:
        from .resources.poi import AsyncPoiResource

        return AsyncPoiResource(self)

    @cached_property
    def referencedata(self) -> AsyncReferencedataResource:
        from .resources.referencedata import AsyncReferencedataResource

        return AsyncReferencedataResource(self)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        from .resources.profile import AsyncProfileResource

        return AsyncProfileResource(self)

    @cached_property
    def comment(self) -> AsyncCommentResource:
        from .resources.comment import AsyncCommentResource

        return AsyncCommentResource(self)

    @cached_property
    def mediaitem(self) -> AsyncMediaitemResource:
        from .resources.mediaitem import AsyncMediaitemResource

        return AsyncMediaitemResource(self)

    @cached_property
    def openapi(self) -> AsyncOpenAPIResource:
        from .resources.openapi import AsyncOpenAPIResource

        return AsyncOpenAPIResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncOcmWithRawResponse:
        return AsyncOcmWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOcmWithStreamedResponse:
        return AsyncOcmWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_header, **self._user_authentication}

    @property
    def _api_key_header(self) -> dict[str, str]:
        api_key_header = self.api_key_header
        if api_key_header is None:
            return {}
        return {"X-API-Key": api_key_header}

    @property
    def _user_authentication(self) -> dict[str, str]:
        bearer = self.bearer
        if bearer is None:
            return {}
        return {"Authorization": f"Bearer {bearer}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "key": self.api_key if self.api_key is not None else Omit(),
            **self._custom_query,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_key_header: str | None = None,
        bearer: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            api_key_header=api_key_header or self.api_key_header,
            bearer=bearer or self.bearer,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OcmWithRawResponse:
    _client: Ocm

    def __init__(self, client: Ocm) -> None:
        self._client = client

    @cached_property
    def poi(self) -> poi.PoiResourceWithRawResponse:
        from .resources.poi import PoiResourceWithRawResponse

        return PoiResourceWithRawResponse(self._client.poi)

    @cached_property
    def referencedata(self) -> referencedata.ReferencedataResourceWithRawResponse:
        from .resources.referencedata import ReferencedataResourceWithRawResponse

        return ReferencedataResourceWithRawResponse(self._client.referencedata)

    @cached_property
    def profile(self) -> profile.ProfileResourceWithRawResponse:
        from .resources.profile import ProfileResourceWithRawResponse

        return ProfileResourceWithRawResponse(self._client.profile)

    @cached_property
    def comment(self) -> comment.CommentResourceWithRawResponse:
        from .resources.comment import CommentResourceWithRawResponse

        return CommentResourceWithRawResponse(self._client.comment)

    @cached_property
    def mediaitem(self) -> mediaitem.MediaitemResourceWithRawResponse:
        from .resources.mediaitem import MediaitemResourceWithRawResponse

        return MediaitemResourceWithRawResponse(self._client.mediaitem)

    @cached_property
    def openapi(self) -> openapi.OpenAPIResourceWithRawResponse:
        from .resources.openapi import OpenAPIResourceWithRawResponse

        return OpenAPIResourceWithRawResponse(self._client.openapi)


class AsyncOcmWithRawResponse:
    _client: AsyncOcm

    def __init__(self, client: AsyncOcm) -> None:
        self._client = client

    @cached_property
    def poi(self) -> poi.AsyncPoiResourceWithRawResponse:
        from .resources.poi import AsyncPoiResourceWithRawResponse

        return AsyncPoiResourceWithRawResponse(self._client.poi)

    @cached_property
    def referencedata(self) -> referencedata.AsyncReferencedataResourceWithRawResponse:
        from .resources.referencedata import AsyncReferencedataResourceWithRawResponse

        return AsyncReferencedataResourceWithRawResponse(self._client.referencedata)

    @cached_property
    def profile(self) -> profile.AsyncProfileResourceWithRawResponse:
        from .resources.profile import AsyncProfileResourceWithRawResponse

        return AsyncProfileResourceWithRawResponse(self._client.profile)

    @cached_property
    def comment(self) -> comment.AsyncCommentResourceWithRawResponse:
        from .resources.comment import AsyncCommentResourceWithRawResponse

        return AsyncCommentResourceWithRawResponse(self._client.comment)

    @cached_property
    def mediaitem(self) -> mediaitem.AsyncMediaitemResourceWithRawResponse:
        from .resources.mediaitem import AsyncMediaitemResourceWithRawResponse

        return AsyncMediaitemResourceWithRawResponse(self._client.mediaitem)

    @cached_property
    def openapi(self) -> openapi.AsyncOpenAPIResourceWithRawResponse:
        from .resources.openapi import AsyncOpenAPIResourceWithRawResponse

        return AsyncOpenAPIResourceWithRawResponse(self._client.openapi)


class OcmWithStreamedResponse:
    _client: Ocm

    def __init__(self, client: Ocm) -> None:
        self._client = client

    @cached_property
    def poi(self) -> poi.PoiResourceWithStreamingResponse:
        from .resources.poi import PoiResourceWithStreamingResponse

        return PoiResourceWithStreamingResponse(self._client.poi)

    @cached_property
    def referencedata(self) -> referencedata.ReferencedataResourceWithStreamingResponse:
        from .resources.referencedata import ReferencedataResourceWithStreamingResponse

        return ReferencedataResourceWithStreamingResponse(self._client.referencedata)

    @cached_property
    def profile(self) -> profile.ProfileResourceWithStreamingResponse:
        from .resources.profile import ProfileResourceWithStreamingResponse

        return ProfileResourceWithStreamingResponse(self._client.profile)

    @cached_property
    def comment(self) -> comment.CommentResourceWithStreamingResponse:
        from .resources.comment import CommentResourceWithStreamingResponse

        return CommentResourceWithStreamingResponse(self._client.comment)

    @cached_property
    def mediaitem(self) -> mediaitem.MediaitemResourceWithStreamingResponse:
        from .resources.mediaitem import MediaitemResourceWithStreamingResponse

        return MediaitemResourceWithStreamingResponse(self._client.mediaitem)

    @cached_property
    def openapi(self) -> openapi.OpenAPIResourceWithStreamingResponse:
        from .resources.openapi import OpenAPIResourceWithStreamingResponse

        return OpenAPIResourceWithStreamingResponse(self._client.openapi)


class AsyncOcmWithStreamedResponse:
    _client: AsyncOcm

    def __init__(self, client: AsyncOcm) -> None:
        self._client = client

    @cached_property
    def poi(self) -> poi.AsyncPoiResourceWithStreamingResponse:
        from .resources.poi import AsyncPoiResourceWithStreamingResponse

        return AsyncPoiResourceWithStreamingResponse(self._client.poi)

    @cached_property
    def referencedata(self) -> referencedata.AsyncReferencedataResourceWithStreamingResponse:
        from .resources.referencedata import AsyncReferencedataResourceWithStreamingResponse

        return AsyncReferencedataResourceWithStreamingResponse(self._client.referencedata)

    @cached_property
    def profile(self) -> profile.AsyncProfileResourceWithStreamingResponse:
        from .resources.profile import AsyncProfileResourceWithStreamingResponse

        return AsyncProfileResourceWithStreamingResponse(self._client.profile)

    @cached_property
    def comment(self) -> comment.AsyncCommentResourceWithStreamingResponse:
        from .resources.comment import AsyncCommentResourceWithStreamingResponse

        return AsyncCommentResourceWithStreamingResponse(self._client.comment)

    @cached_property
    def mediaitem(self) -> mediaitem.AsyncMediaitemResourceWithStreamingResponse:
        from .resources.mediaitem import AsyncMediaitemResourceWithStreamingResponse

        return AsyncMediaitemResourceWithStreamingResponse(self._client.mediaitem)

    @cached_property
    def openapi(self) -> openapi.AsyncOpenAPIResourceWithStreamingResponse:
        from .resources.openapi import AsyncOpenAPIResourceWithStreamingResponse

        return AsyncOpenAPIResourceWithStreamingResponse(self._client.openapi)


Client = Ocm

AsyncClient = AsyncOcm
