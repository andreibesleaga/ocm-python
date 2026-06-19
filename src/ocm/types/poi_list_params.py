# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PoiListParams"]


class PoiListParams(TypedDict, total=False):
    boundingbox: Iterable[object]
    """Filter results to a given bounding box.

    specify top left and bottom right box corners as: (lat,lng),(lat2,lng2)
    """

    camelcase: bool
    """Set to true to get a property names in camelCase format."""

    chargepointid: str
    """Exact match on a given OCM POI ID (comma separated list)"""

    client: str
    """String to identify your client application.

    Optional but recommended to distinguish your client from other bots/crawlers
    """

    compact: bool
    """
    Set to true to remove reference data objects from output (just returns IDs for
    common reference data such as DataProvider etc).
    """

    connectiontypeid: Iterable[object]
    """Exact match on a given connection type id (comma separated list)"""

    countrycode: str
    """2-character ISO Country code to filter to one specific country"""

    countryid: SequenceNotStr[str]
    """Exact match on a given numeric country id (comma separated list)"""

    dataproviderid: Iterable[object]
    """Exact match on a given data provider id id (comma separated list)."""

    distance: float
    """Optionally filter results by a max distance from the given latitude/longitude"""

    distanceunit: str
    """`miles` or `km` distance unit"""

    greaterthanid: str
    """Filter to items with ID greater than given value"""

    includecomments: bool
    """If true, user comments and media items will be include in result set"""

    latitude: int
    """Latitude for distance calculation and filtering"""

    levelid: Iterable[object]
    """Exact match on a given charging level (1-3) id (comma separated list)"""

    longitude: float
    """Longitude for distance calculation and filtering"""

    maxresults: int
    """Limit on max number of results returned"""

    modifiedsince: str
    """Filter to results modified after the given date"""

    opendata: bool
    """Use opendata=true for only OCM provided ("Open") data."""

    operatorid: Iterable[object]
    """Exact match on a given EVSE operator id (comma separated list)"""

    output: str
    """
    Optional output format `json`,`geojson`,`xml`,`csv`, JSON is the default and
    recommended as the highest fidelity.
    """

    polygon: str
    """Filter results within a given Polygon.

    Specify an encoded polyline for the polygon shape. Polygon will be automatically
    closed from the last point to the first point.
    """

    polyline: str
    """
    Filter results along an encoded polyline, use with distance param to increase
    search distance along line. Polyline is expanded into a polygon to cover the
    search distance.
    """

    sortby: str
    """
    Default sort order is based on spatial index but you can optionally sort by
    `modified_asc` for results in order of modification (oldest to newest), or
    ` id_asc` for results in order of ID
    """

    statustypeid: Iterable[object]
    """Exact match on a given status type id (comma separated list)"""

    usagetypeid: Iterable[object]
    """Exact match on a given usage type id (comma separated list)"""

    verbose: bool
    """Set to false to get a smaller result set with null items removed."""
