# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SocialPostResult", "Media", "MediaTag", "PlatformData"]


class MediaTag(BaseModel):
    id: str
    """Facebook User ID, Instagram Username or Instagram product id to tag"""

    platform: Literal["facebook", "instagram"]
    """The platform for the tags"""

    type: Literal["user", "product"]
    """
    The type of tag, user to tag accounts, product to tag products (only supported
    for instagram)
    """

    x: Optional[float] = None
    """
    Percentage distance from left edge of the image, Not required for videos or
    stories
    """

    y: Optional[float] = None
    """
    Percentage distance from top edge of the image, Not required for videos or
    stories
    """


class Media(BaseModel):
    url: str
    """Public URL of the media"""

    skip_processing: Optional[bool] = None
    """
    If true the media will not be processed at all and instead be posted as is, this
    may increase chance of post failure if media does not meet platform's
    requirements. Best used for larger files.
    """

    tags: Optional[List[MediaTag]] = None
    """List of tags to attach to the media"""

    thumbnail_timestamp_ms: Optional[object] = None
    """Timestamp in milliseconds of frame to use as thumbnail for the media"""

    thumbnail_url: Optional[object] = None
    """Public URL of the thumbnail for the media"""


class PlatformData(BaseModel):
    """Platform-specific data"""

    id: Optional[str] = None
    """Platform-specific ID"""

    url: Optional[str] = None
    """URL of the posted content"""


class SocialPostResult(BaseModel):
    id: str
    """The unique identifier of the post result"""

    details: object
    """Detailed logs from the post"""

    error: object
    """Error message if the post failed"""

    media: Optional[List[Media]] = None
    """Array of media URLs associated with the post"""

    platform_data: PlatformData
    """Platform-specific data"""

    post_id: str
    """The ID of the associated post"""

    social_account_id: str
    """The ID of the associated social account"""

    success: bool
    """Indicates if the post was successful"""
