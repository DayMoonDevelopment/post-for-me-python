# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FacebookVideoViewTimeByDemographic"]


class FacebookVideoViewTimeByDemographic(BaseModel):
    key: str
    """Demographic key (e.g., age_gender, region, country)"""

    value: float
    """Total view time in milliseconds"""
