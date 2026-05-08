# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    id: str
    """The unique identifier of the webhook"""

    event_types: List[str]
    """Events that will be sent to the webhook"""

    secret: str
    """Secret key used to verify webhook post"""

    url: str
    """The public webhook url"""
