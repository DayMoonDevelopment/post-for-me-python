# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .social_post_media_param import SocialPostMediaParam
from .account_configuration_param import AccountConfigurationParam
from .platform_configurations_dto_param import PlatformConfigurationsDtoParam

__all__ = ["SocialPostCreateParams"]


class SocialPostCreateParams(TypedDict, total=False):
    caption: Required[str]
    """Caption text for the post"""

    social_accounts: Required[SequenceNotStr[str]]
    """Array of social account IDs for posting"""

    account_configurations: Optional[Iterable[AccountConfigurationParam]]
    """Account-specific configurations for the post"""

    external_id: Optional[str]
    """Array of social account IDs for posting"""

    is_draft: Annotated[Optional[bool], PropertyInfo(alias="isDraft")]
    """If isDraft is set then the post will not be processed"""

    media: Optional[Iterable[SocialPostMediaParam]]
    """Array of media associated with the post.

    If multiple media items are provided and the placement is `stories`, individual
    posts are created per media item.
    """

    platform_configurations: Optional[PlatformConfigurationsDtoParam]
    """Platform-specific configurations for the post"""

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Scheduled date and time for the post, setting to null or undefined will post
    instantly
    """
