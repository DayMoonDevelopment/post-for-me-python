# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .social_post_media import SocialPostMedia

__all__ = ["YoutubeConfigurationDto"]


class YoutubeConfigurationDto(BaseModel):
    caption: Optional[object] = None
    """Overrides the `caption` from the post"""

    contains_synthetic_media: Optional[bool] = None
    """
    If true, marks the video as containing altered or synthetic content per
    YouTube's disclosure policy. Sets status.containsSyntheticMedia on the YouTube
    Data API videos.insert call; YouTube adds a "How this content was made" label to
    the description automatically.
    """

    made_for_kids: Optional[bool] = None
    """If true will notify YouTube the video is intended for kids, defaults to false"""

    media: Optional[List[SocialPostMedia]] = None
    """Overrides the `media` from the post"""

    privacy_status: Optional[Literal["public", "private", "unlisted"]] = None
    """Sets the privacy status of the video, will default to public"""

    title: Optional[str] = None
    """Overrides the `title` from the post"""
