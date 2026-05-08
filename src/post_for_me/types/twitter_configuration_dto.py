# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .twitter_poll import TwitterPoll
from .social_post_media import SocialPostMedia

__all__ = ["TwitterConfigurationDto"]


class TwitterConfigurationDto(BaseModel):
    caption: Optional[object] = None
    """Overrides the `caption` from the post"""

    community_id: Optional[str] = None
    """Id of the community to post to"""

    media: Optional[List[SocialPostMedia]] = None
    """Overrides the `media` from the post"""

    poll: Optional[TwitterPoll] = None
    """Poll options for the tweet"""

    quote_tweet_id: Optional[str] = None
    """Id of the tweet you want to quote"""

    reply_settings: Optional[Literal["following", "mentionedUsers", "subscribers", "verified"]] = None
    """Who can reply to the tweet"""
