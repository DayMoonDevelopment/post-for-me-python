# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .social_post_media import SocialPostMedia

__all__ = ["InstagramConfigurationDto"]


class InstagramConfigurationDto(BaseModel):
    audio_name: Optional[str] = None
    """Display name for the audio track on Instagram Reels.

    Only honored on Reels uploads, and only when the audio is original (Meta
    silently ignores it on licensed/fingerprinted tracks).
    """

    caption: Optional[object] = None
    """Overrides the `caption` from the post"""

    collaborators: Optional[List[str]] = None
    """Instagram usernames to be tagged as a collaborator"""

    location: Optional[str] = None
    """Page id with a location that you want to tag the image or video with"""

    media: Optional[List[SocialPostMedia]] = None
    """Overrides the `media` from the post"""

    placement: Optional[Literal["reels", "stories", "timeline"]] = None
    """Instagram post placement"""

    share_to_feed: Optional[bool] = None
    """If false video posts will only be shown in the Reels tab"""

    trial_reel_type: Optional[Literal["manual", "performance"]] = None
    """Instagram trial reel type, when passed will be created as a trial reel.

    If manual the trial reel can be manually graduated in the native app. If
    perfomance the trial reel will be automatically graduated if the trial reel
    performs well.
    """
