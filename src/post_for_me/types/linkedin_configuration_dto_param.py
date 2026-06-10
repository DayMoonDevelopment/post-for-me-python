# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .social_post_media_param import SocialPostMediaParam

__all__ = ["LinkedinConfigurationDtoParam"]


class LinkedinConfigurationDtoParam(TypedDict, total=False):
    caption: Optional[object]
    """Overrides the `caption` from the post"""

    media: Optional[Iterable[SocialPostMediaParam]]
    """Overrides the `media` from the post"""

    reshare_post_id: Optional[str]
    """LinkedIn UGC post id to reshare. The caption is used as the reshare commentary."""
