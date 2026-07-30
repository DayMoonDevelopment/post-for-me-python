# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .social_post_media_param import SocialPostMediaParam
from .account_configuration_param import AccountConfigurationParam
from .platform_configurations_dto_param import PlatformConfigurationsDtoParam

__all__ = ["SocialPostPreviewCreateParams", "PreviewSocialAccount"]


class SocialPostPreviewCreateParams(TypedDict, total=False):
    caption: Required[str]
    """Caption text for the post"""

    preview_social_accounts: Required[Iterable[PreviewSocialAccount]]
    """Array of social accounts.

    Can preview non connected accounts, just specify a random ID
    """

    account_configurations: Optional[Iterable[AccountConfigurationParam]]
    """Account-specific configurations for the post"""

    media: Optional[Iterable[SocialPostMediaParam]]
    """Array of media URLs associated with the post"""

    platform_configurations: Optional[PlatformConfigurationsDtoParam]
    """Platform-specific configurations for the post"""


class PreviewSocialAccount(TypedDict, total=False):
    id: Required[str]
    """ID of the social account, ex: spc_12312"""

    platform: Required[str]
    """Platform of the social account"""

    username: str
    """username of the social account"""
