# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .twitter_poll import TwitterPoll
from .social_post_media import SocialPostMedia

__all__ = ["AccountConfiguration", "Configuration"]


class Configuration(BaseModel):
    """Configuration for the social account"""

    allow_comment: Optional[bool] = None
    """Allow comments on TikTok"""

    allow_duet: Optional[bool] = None
    """Allow duets on TikTok"""

    allow_stitch: Optional[bool] = None
    """Allow stitch on TikTok"""

    audio_name: Optional[str] = None
    """Display name for the audio track on Instagram Reels.

    Only honored on Reels uploads, and only when the audio is original (Meta
    silently ignores it on licensed/fingerprinted tracks).
    """

    auto_add_music: Optional[bool] = None
    """Will automatically add music to photo posts on TikTok"""

    board_ids: Optional[List[str]] = None
    """Pinterest board IDs"""

    caption: Optional[object] = None
    """Overrides the `caption` from the post"""

    collaborators: Optional[List[List[object]]] = None
    """
    List of page ids or users to invite as collaborators for a Video Reel (Instagram
    and Facebook)
    """

    community_id: Optional[str] = None
    """Id of the twitter community to post to"""

    disclose_branded_content: Optional[bool] = None
    """Disclose branded content on TikTok"""

    disclose_your_brand: Optional[bool] = None
    """Disclose your brand on TikTok"""

    is_ai_generated: Optional[bool] = None
    """Flag content as AI generated on TikTok"""

    is_draft: Optional[bool] = None
    """
    Will create a draft upload to TikTok, posting will need to be completed from
    within the app
    """

    link: Optional[str] = None
    """Pinterest post link"""

    location: Optional[str] = None
    """
    Page id with a location that you want to tag the image or video with (Instagram
    and Facebook)
    """

    made_for_kids: Optional[bool] = None
    """If true will notify YouTube the video is intended for kids, defaults to false"""

    media: Optional[List[SocialPostMedia]] = None
    """Overrides the `media` from the post"""

    placement: Optional[Literal["reels", "timeline", "stories"]] = None
    """Post placement for Facebook/Instagram/Threads"""

    poll: Optional[TwitterPoll] = None
    """Poll options for the twitter"""

    privacy_status: Optional[Literal["public", "private", "unlisted"]] = None
    """
    Sets the privacy status for TikTok (private, public), or YouTube (private,
    public, unlisted)
    """

    quote_tweet_id: Optional[str] = None
    """Id of the tweet you want to quote"""

    reply_settings: Optional[Literal["following", "mentionedUsers", "subscribers", "verified"]] = None
    """Who can reply to the tweet"""

    set_caption_for_each_image: Optional[bool] = None
    """
    If true, include the caption on each image in a Facebook carousel upload; if
    false, only include it on the final carousel post
    """

    share_to_feed: Optional[bool] = None
    """If false Instagram video posts will only be shown in the Reels tab"""

    title: Optional[str] = None
    """Overrides the `title` from the post (Pinterest, TikTok, YouTube)"""

    trial_reel_type: Optional[Literal["manual", "performance"]] = None
    """Instagram trial reel type, when passed will be created as a trial reel.

    If manual the trial reel can be manually graduated in the native app. If
    perfomance the trial reel will be automatically graduated if the trial reel
    performs well.
    """


class AccountConfiguration(BaseModel):
    configuration: Configuration
    """Configuration for the social account"""

    social_account_id: str
    """ID of the social account, you want to apply the configuration to"""
