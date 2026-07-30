# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FacebookActivityByActionType"]


class FacebookActivityByActionType(BaseModel):
    action_type: str
    """Action type (e.g., like, comment, share)"""

    value: float
    """Number of actions"""
