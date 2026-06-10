# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .twitter_poll import TwitterPoll
from .social_post_media import SocialPostMedia

__all__ = ["AccountConfiguration", "Configuration"]


class Configuration(BaseModel):
    """Configuration for the social account"""

    localizations: Optional[Dict[str, object]] = None
    """Per-language localizations for the video title and description.

    Keys are BCP-47 language tags (e.g. "fr", "es"). Maps to localizations on the
    YouTube Data API videos resource.
    """

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

    category_id: Optional[str] = None
    """
    YouTube video category id (maps to snippet.categoryId; see YouTube Data API
    videoCategories.list)
    """

    collaborators: Optional[List[List[object]]] = None
    """
    List of page ids or users to invite as collaborators for a Video Reel (Instagram
    and Facebook)
    """

    community_id: Optional[str] = None
    """Id of the twitter community to post to"""

    contains_synthetic_media: Optional[bool] = None
    """
    If true, marks the YouTube video as containing altered or synthetic content per
    YouTube's disclosure policy. Sets status.containsSyntheticMedia on the
    videos.insert call; YouTube adds a "How this content was made" label to the
    description automatically.
    """

    default_language: Optional[str] = None
    """Default language of the video (BCP-47 language tag, e.g.

    "en"). Maps to snippet.defaultLanguage.
    """

    disclose_branded_content: Optional[bool] = None
    """Disclose branded content on TikTok"""

    disclose_your_brand: Optional[bool] = None
    """Disclose your brand on TikTok"""

    embeddable: Optional[bool] = None
    """If true the video can be embedded on other websites (maps to status.embeddable).

    Defaults to true.
    """

    is_ai_generated: Optional[bool] = None
    """Flag content as AI generated on TikTok"""

    is_draft: Optional[bool] = None
    """
    Will create a draft upload to TikTok, posting will need to be completed from
    within the app
    """

    license: Optional[Literal["youtube", "creativeCommon"]] = None
    """The video's license (maps to status.license).

    "youtube" is the standard YouTube license; "creativeCommon" is Creative Commons.
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

    public_stats_viewable: Optional[bool] = None
    """
    If true, the extended video statistics are publicly viewable (maps to
    status.publicStatsViewable). Defaults to true.
    """

    publish_at: Optional[str] = None
    """ISO 8601 datetime at which the video should be published.

    Only honoured when privacy_status is "private" (maps to status.publishAt).
    """

    quote_tweet_id: Optional[str] = None
    """Id of the tweet you want to quote"""

    recording_date: Optional[str] = None
    """
    ISO 8601 date (YYYY-MM-DD) or datetime when the video was recorded (maps to
    recordingDetails.recordingDate).
    """

    reply_settings: Optional[Literal["following", "mentionedUsers", "subscribers", "verified"]] = None
    """Who can reply to the tweet"""

    reshare_post_id: Optional[str] = None
    """LinkedIn UGC post id to reshare. The caption is used as the reshare commentary."""

    set_caption_for_each_image: Optional[bool] = None
    """
    If true, include the caption on each image in a Facebook carousel upload; if
    false, only include it on the final carousel post
    """

    share_to_feed: Optional[bool] = None
    """If false Instagram video posts will only be shown in the Reels tab"""

    tags: Optional[List[str]] = None
    """YouTube video tags"""

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
