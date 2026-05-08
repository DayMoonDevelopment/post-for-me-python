# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TwitterPoll"]


class TwitterPoll(BaseModel):
    duration_minutes: float
    """Duration of the poll in minutes"""

    options: List[str]
    """The choices of the poll, requiring 2-4 options"""

    reply_settings: Optional[Literal["following", "mentionedUsers", "subscribers", "verified"]] = None
    """Who can reply to the tweet"""
