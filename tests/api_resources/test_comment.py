# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ocm import Ocm, AsyncOcm
from ocm.types import CommentSubmitResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Ocm) -> None:
        comment = client.comment.submit(
            charge_point_id=0,
        )
        assert_matches_type(CommentSubmitResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: Ocm) -> None:
        comment = client.comment.submit(
            charge_point_id=0,
            checkin_status_type_id=0,
            comment="string",
            comment_type_id=0,
            rating=3,
            related_url="string",
            user_name="string",
        )
        assert_matches_type(CommentSubmitResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Ocm) -> None:
        response = client.comment.with_raw_response.submit(
            charge_point_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentSubmitResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Ocm) -> None:
        with client.comment.with_streaming_response.submit(
            charge_point_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentSubmitResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncComment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncOcm) -> None:
        comment = await async_client.comment.submit(
            charge_point_id=0,
        )
        assert_matches_type(CommentSubmitResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncOcm) -> None:
        comment = await async_client.comment.submit(
            charge_point_id=0,
            checkin_status_type_id=0,
            comment="string",
            comment_type_id=0,
            rating=3,
            related_url="string",
            user_name="string",
        )
        assert_matches_type(CommentSubmitResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncOcm) -> None:
        response = await async_client.comment.with_raw_response.submit(
            charge_point_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentSubmitResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncOcm) -> None:
        async with async_client.comment.with_streaming_response.submit(
            charge_point_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentSubmitResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True
