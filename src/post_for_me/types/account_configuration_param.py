# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .twitter_poll_param import TwitterPollParam
from .social_post_media_param import SocialPostMediaParam

__all__ = ["AccountConfigurationParam", "Configuration"]


class Configuration(TypedDict, total=False):
    """Configuration for the social account"""

    localizations: Required[Optional[Dict[str, object]]]
    """Per-language localizations for the video title and description.

    Keys are BCP-47 language tags (e.g. "fr", "es"). Maps to localizations on the
    YouTube Data API videos resource.
    """

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

    category_id: Optional[str]
    """
    YouTube video category id (maps to snippet.categoryId; see YouTube Data API
    videoCategories.list)
    """

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

    default_language: Optional[str]
    """Default language of the video (BCP-47 language tag, e.g.

    "en"). Maps to snippet.defaultLanguage.
    """

    disclose_branded_content: Optional[bool]
    """Disclose branded content on TikTok"""

    disclose_your_brand: Optional[bool]
    """Disclose your brand on TikTok"""

    embeddable: Optional[bool]
    """If true the video can be embedded on other websites (maps to status.embeddable).

    Defaults to true.
    """

    is_ai_generated: Optional[bool]
    """Flag content as AI generated on TikTok"""

    is_draft: Optional[bool]
    """
    Will create a draft upload to TikTok, posting will need to be completed from
    within the app
    """

    license: Optional[Literal["youtube", "creativeCommon"]]
    """The video's license (maps to status.license).

    "youtube" is the standard YouTube license; "creativeCommon" is Creative Commons.
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

    public_stats_viewable: Optional[bool]
    """
    If true, the extended video statistics are publicly viewable (maps to
    status.publicStatsViewable). Defaults to true.
    """

    publish_at: Optional[str]
    """ISO 8601 datetime at which the video should be published.

    Only honoured when privacy_status is "private" (maps to status.publishAt).
    """

    quote_tweet_id: str
    """Id of the tweet you want to quote"""

    recording_date: Optional[str]
    """
    ISO 8601 date (YYYY-MM-DD) or datetime when the video was recorded (maps to
    recordingDetails.recordingDate).
    """

    reply_settings: Optional[Literal["following", "mentionedUsers", "subscribers", "verified"]]
    """Who can reply to the tweet"""

    reshare_post_id: Optional[str]
    """LinkedIn UGC post id to reshare. The caption is used as the reshare commentary."""

    set_caption_for_each_image: Optional[bool]
    """
    If true, include the caption on each image in a Facebook carousel upload; if
    false, only include it on the final carousel post
    """

    share_to_feed: Optional[bool]
    """If false Instagram video posts will only be shown in the Reels tab"""

    tags: Optional[SequenceNotStr[str]]
    """YouTube video tags"""

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
