# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PinterestMetricsWindow"]


class PinterestMetricsWindow(BaseModel):
    comment: Optional[float] = None
    """Number of comments on the Pin"""

    impression: Optional[float] = None
    """Number of times the Pin was shown (impressions)"""

    last_updated: Optional[str] = None
    """The last time Pinterest updated these metrics"""

    outbound_click: Optional[float] = None
    """Number of clicks from the Pin to an external destination (outbound clicks)"""

    pin_click: Optional[float] = None
    """Number of clicks on the Pin to view it in closeup (Pin clicks)"""

    profile_visit: Optional[object] = None
    """Number of visits to the author's profile driven from the Pin"""

    reaction: Optional[float] = None
    """Total number of reactions on the Pin"""

    save: Optional[float] = None
    """Number of saves of the Pin"""

    user_follow: Optional[object] = None
    """Number of follows driven from the Pin"""

    video_10s_views: Optional[float] = None
    """Number of video views of at least 10 seconds"""

    video_average_time: Optional[float] = None
    """Average watch time for the video"""

    video_p95_views: Optional[float] = None
    """Number of video views that reached 95% completion"""

    video_total_time: Optional[float] = None
    """Total watch time for the video"""

    video_views: Optional[float] = None
    """Number of video views"""
