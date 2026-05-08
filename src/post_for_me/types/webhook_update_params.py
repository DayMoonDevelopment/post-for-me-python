# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    event_types: List[
        Literal[
            "social.post.created",
            "social.post.updated",
            "social.post.deleted",
            "social.post.result.created",
            "social.account.created",
            "social.account.updated",
        ]
    ]
    """List of events the webhook will recieve"""

    url: str
    """Public url to recieve event data"""
