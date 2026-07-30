# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .social_post_media_param import SocialPostMediaParam

__all__ = ["InstagramConfigurationDtoParam"]


class InstagramConfigurationDtoParam(TypedDict, total=False):
    audio_name: Optional[str]
    """Display name for the audio track on Instagram Reels.

    Only honored on Reels uploads, and only when the audio is original (Meta
    silently ignores it on licensed/fingerprinted tracks).
    """

    caption: Optional[object]
    """Overrides the `caption` from the post"""

    collaborators: Optional[SequenceNotStr[str]]
    """Instagram usernames to be tagged as a collaborator"""

    location: Optional[str]
    """Page id with a location that you want to tag the image or video with"""

    media: Optional[Iterable[SocialPostMediaParam]]
    """Overrides the `media` from the post"""

    placement: Optional[Literal["reels", "stories", "timeline"]]
    """Instagram post placement"""

    share_to_feed: Optional[bool]
    """If false video posts will only be shown in the Reels tab"""

    trial_reel_type: Optional[Literal["manual", "performance"]]
    """Instagram trial reel type, when passed will be created as a trial reel.

    If manual the trial reel can be manually graduated in the native app. If
    perfomance the trial reel will be automatically graduated if the trial reel
    performs well.
    """
