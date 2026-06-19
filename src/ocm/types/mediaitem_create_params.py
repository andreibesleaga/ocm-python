# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MediaitemCreateParams"]


class MediaitemCreateParams(TypedDict, total=False):
    charge_point_id: Required[Annotated[int, PropertyInfo(alias="chargePointID")]]
    """ID value for the OCM site (POI) this image relates to."""

    image_data_base64: Required[Annotated[str, PropertyInfo(alias="imageDataBase64")]]
    """BASE64 encoded data"""

    comment: str
    """Optional description of image or context"""
