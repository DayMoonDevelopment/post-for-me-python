# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .social_post_media import SocialPostMedia

__all__ = ["SocialPostPreview"]


class SocialPostPreview(BaseModel):
    caption: str
    """Caption text for the post"""

    platform: str
    """Platform of the post"""

    social_account_id: str
    """Id of the social account"""

    configuration: Optional[object] = None
    """Additional configuration for this platform"""

    media: Optional[List[SocialPostMedia]] = None
    """Array of media URLs associated with the post"""

    social_account_profile_picture_url: Optional[object] = None
    """Url of the social account profile picture"""

    social_account_username: Optional[object] = None
    """Username of the social account"""
