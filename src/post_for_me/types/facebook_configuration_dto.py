# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .social_post_media import SocialPostMedia

__all__ = ["FacebookConfigurationDto"]


class FacebookConfigurationDto(BaseModel):
    caption: Optional[object] = None
    """Overrides the `caption` from the post"""

    collaborators: Optional[List[List[object]]] = None
    """List of page ids to invite as collaborators for a Video Reel"""

    location: Optional[str] = None
    """Page id with a location that you want to tag the image or video with"""

    media: Optional[List[SocialPostMedia]] = None
    """Overrides the `media` from the post"""

    placement: Optional[Literal["reels", "stories", "timeline"]] = None
    """Facebook post placement"""

    set_caption_for_each_image: Optional[bool] = None
    """
    If true, include the caption on each image in a carousel upload; if false, only
    include it on the final carousel post
    """
