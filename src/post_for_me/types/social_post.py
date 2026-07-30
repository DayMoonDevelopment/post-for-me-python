# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .social_account import SocialAccount
from .social_post_media import SocialPostMedia
from .account_configuration import AccountConfiguration
from .platform_configurations_dto import PlatformConfigurationsDto

__all__ = ["SocialPost"]


class SocialPost(BaseModel):
    id: str
    """Unique identifier of the post"""

    account_configurations: Optional[List[AccountConfiguration]] = None
    """Account-specific configurations for the post"""

    caption: str
    """Caption text for the post"""

    created_at: str
    """Timestamp when the post was created"""

    external_id: Optional[str] = None
    """Provided unique identifier of the post"""

    media: Optional[List[SocialPostMedia]] = None
    """Array of media associated with the post"""

    platform_configurations: Optional[PlatformConfigurationsDto] = None
    """Platform-specific configurations for the post"""

    scheduled_at: Optional[str] = None
    """Scheduled date and time for the post"""

    social_accounts: List[SocialAccount]
    """Array of social account IDs for posting"""

    status: Literal["draft", "scheduled", "processing", "processed"]
    """Current status of the post: draft, processed, scheduled, or processing"""

    updated_at: str
    """Timestamp when the post was last updated"""
