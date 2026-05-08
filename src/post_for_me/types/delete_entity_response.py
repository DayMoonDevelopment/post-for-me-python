# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DeleteEntityResponse"]


class DeleteEntityResponse(BaseModel):
    success: bool
    """Whether or not the entity was deleted"""
