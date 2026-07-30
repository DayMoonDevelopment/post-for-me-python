# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TwitterPollParam"]


class TwitterPollParam(TypedDict, total=False):
    duration_minutes: Required[float]
    """Duration of the poll in minutes"""

    options: Required[SequenceNotStr[str]]
    """The choices of the poll, requiring 2-4 options"""

    reply_settings: Literal["following", "mentionedUsers", "subscribers", "verified"]
    """Who can reply to the tweet"""
