# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Country"]


class Country(BaseModel):
    """Country details"""

    continent_code: str = FieldInfo(alias="ContinentCode")
    """The Continentcode Schema"""

    id: int = FieldInfo(alias="ID")
    """The Id Schema"""

    iso_code: str = FieldInfo(alias="ISOCode")
    """The Isocode Schema"""

    title: Optional[str] = FieldInfo(alias="Title", default=None)
    """The Title Schema"""
