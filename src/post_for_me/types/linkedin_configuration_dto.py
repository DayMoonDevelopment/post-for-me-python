# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .social_post_media import SocialPostMedia

__all__ = ["LinkedinConfigurationDto"]


class LinkedinConfigurationDto(BaseModel):
    caption: Optional[object] = None
    """Overrides the `caption` from the post"""

    media: Optional[List[SocialPostMedia]] = None
    """Overrides the `media` from the post"""

    reshare_post_id: Optional[str] = None
    """LinkedIn UGC post id to reshare. The caption is used as the reshare commentary."""
