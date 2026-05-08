# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FacebookVideoRetentionGraph"]


class FacebookVideoRetentionGraph(BaseModel):
    rate: float
    """Percentage of viewers at this time"""

    time: float
    """Time in seconds"""
