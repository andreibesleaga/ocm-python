# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["ReferencedataRetrieveParams"]


class ReferencedataRetrieveParams(TypedDict, total=False):
    countryid: Iterable[object]
    """
    Optional filter on countryid, exact match on a given numeric country id (comma
    separated list)
    """
