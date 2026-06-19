# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CommentSubmitResponse"]


class CommentSubmitResponse(BaseModel):
    description: str

    status: str
