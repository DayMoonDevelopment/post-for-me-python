# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["InstagramConfigurationDtoParam"]


class InstagramConfigurationDtoParam(TypedDict, total=False):
    caption: Optional[object]
    """Overrides the `caption` from the post"""

    collaborators: Optional[SequenceNotStr[str]]
    """Instagram usernames to be tagged as a collaborator"""

    media: Optional[SequenceNotStr[str]]
    """Overrides the `media` from the post"""

    placement: Optional[Literal["reels", "stories", "timeline"]]
    """Instagram post placement"""
