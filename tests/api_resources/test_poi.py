# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ocm import Ocm, AsyncOcm
from ocm.types import PoiListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPoi:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Ocm) -> None:
        poi = client.poi.list()
        assert_matches_type(PoiListResponse, poi, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Ocm) -> None:
        poi = client.poi.list(
            boundingbox=[{}],
            camelcase=True,
            chargepointid="chargepointid",
            client="client",
            compact=True,
            connectiontypeid=[{}],
            countrycode="countrycode",
            countryid=["string"],
            dataproviderid=[{}],
            distance=0,
            distanceunit="distanceunit",
            greaterthanid="greaterthanid",
            includecomments=True,
            latitude=0,
            levelid=[{}],
            longitude=0,
            maxresults=0,
            modifiedsince="modifiedsince",
            opendata=True,
            operatorid=[{}],
            output="output",
            polygon="polygon",
            polyline="polyline",
            sortby="sortby",
            statustypeid=[{}],
            usagetypeid=[{}],
            verbose=True,
        )
        assert_matches_type(PoiListResponse, poi, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Ocm) -> None:
        response = client.poi.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert_matches_type(PoiListResponse, poi, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Ocm) -> None:
        with client.poi.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert_matches_type(PoiListResponse, poi, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPoi:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOcm) -> None:
        poi = await async_client.poi.list()
        assert_matches_type(PoiListResponse, poi, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOcm) -> None:
        poi = await async_client.poi.list(
            boundingbox=[{}],
            camelcase=True,
            chargepointid="chargepointid",
            client="client",
            compact=True,
            connectiontypeid=[{}],
            countrycode="countrycode",
            countryid=["string"],
            dataproviderid=[{}],
            distance=0,
            distanceunit="distanceunit",
            greaterthanid="greaterthanid",
            includecomments=True,
            latitude=0,
            levelid=[{}],
            longitude=0,
            maxresults=0,
            modifiedsince="modifiedsince",
            opendata=True,
            operatorid=[{}],
            output="output",
            polygon="polygon",
            polyline="polyline",
            sortby="sortby",
            statustypeid=[{}],
            usagetypeid=[{}],
            verbose=True,
        )
        assert_matches_type(PoiListResponse, poi, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOcm) -> None:
        response = await async_client.poi.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert_matches_type(PoiListResponse, poi, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOcm) -> None:
        async with async_client.poi.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert_matches_type(PoiListResponse, poi, path=["response"])

        assert cast(Any, response.is_closed) is True
