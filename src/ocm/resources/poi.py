# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import poi_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.poi_list_response import PoiListResponse

__all__ = ["PoiResource", "AsyncPoiResource"]


class PoiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#accessing-raw-response-data-eg-headers
        """
        return PoiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#with_streaming_response
        """
        return PoiResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        boundingbox: Iterable[object] | Omit = omit,
        camelcase: bool | Omit = omit,
        chargepointid: str | Omit = omit,
        client: str | Omit = omit,
        compact: bool | Omit = omit,
        connectiontypeid: Iterable[object] | Omit = omit,
        countrycode: str | Omit = omit,
        countryid: SequenceNotStr[str] | Omit = omit,
        dataproviderid: Iterable[object] | Omit = omit,
        distance: float | Omit = omit,
        distanceunit: str | Omit = omit,
        greaterthanid: str | Omit = omit,
        includecomments: bool | Omit = omit,
        latitude: int | Omit = omit,
        levelid: Iterable[object] | Omit = omit,
        longitude: float | Omit = omit,
        maxresults: int | Omit = omit,
        modifiedsince: str | Omit = omit,
        opendata: bool | Omit = omit,
        operatorid: Iterable[object] | Omit = omit,
        output: str | Omit = omit,
        polygon: str | Omit = omit,
        polyline: str | Omit = omit,
        sortby: str | Omit = omit,
        statustypeid: Iterable[object] | Omit = omit,
        usagetypeid: Iterable[object] | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PoiListResponse:
        """
        Used to fetch a list of POIs (sites) within a geographic boundary or near a
        specific latitude/longitude. This is the primary method for most applications
        and services to consume data from Open Charge Map.

        Args:
          boundingbox: Filter results to a given bounding box. specify top left and bottom right box
              corners as: (lat,lng),(lat2,lng2)

          camelcase: Set to true to get a property names in camelCase format.

          chargepointid: Exact match on a given OCM POI ID (comma separated list)

          client: String to identify your client application. Optional but recommended to
              distinguish your client from other bots/crawlers

          compact: Set to true to remove reference data objects from output (just returns IDs for
              common reference data such as DataProvider etc).

          connectiontypeid: Exact match on a given connection type id (comma separated list)

          countrycode: 2-character ISO Country code to filter to one specific country

          countryid: Exact match on a given numeric country id (comma separated list)

          dataproviderid: Exact match on a given data provider id id (comma separated list).

          distance: Optionally filter results by a max distance from the given latitude/longitude

          distanceunit: `miles` or `km` distance unit

          greaterthanid: Filter to items with ID greater than given value

          includecomments: If true, user comments and media items will be include in result set

          latitude: Latitude for distance calculation and filtering

          levelid: Exact match on a given charging level (1-3) id (comma separated list)

          longitude: Longitude for distance calculation and filtering

          maxresults: Limit on max number of results returned

          modifiedsince: Filter to results modified after the given date

          opendata: Use opendata=true for only OCM provided ("Open") data.

          operatorid: Exact match on a given EVSE operator id (comma separated list)

          output: Optional output format `json`,`geojson`,`xml`,`csv`, JSON is the default and
              recommended as the highest fidelity.

          polygon: Filter results within a given Polygon. Specify an encoded polyline for the
              polygon shape. Polygon will be automatically closed from the last point to the
              first point.

          polyline: Filter results along an encoded polyline, use with distance param to increase
              search distance along line. Polyline is expanded into a polygon to cover the
              search distance.

          sortby: Default sort order is based on spatial index but you can optionally sort by
              `modified_asc` for results in order of modification (oldest to newest), or
              ` id_asc` for results in order of ID

          statustypeid: Exact match on a given status type id (comma separated list)

          usagetypeid: Exact match on a given usage type id (comma separated list)

          verbose: Set to false to get a smaller result set with null items removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/poi",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "boundingbox": boundingbox,
                        "camelcase": camelcase,
                        "chargepointid": chargepointid,
                        "client": client,
                        "compact": compact,
                        "connectiontypeid": connectiontypeid,
                        "countrycode": countrycode,
                        "countryid": countryid,
                        "dataproviderid": dataproviderid,
                        "distance": distance,
                        "distanceunit": distanceunit,
                        "greaterthanid": greaterthanid,
                        "includecomments": includecomments,
                        "latitude": latitude,
                        "levelid": levelid,
                        "longitude": longitude,
                        "maxresults": maxresults,
                        "modifiedsince": modifiedsince,
                        "opendata": opendata,
                        "operatorid": operatorid,
                        "output": output,
                        "polygon": polygon,
                        "polyline": polyline,
                        "sortby": sortby,
                        "statustypeid": statustypeid,
                        "usagetypeid": usagetypeid,
                        "verbose": verbose,
                    },
                    poi_list_params.PoiListParams,
                ),
            ),
            cast_to=PoiListResponse,
        )


class AsyncPoiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/ocm-python#with_streaming_response
        """
        return AsyncPoiResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        boundingbox: Iterable[object] | Omit = omit,
        camelcase: bool | Omit = omit,
        chargepointid: str | Omit = omit,
        client: str | Omit = omit,
        compact: bool | Omit = omit,
        connectiontypeid: Iterable[object] | Omit = omit,
        countrycode: str | Omit = omit,
        countryid: SequenceNotStr[str] | Omit = omit,
        dataproviderid: Iterable[object] | Omit = omit,
        distance: float | Omit = omit,
        distanceunit: str | Omit = omit,
        greaterthanid: str | Omit = omit,
        includecomments: bool | Omit = omit,
        latitude: int | Omit = omit,
        levelid: Iterable[object] | Omit = omit,
        longitude: float | Omit = omit,
        maxresults: int | Omit = omit,
        modifiedsince: str | Omit = omit,
        opendata: bool | Omit = omit,
        operatorid: Iterable[object] | Omit = omit,
        output: str | Omit = omit,
        polygon: str | Omit = omit,
        polyline: str | Omit = omit,
        sortby: str | Omit = omit,
        statustypeid: Iterable[object] | Omit = omit,
        usagetypeid: Iterable[object] | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PoiListResponse:
        """
        Used to fetch a list of POIs (sites) within a geographic boundary or near a
        specific latitude/longitude. This is the primary method for most applications
        and services to consume data from Open Charge Map.

        Args:
          boundingbox: Filter results to a given bounding box. specify top left and bottom right box
              corners as: (lat,lng),(lat2,lng2)

          camelcase: Set to true to get a property names in camelCase format.

          chargepointid: Exact match on a given OCM POI ID (comma separated list)

          client: String to identify your client application. Optional but recommended to
              distinguish your client from other bots/crawlers

          compact: Set to true to remove reference data objects from output (just returns IDs for
              common reference data such as DataProvider etc).

          connectiontypeid: Exact match on a given connection type id (comma separated list)

          countrycode: 2-character ISO Country code to filter to one specific country

          countryid: Exact match on a given numeric country id (comma separated list)

          dataproviderid: Exact match on a given data provider id id (comma separated list).

          distance: Optionally filter results by a max distance from the given latitude/longitude

          distanceunit: `miles` or `km` distance unit

          greaterthanid: Filter to items with ID greater than given value

          includecomments: If true, user comments and media items will be include in result set

          latitude: Latitude for distance calculation and filtering

          levelid: Exact match on a given charging level (1-3) id (comma separated list)

          longitude: Longitude for distance calculation and filtering

          maxresults: Limit on max number of results returned

          modifiedsince: Filter to results modified after the given date

          opendata: Use opendata=true for only OCM provided ("Open") data.

          operatorid: Exact match on a given EVSE operator id (comma separated list)

          output: Optional output format `json`,`geojson`,`xml`,`csv`, JSON is the default and
              recommended as the highest fidelity.

          polygon: Filter results within a given Polygon. Specify an encoded polyline for the
              polygon shape. Polygon will be automatically closed from the last point to the
              first point.

          polyline: Filter results along an encoded polyline, use with distance param to increase
              search distance along line. Polyline is expanded into a polygon to cover the
              search distance.

          sortby: Default sort order is based on spatial index but you can optionally sort by
              `modified_asc` for results in order of modification (oldest to newest), or
              ` id_asc` for results in order of ID

          statustypeid: Exact match on a given status type id (comma separated list)

          usagetypeid: Exact match on a given usage type id (comma separated list)

          verbose: Set to false to get a smaller result set with null items removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/poi",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "boundingbox": boundingbox,
                        "camelcase": camelcase,
                        "chargepointid": chargepointid,
                        "client": client,
                        "compact": compact,
                        "connectiontypeid": connectiontypeid,
                        "countrycode": countrycode,
                        "countryid": countryid,
                        "dataproviderid": dataproviderid,
                        "distance": distance,
                        "distanceunit": distanceunit,
                        "greaterthanid": greaterthanid,
                        "includecomments": includecomments,
                        "latitude": latitude,
                        "levelid": levelid,
                        "longitude": longitude,
                        "maxresults": maxresults,
                        "modifiedsince": modifiedsince,
                        "opendata": opendata,
                        "operatorid": operatorid,
                        "output": output,
                        "polygon": polygon,
                        "polyline": polyline,
                        "sortby": sortby,
                        "statustypeid": statustypeid,
                        "usagetypeid": usagetypeid,
                        "verbose": verbose,
                    },
                    poi_list_params.PoiListParams,
                ),
            ),
            cast_to=PoiListResponse,
        )


class PoiResourceWithRawResponse:
    def __init__(self, poi: PoiResource) -> None:
        self._poi = poi

        self.list = to_raw_response_wrapper(
            poi.list,
        )


class AsyncPoiResourceWithRawResponse:
    def __init__(self, poi: AsyncPoiResource) -> None:
        self._poi = poi

        self.list = async_to_raw_response_wrapper(
            poi.list,
        )


class PoiResourceWithStreamingResponse:
    def __init__(self, poi: PoiResource) -> None:
        self._poi = poi

        self.list = to_streamed_response_wrapper(
            poi.list,
        )


class AsyncPoiResourceWithStreamingResponse:
    def __init__(self, poi: AsyncPoiResource) -> None:
        self._poi = poi

        self.list = async_to_streamed_response_wrapper(
            poi.list,
        )
