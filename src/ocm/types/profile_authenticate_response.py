# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProfileAuthenticateResponse", "Data", "DataUserProfile", "Metadata"]


class DataUserProfile(BaseModel):
    """Full user profile, including non-public fields such as Email Address"""

    date_created: str = FieldInfo(alias="DateCreated")

    id: float = FieldInfo(alias="ID")

    is_profile_public: bool = FieldInfo(alias="IsProfilePublic")

    username: str = FieldInfo(alias="Username")

    date_last_login: Optional[str] = FieldInfo(alias="DateLastLogin", default=None)

    email_address: Optional[str] = FieldInfo(alias="EmailAddress", default=None)

    latitude: Optional[float] = FieldInfo(alias="Latitude", default=None)

    location: Optional[str] = FieldInfo(alias="Location", default=None)

    longitude: Optional[float] = FieldInfo(alias="Longitude", default=None)

    permissions: Optional[str] = FieldInfo(alias="Permissions", default=None)

    profile: Optional[str] = FieldInfo(alias="Profile", default=None)

    profile_image_url: Optional[str] = FieldInfo(alias="ProfileImageURL", default=None)

    reputation_points: Optional[float] = FieldInfo(alias="ReputationPoints", default=None)

    website_url: Optional[str] = FieldInfo(alias="WebsiteURL", default=None)


class Data(BaseModel):
    access_token: str
    """JWT Bearer Token to use in subsequent authenticated requests"""

    user_profile: DataUserProfile = FieldInfo(alias="UserProfile")
    """Full user profile, including non-public fields such as Email Address"""


class Metadata(BaseModel):
    status_code: int = FieldInfo(alias="StatusCode")


class ProfileAuthenticateResponse(BaseModel):
    data: Data = FieldInfo(alias="Data")

    metadata: Metadata = FieldInfo(alias="Metadata")
