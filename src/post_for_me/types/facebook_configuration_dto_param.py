# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .social_post_media_param import SocialPostMediaParam

__all__ = ["FacebookConfigurationDtoParam"]


class FacebookConfigurationDtoParam(TypedDict, total=False):
    caption: Optional[object]
    """Overrides the `caption` from the post"""

    collaborators: Optional[Iterable[Iterable[object]]]
    """List of page ids to invite as collaborators for a Video Reel"""

    location: Optional[str]
    """Page id with a location that you want to tag the image or video with"""

    media: Optional[Iterable[SocialPostMediaParam]]
    """Overrides the `media` from the post"""

    placement: Optional[Literal["reels", "stories", "timeline"]]
    """Facebook post placement"""

    set_caption_for_each_image: Optional[bool]
    """
    If true, include the caption on each image in a carousel upload; if false, only
    include it on the final carousel post
    """
