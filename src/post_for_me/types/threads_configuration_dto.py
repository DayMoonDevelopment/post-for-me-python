# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .social_post_media import SocialPostMedia

__all__ = ["ThreadsConfigurationDto"]


class ThreadsConfigurationDto(BaseModel):
    caption: Optional[object] = None
    """Overrides the `caption` from the post"""

    media: Optional[List[SocialPostMedia]] = None
    """Overrides the `media` from the post"""

    placement: Optional[Literal["reels", "timeline"]] = None
    """Threads post placement"""
