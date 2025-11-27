# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "SocialAccountCreateAuthURLParams",
    "PlatformData",
    "PlatformDataBluesky",
    "PlatformDataInstagram",
    "PlatformDataLinkedin",
]


class SocialAccountCreateAuthURLParams(TypedDict, total=False):
    platform: Required[str]
    """The social account provider"""

    external_id: str
    """Your unique identifier for the social account"""

    platform_data: PlatformData
    """Additional data needed for the provider"""

    redirect_url_override: str
    """Override the default redirect URL for the OAuth flow.

    If provided, this URL will be used instead of our redirect URL. Make sure this
    URL is included in your app's authorized redirect urls. This override will not
    work when using our system credientals.
    """


class PlatformDataBluesky(TypedDict, total=False):
    app_password: Required[str]
    """The app password of the account"""

    handle: Required[str]
    """The handle of the account"""


class PlatformDataInstagram(TypedDict, total=False):
    connection_type: Required[Literal["instagram", "facebook"]]
    """
    The type of connection; instagram for using login with instagram, facebook for
    using login with facebook.
    """


class PlatformDataLinkedin(TypedDict, total=False):
    connection_type: Required[Literal["personal", "organization"]]
    """
    The type of connection; If using our provided credentials always use
    "organization". If using your own crednetials then only use "organization" if
    you are using the Community API
    """


class PlatformData(TypedDict, total=False):
    bluesky: PlatformDataBluesky
    """Additional data needed for connecting bluesky accounts"""

    instagram: PlatformDataInstagram
    """Additional data for connecting instagram accounts"""

    linkedin: PlatformDataLinkedin
    """Additional data for connecting linkedin accounts"""
