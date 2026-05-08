# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .twitter_poll_param import TwitterPollParam
from .social_post_media_param import SocialPostMediaParam

__all__ = ["TwitterConfigurationDtoParam"]


class TwitterConfigurationDtoParam(TypedDict, total=False):
    caption: Optional[object]
    """Overrides the `caption` from the post"""

    community_id: str
    """Id of the community to post to"""

    media: Optional[Iterable[SocialPostMediaParam]]
    """Overrides the `media` from the post"""

    poll: TwitterPollParam
    """Poll options for the tweet"""

    quote_tweet_id: str
    """Id of the tweet you want to quote"""

    reply_settings: Optional[Literal["following", "mentionedUsers", "subscribers", "verified"]]
    """Who can reply to the tweet"""
