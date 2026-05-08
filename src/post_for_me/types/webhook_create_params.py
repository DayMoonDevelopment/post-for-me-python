# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    event_types: Required[
        List[
            Literal[
                "social.post.created",
                "social.post.updated",
                "social.post.deleted",
                "social.post.result.created",
                "social.account.created",
                "social.account.updated",
            ]
        ]
    ]
    """List of events the webhook will recieve"""

    url: Required[str]
    """Public url to recieve event data"""
