# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["YoutubeConfigurationDtoParam"]


class YoutubeConfigurationDtoParam(TypedDict, total=False):
    caption: Optional[object]
    """Overrides the `caption` from the post"""

    media: Optional[SequenceNotStr[str]]
    """Overrides the `media` from the post"""

    title: Optional[str]
    """Overrides the `title` from the post"""
