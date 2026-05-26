# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .social_post_media_param import SocialPostMediaParam

__all__ = ["YoutubeConfigurationDtoParam"]


class YoutubeConfigurationDtoParam(TypedDict, total=False):
    localizations: Required[Optional[Dict[str, object]]]
    """Per-language localizations for the video title and description.

    Keys are BCP-47 language tags (e.g. "fr", "es"). Maps to localizations on the
    YouTube Data API videos resource.
    """

    caption: Optional[object]
    """Overrides the `caption` from the post"""

    category_id: Optional[str]
    """
    YouTube video category id (maps to snippet.categoryId; see YouTube Data API
    videoCategories.list)
    """

    contains_synthetic_media: Optional[bool]
    """
    If true, marks the video as containing altered or synthetic content per
    YouTube's disclosure policy (maps to status.containsSyntheticMedia). YouTube
    adds a "How this content was made" label to the description automatically.
    """

    default_language: Optional[str]
    """Default language of the video (BCP-47 language tag, e.g.

    "en"). Maps to snippet.defaultLanguage.
    """

    description: Optional[str]
    """Description for the YouTube video (maps to snippet.description).

    Falls back to the post caption when not provided.
    """

    embeddable: Optional[bool]
    """If true the video can be embedded on other websites (maps to status.embeddable).

    Defaults to true.
    """

    license: Optional[Literal["youtube", "creativeCommon"]]
    """The video's license (maps to status.license).

    "youtube" is the standard YouTube license; "creativeCommon" is Creative Commons.
    """

    made_for_kids: Optional[bool]
    """
    If true will notify YouTube the video is intended for kids (maps to
    status.selfDeclaredMadeForKids), defaults to false
    """

    media: Optional[Iterable[SocialPostMediaParam]]
    """Overrides the `media` from the post"""

    privacy_status: Optional[Literal["public", "private", "unlisted"]]
    """
    Sets the privacy status of the video (maps to status.privacyStatus), will
    default to public
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

    recording_date: Optional[str]
    """
    ISO 8601 date (YYYY-MM-DD) or datetime when the video was recorded (maps to
    recordingDetails.recordingDate).
    """

    tags: Optional[SequenceNotStr[str]]
    """YouTube video tags (maps to snippet.tags)"""

    title: Optional[str]
    """Overrides the `title` from the post (maps to snippet.title)"""
