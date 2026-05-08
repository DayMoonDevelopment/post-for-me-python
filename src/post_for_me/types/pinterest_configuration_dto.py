# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .social_post_media import SocialPostMedia

__all__ = ["PinterestConfigurationDto"]


class PinterestConfigurationDto(BaseModel):
    board_ids: Optional[List[str]] = None
    """Pinterest board IDs"""

    caption: Optional[object] = None
    """Overrides the `caption` from the post"""

    link: Optional[str] = None
    """Pinterest post link"""

    media: Optional[List[SocialPostMedia]] = None
    """Overrides the `media` from the post"""

    title: Optional[str] = None
    """Overrides the `title` from the post for Pinterest"""
