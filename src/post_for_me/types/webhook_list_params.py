# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """Filter by id(s).

    Multiple values imply OR logic (e.g., ?id=wbh_xxxxxx&id=wbh_yyyyyy).
    """

    event_type: SequenceNotStr[str]
    """Filter by event type(s).

    Multiple values imply OR logic (e.g.,
    ?event_type=social.post.created&event_type=social.post.updated).
    """

    limit: float
    """Number of items to return"""

    offset: float
    """Number of items to skip"""

    url: SequenceNotStr[str]
    """Filter by url(s).

    Multiple values imply OR logic (e.g.,
    ?url=https://example.com&url=https://postforme.dev).
    """
