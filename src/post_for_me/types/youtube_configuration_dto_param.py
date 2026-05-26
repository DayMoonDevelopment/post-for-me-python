# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .social_post_media_param import SocialPostMediaParam

__all__ = ["YoutubeConfigurationDtoParam"]


class YoutubeConfigurationDtoParam(TypedDict, total=False):
    caption: Optional[object]
    """Overrides the `caption` from the post"""

    contains_synthetic_media: Optional[bool]
    """
    If true, marks the video as containing altered or synthetic content per
    YouTube's disclosure policy. Sets status.containsSyntheticMedia on the YouTube
    Data API videos.insert call; YouTube adds a "How this content was made" label to
    the description automatically.
    """

    made_for_kids: Optional[bool]
    """If true will notify YouTube the video is intended for kids, defaults to false"""

    media: Optional[Iterable[SocialPostMediaParam]]
    """Overrides the `media` from the post"""

    privacy_status: Optional[Literal["public", "private", "unlisted"]]
    """Sets the privacy status of the video, will default to public"""

    title: Optional[str]
    """Overrides the `title` from the post"""
