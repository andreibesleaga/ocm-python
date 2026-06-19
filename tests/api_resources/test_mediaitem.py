# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ocm import Ocm, AsyncOcm
from ocm.types import MediaitemCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMediaitem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Ocm) -> None:
        mediaitem = client.mediaitem.create(
            charge_point_id=1234,
            image_data_base64="data:image/jpeg;base64,<BASE64_ENCODED_DATA>",
        )
        assert_matches_type(MediaitemCreateResponse, mediaitem, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Ocm) -> None:
        mediaitem = client.mediaitem.create(
            charge_point_id=1234,
            image_data_base64="data:image/jpeg;base64,<BASE64_ENCODED_DATA>",
            comment="An example comment",
        )
        assert_matches_type(MediaitemCreateResponse, mediaitem, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Ocm) -> None:
        response = client.mediaitem.with_raw_response.create(
            charge_point_id=1234,
            image_data_base64="data:image/jpeg;base64,<BASE64_ENCODED_DATA>",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mediaitem = response.parse()
        assert_matches_type(MediaitemCreateResponse, mediaitem, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Ocm) -> None:
        with client.mediaitem.with_streaming_response.create(
            charge_point_id=1234,
            image_data_base64="data:image/jpeg;base64,<BASE64_ENCODED_DATA>",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mediaitem = response.parse()
            assert_matches_type(MediaitemCreateResponse, mediaitem, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMediaitem:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOcm) -> None:
        mediaitem = await async_client.mediaitem.create(
            charge_point_id=1234,
            image_data_base64="data:image/jpeg;base64,<BASE64_ENCODED_DATA>",
        )
        assert_matches_type(MediaitemCreateResponse, mediaitem, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOcm) -> None:
        mediaitem = await async_client.mediaitem.create(
            charge_point_id=1234,
            image_data_base64="data:image/jpeg;base64,<BASE64_ENCODED_DATA>",
            comment="An example comment",
        )
        assert_matches_type(MediaitemCreateResponse, mediaitem, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOcm) -> None:
        response = await async_client.mediaitem.with_raw_response.create(
            charge_point_id=1234,
            image_data_base64="data:image/jpeg;base64,<BASE64_ENCODED_DATA>",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mediaitem = await response.parse()
        assert_matches_type(MediaitemCreateResponse, mediaitem, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOcm) -> None:
        async with async_client.mediaitem.with_streaming_response.create(
            charge_point_id=1234,
            image_data_base64="data:image/jpeg;base64,<BASE64_ENCODED_DATA>",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mediaitem = await response.parse()
            assert_matches_type(MediaitemCreateResponse, mediaitem, path=["response"])

        assert cast(Any, response.is_closed) is True
