# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CommentSubmitParams"]


class CommentSubmitParams(TypedDict, total=False):
    charge_point_id: Required[Annotated[int, PropertyInfo(alias="chargePointID")]]
    """This must be a valid POI ID"""

    checkin_status_type_id: Annotated[int, PropertyInfo(alias="checkinStatusTypeID")]
    """
    Optional valid CheckStatusTypeID to indicate overall catgeory and
    success/failure to use equipment e.g. 10 = Charged Successfully.
    """

    comment: str
    """
    This is an optional comment to describe the charging experience, may include
    guidance for future users.
    """

    comment_type_id: Annotated[int, PropertyInfo(alias="commentTypeID")]
    """
    This must be a valid Comment Type ID as per UserCommentTypes found in Core
    Reference Data. If left as null then General Comment will be used.
    """

    rating: int
    """Optional integer rating between 1 = Worst, 5 = Best."""

    related_url: Annotated[str, PropertyInfo(alias="relatedURL")]
    """Optional website URL for related information"""

    user_name: Annotated[str, PropertyInfo(alias="userName")]
    """
    This is an optional name to associate with the submission, for authenticated
    users their profile username is used.
    """
