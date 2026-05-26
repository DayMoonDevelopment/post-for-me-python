# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .twitter_poll_param import TwitterPollParam
from .social_post_media_param import SocialPostMediaParam

__all__ = ["AccountConfigurationParam", "Configuration"]


class Configuration(TypedDict, total=False):
    """Configuration for the social account"""

    allow_comment: Optional[bool]
    """Allow comments on TikTok"""

    allow_duet: Optional[bool]
    """Allow duets on TikTok"""

    allow_stitch: Optional[bool]
    """Allow stitch on TikTok"""

    audio_name: Optional[str]
    """Display name for the audio track on Instagram Reels.

    Only honored on Reels uploads, and only when the audio is original (Meta
    silently ignores it on licensed/fingerprinted tracks).
    """

    auto_add_music: Optional[bool]
    """Will automatically add music to photo posts on TikTok"""

    board_ids: Optional[SequenceNotStr[str]]
    """Pinterest board IDs"""

    caption: Optional[object]
    """Overrides the `caption` from the post"""

    collaborators: Optional[Iterable[Iterable[object]]]
    """
    List of page ids or users to invite as collaborators for a Video Reel (Instagram
    and Facebook)
    """

    community_id: str
    """Id of the twitter community to post to"""

    contains_synthetic_media: Optional[bool]
    """
    If true, marks the YouTube video as containing altered or synthetic content per
    YouTube's disclosure policy. Sets status.containsSyntheticMedia on the
    videos.insert call; YouTube adds a "How this content was made" label to the
    description automatically.
    """

    disclose_branded_content: Optional[bool]
    """Disclose branded content on TikTok"""

    disclose_your_brand: Optional[bool]
    """Disclose your brand on TikTok"""

    is_ai_generated: Optional[bool]
    """Flag content as AI generated on TikTok"""

    is_draft: Optional[bool]
    """
    Will create a draft upload to TikTok, posting will need to be completed from
    within the app
    """

    link: Optional[str]
    """Pinterest post link"""

    location: Optional[str]
    """
    Page id with a location that you want to tag the image or video with (Instagram
    and Facebook)
    """

    made_for_kids: Optional[bool]
    """If true will notify YouTube the video is intended for kids, defaults to false"""

    media: Optional[Iterable[SocialPostMediaParam]]
    """Overrides the `media` from the post"""

    placement: Optional[Literal["reels", "timeline", "stories"]]
    """Post placement for Facebook/Instagram/Threads"""

    poll: TwitterPollParam
    """Poll options for the twitter"""

    privacy_status: Optional[Literal["public", "private", "unlisted"]]
    """
    Sets the privacy status for TikTok (private, public), or YouTube (private,
    public, unlisted)
    """

    quote_tweet_id: str
    """Id of the tweet you want to quote"""

    reply_settings: Optional[Literal["following", "mentionedUsers", "subscribers", "verified"]]
    """Who can reply to the tweet"""

    set_caption_for_each_image: Optional[bool]
    """
    If true, include the caption on each image in a Facebook carousel upload; if
    false, only include it on the final carousel post
    """

    share_to_feed: Optional[bool]
    """If false Instagram video posts will only be shown in the Reels tab"""

    title: Optional[str]
    """Overrides the `title` from the post (Pinterest, TikTok, YouTube)"""

    trial_reel_type: Optional[Literal["manual", "performance"]]
    """Instagram trial reel type, when passed will be created as a trial reel.

    If manual the trial reel can be manually graduated in the native app. If
    perfomance the trial reel will be automatically graduated if the trial reel
    performs well.
    """


class AccountConfigurationParam(TypedDict, total=False):
    configuration: Required[Configuration]
    """Configuration for the social account"""

    social_account_id: Required[str]
    """ID of the social account, you want to apply the configuration to"""
