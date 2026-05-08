# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .social_post_media_param import SocialPostMediaParam

__all__ = ["PinterestConfigurationDtoParam"]


class PinterestConfigurationDtoParam(TypedDict, total=False):
    board_ids: Optional[SequenceNotStr[str]]
    """Pinterest board IDs"""

    caption: Optional[object]
    """Overrides the `caption` from the post"""

    link: Optional[str]
    """Pinterest post link"""

    media: Optional[Iterable[SocialPostMediaParam]]
    """Overrides the `media` from the post"""

    title: Optional[str]
    """Overrides the `title` from the post for Pinterest"""
