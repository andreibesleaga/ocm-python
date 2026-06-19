# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ocm import Ocm, AsyncOcm
from ocm.types import ProfileAuthenticateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_authenticate(self, client: Ocm) -> None:
        profile = client.profile.authenticate()
        assert_matches_type(ProfileAuthenticateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_authenticate_with_all_params(self, client: Ocm) -> None:
        profile = client.profile.authenticate(
            emailaddress="string",
            password="string",
        )
        assert_matches_type(ProfileAuthenticateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_authenticate(self, client: Ocm) -> None:
        response = client.profile.with_raw_response.authenticate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileAuthenticateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_authenticate(self, client: Ocm) -> None:
        with client.profile.with_streaming_response.authenticate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileAuthenticateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_authenticate(self, async_client: AsyncOcm) -> None:
        profile = await async_client.profile.authenticate()
        assert_matches_type(ProfileAuthenticateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_authenticate_with_all_params(self, async_client: AsyncOcm) -> None:
        profile = await async_client.profile.authenticate(
            emailaddress="string",
            password="string",
        )
        assert_matches_type(ProfileAuthenticateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_authenticate(self, async_client: AsyncOcm) -> None:
        response = await async_client.profile.with_raw_response.authenticate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileAuthenticateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_authenticate(self, async_client: AsyncOcm) -> None:
        async with async_client.profile.with_streaming_response.authenticate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileAuthenticateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
