# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SocialPostMediaParam", "Tag"]


class Tag(TypedDict, total=False):
    id: Required[str]
    """Facebook User ID, Instagram Username or Instagram product id to tag"""

    platform: Required[Literal["facebook", "instagram"]]
    """The platform for the tags"""

    type: Required[Literal["user", "product"]]
    """
    The type of tag, user to tag accounts, product to tag products (only supported
    for instagram)
    """

    x: float
    """
    Percentage distance from left edge of the image, Not required for videos or
    stories
    """

    y: float
    """
    Percentage distance from top edge of the image, Not required for videos or
    stories
    """


class SocialPostMediaParam(TypedDict, total=False):
    url: Required[str]
    """Public URL of the media"""

    skip_processing: Optional[bool]
    """
    If true the media will not be processed at all and instead be posted as is, this
    may increase chance of post failure if media does not meet platform's
    requirements. Best used for larger files.
    """

    tags: Optional[Iterable[Tag]]
    """List of tags to attach to the media"""

    thumbnail_timestamp_ms: Optional[object]
    """Timestamp in milliseconds of frame to use as thumbnail for the media"""

    thumbnail_url: Optional[object]
    """Public URL of the thumbnail for the media"""
