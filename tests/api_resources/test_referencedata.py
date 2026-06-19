# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ocm import Ocm, AsyncOcm
from ocm.types import ReferencedataRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReferencedata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Ocm) -> None:
        referencedata = client.referencedata.retrieve()
        assert_matches_type(ReferencedataRetrieveResponse, referencedata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Ocm) -> None:
        referencedata = client.referencedata.retrieve(
            countryid=[{}],
        )
        assert_matches_type(ReferencedataRetrieveResponse, referencedata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Ocm) -> None:
        response = client.referencedata.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        referencedata = response.parse()
        assert_matches_type(ReferencedataRetrieveResponse, referencedata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Ocm) -> None:
        with client.referencedata.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            referencedata = response.parse()
            assert_matches_type(ReferencedataRetrieveResponse, referencedata, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReferencedata:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOcm) -> None:
        referencedata = await async_client.referencedata.retrieve()
        assert_matches_type(ReferencedataRetrieveResponse, referencedata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOcm) -> None:
        referencedata = await async_client.referencedata.retrieve(
            countryid=[{}],
        )
        assert_matches_type(ReferencedataRetrieveResponse, referencedata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOcm) -> None:
        response = await async_client.referencedata.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        referencedata = await response.parse()
        assert_matches_type(ReferencedataRetrieveResponse, referencedata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOcm) -> None:
        async with async_client.referencedata.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            referencedata = await response.parse()
            assert_matches_type(ReferencedataRetrieveResponse, referencedata, path=["response"])

        assert cast(Any, response.is_closed) is True
