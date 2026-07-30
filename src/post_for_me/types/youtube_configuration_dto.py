# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .social_post_media import SocialPostMedia

__all__ = ["YoutubeConfigurationDto", "Localizations"]


class Localizations(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None


class YoutubeConfigurationDto(BaseModel):
    localizations: Optional[Dict[str, Localizations]] = None
    """Per-language localizations for the video title and description.

    Keys are BCP-47 language tags (e.g. "fr", "es"). Maps to localizations on the
    YouTube Data API videos resource.
    """

    caption: Optional[object] = None
    """Overrides the `caption` from the post"""

    category_id: Optional[str] = None
    """
    YouTube video category id (maps to snippet.categoryId; see YouTube Data API
    videoCategories.list)
    """

    contains_synthetic_media: Optional[bool] = None
    """
    If true, marks the video as containing altered or synthetic content per
    YouTube's disclosure policy (maps to status.containsSyntheticMedia). YouTube
    adds a "How this content was made" label to the description automatically.
    """

    default_language: Optional[str] = None
    """Default language of the video (BCP-47 language tag, e.g.

    "en"). Maps to snippet.defaultLanguage.
    """

    description: Optional[str] = None
    """Description for the YouTube video (maps to snippet.description).

    Falls back to the post caption when not provided.
    """

    embeddable: Optional[bool] = None
    """If true the video can be embedded on other websites (maps to status.embeddable).

    Defaults to true.
    """

    license: Optional[Literal["youtube", "creativeCommon"]] = None
    """The video's license (maps to status.license).

    "youtube" is the standard YouTube license; "creativeCommon" is Creative Commons.
    """

    made_for_kids: Optional[bool] = None
    """
    If true will notify YouTube the video is intended for kids (maps to
    status.selfDeclaredMadeForKids), defaults to false
    """

    media: Optional[List[SocialPostMedia]] = None
    """Overrides the `media` from the post"""

    privacy_status: Optional[Literal["public", "private", "unlisted"]] = None
    """
    Sets the privacy status of the video (maps to status.privacyStatus), will
    default to public
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

    recording_date: Optional[str] = None
    """
    ISO 8601 date (YYYY-MM-DD) or datetime when the video was recorded (maps to
    recordingDetails.recordingDate).
    """

    tags: Optional[List[str]] = None
    """YouTube video tags (maps to snippet.tags)"""

    title: Optional[str] = None
    """Overrides the `title` from the post (maps to snippet.title)"""
