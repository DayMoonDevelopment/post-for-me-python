# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PinterestConfigurationDtoParam"]


class PinterestConfigurationDtoParam(TypedDict, total=False):
    board_ids: Optional[SequenceNotStr[str]]
    """Pinterest board IDs"""

    caption: Optional[object]
    """Overrides the `caption` from the post"""

    link: Optional[str]
    """Pinterest post link"""

    media: Optional[SequenceNotStr[str]]
    """Overrides the `media` from the post"""
