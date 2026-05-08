# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TiktokBusinessVideoMetricPercentage"]


class TiktokBusinessVideoMetricPercentage(BaseModel):
    percentage: float
    """Percentage value for the metric"""

    second: str
    """Time in seconds for the metric"""
