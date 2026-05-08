# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from post_for_me import PostForMe, AsyncPostForMe
from tests.utils import assert_matches_type
from post_for_me.types import (
    SocialPostPreviewCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSocialPostPreviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PostForMe) -> None:
        social_post_preview = client.social_post_previews.create(
            caption="caption",
            preview_social_accounts=[
                {
                    "id": "id",
                    "platform": "platform",
                }
            ],
        )
        assert_matches_type(SocialPostPreviewCreateResponse, social_post_preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostForMe) -> None:
        social_post_preview = client.social_post_previews.create(
            caption="caption",
            preview_social_accounts=[
                {
                    "id": "id",
                    "platform": "platform",
                    "username": "username",
                }
            ],
            account_configurations=[
                {
                    "configuration": {
                        "allow_comment": True,
                        "allow_duet": True,
                        "allow_stitch": True,
                        "auto_add_music": True,
                        "board_ids": ["string"],
                        "caption": {},
                        "collaborators": [[{}]],
                        "community_id": "community_id",
                        "disclose_branded_content": True,
                        "disclose_your_brand": True,
                        "is_ai_generated": True,
                        "is_draft": True,
                        "link": "link",
                        "location": "location",
                        "made_for_kids": True,
                        "media": [
                            {
                                "url": "url",
                                "skip_processing": True,
                                "tags": [
                                    {
                                        "id": "id",
                                        "platform": "facebook",
                                        "type": "user",
                                        "x": 0,
                                        "y": 0,
                                    }
                                ],
                                "thumbnail_timestamp_ms": {},
                                "thumbnail_url": {},
                            }
                        ],
                        "placement": "reels",
                        "poll": {
                            "duration_minutes": 0,
                            "options": ["string"],
                            "reply_settings": "following",
                        },
                        "privacy_status": "public",
                        "quote_tweet_id": "quote_tweet_id",
                        "reply_settings": "following",
                        "set_caption_for_each_image": True,
                        "share_to_feed": True,
                        "title": "title",
                        "trial_reel_type": "manual",
                    },
                    "social_account_id": "social_account_id",
                }
            ],
            media=[
                {
                    "url": "url",
                    "skip_processing": True,
                    "tags": [
                        {
                            "id": "id",
                            "platform": "facebook",
                            "type": "user",
                            "x": 0,
                            "y": 0,
                        }
                    ],
                    "thumbnail_timestamp_ms": {},
                    "thumbnail_url": {},
                }
            ],
            platform_configurations={
                "bluesky": {
                    "caption": {},
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                },
                "facebook": {
                    "caption": {},
                    "collaborators": [[{}]],
                    "location": "location",
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "placement": "reels",
                    "set_caption_for_each_image": True,
                },
                "instagram": {
                    "caption": {},
                    "collaborators": ["string"],
                    "location": "location",
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "placement": "reels",
                    "share_to_feed": True,
                    "trial_reel_type": "manual",
                },
                "linkedin": {
                    "caption": {},
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                },
                "pinterest": {
                    "board_ids": ["string"],
                    "caption": {},
                    "link": "link",
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "title": "title",
                },
                "threads": {
                    "caption": {},
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "placement": "reels",
                },
                "tiktok": {
                    "allow_comment": True,
                    "allow_duet": True,
                    "allow_stitch": True,
                    "auto_add_music": True,
                    "caption": {},
                    "disclose_branded_content": True,
                    "disclose_your_brand": True,
                    "is_ai_generated": True,
                    "is_draft": True,
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "privacy_status": "privacy_status",
                    "title": "title",
                },
                "tiktok_business": {
                    "allow_comment": True,
                    "allow_duet": True,
                    "allow_stitch": True,
                    "auto_add_music": True,
                    "caption": {},
                    "disclose_branded_content": True,
                    "disclose_your_brand": True,
                    "is_ai_generated": True,
                    "is_draft": True,
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "privacy_status": "privacy_status",
                    "title": "title",
                },
                "x": {
                    "caption": {},
                    "community_id": "community_id",
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "poll": {
                        "duration_minutes": 0,
                        "options": ["string"],
                        "reply_settings": "following",
                    },
                    "quote_tweet_id": "quote_tweet_id",
                    "reply_settings": "following",
                },
                "youtube": {
                    "caption": {},
                    "made_for_kids": True,
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "privacy_status": "public",
                    "title": "title",
                },
            },
        )
        assert_matches_type(SocialPostPreviewCreateResponse, social_post_preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostForMe) -> None:
        response = client.social_post_previews.with_raw_response.create(
            caption="caption",
            preview_social_accounts=[
                {
                    "id": "id",
                    "platform": "platform",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_post_preview = response.parse()
        assert_matches_type(SocialPostPreviewCreateResponse, social_post_preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostForMe) -> None:
        with client.social_post_previews.with_streaming_response.create(
            caption="caption",
            preview_social_accounts=[
                {
                    "id": "id",
                    "platform": "platform",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_post_preview = response.parse()
            assert_matches_type(SocialPostPreviewCreateResponse, social_post_preview, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSocialPostPreviews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostForMe) -> None:
        social_post_preview = await async_client.social_post_previews.create(
            caption="caption",
            preview_social_accounts=[
                {
                    "id": "id",
                    "platform": "platform",
                }
            ],
        )
        assert_matches_type(SocialPostPreviewCreateResponse, social_post_preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostForMe) -> None:
        social_post_preview = await async_client.social_post_previews.create(
            caption="caption",
            preview_social_accounts=[
                {
                    "id": "id",
                    "platform": "platform",
                    "username": "username",
                }
            ],
            account_configurations=[
                {
                    "configuration": {
                        "allow_comment": True,
                        "allow_duet": True,
                        "allow_stitch": True,
                        "auto_add_music": True,
                        "board_ids": ["string"],
                        "caption": {},
                        "collaborators": [[{}]],
                        "community_id": "community_id",
                        "disclose_branded_content": True,
                        "disclose_your_brand": True,
                        "is_ai_generated": True,
                        "is_draft": True,
                        "link": "link",
                        "location": "location",
                        "made_for_kids": True,
                        "media": [
                            {
                                "url": "url",
                                "skip_processing": True,
                                "tags": [
                                    {
                                        "id": "id",
                                        "platform": "facebook",
                                        "type": "user",
                                        "x": 0,
                                        "y": 0,
                                    }
                                ],
                                "thumbnail_timestamp_ms": {},
                                "thumbnail_url": {},
                            }
                        ],
                        "placement": "reels",
                        "poll": {
                            "duration_minutes": 0,
                            "options": ["string"],
                            "reply_settings": "following",
                        },
                        "privacy_status": "public",
                        "quote_tweet_id": "quote_tweet_id",
                        "reply_settings": "following",
                        "set_caption_for_each_image": True,
                        "share_to_feed": True,
                        "title": "title",
                        "trial_reel_type": "manual",
                    },
                    "social_account_id": "social_account_id",
                }
            ],
            media=[
                {
                    "url": "url",
                    "skip_processing": True,
                    "tags": [
                        {
                            "id": "id",
                            "platform": "facebook",
                            "type": "user",
                            "x": 0,
                            "y": 0,
                        }
                    ],
                    "thumbnail_timestamp_ms": {},
                    "thumbnail_url": {},
                }
            ],
            platform_configurations={
                "bluesky": {
                    "caption": {},
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                },
                "facebook": {
                    "caption": {},
                    "collaborators": [[{}]],
                    "location": "location",
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "placement": "reels",
                    "set_caption_for_each_image": True,
                },
                "instagram": {
                    "caption": {},
                    "collaborators": ["string"],
                    "location": "location",
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "placement": "reels",
                    "share_to_feed": True,
                    "trial_reel_type": "manual",
                },
                "linkedin": {
                    "caption": {},
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                },
                "pinterest": {
                    "board_ids": ["string"],
                    "caption": {},
                    "link": "link",
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "title": "title",
                },
                "threads": {
                    "caption": {},
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "placement": "reels",
                },
                "tiktok": {
                    "allow_comment": True,
                    "allow_duet": True,
                    "allow_stitch": True,
                    "auto_add_music": True,
                    "caption": {},
                    "disclose_branded_content": True,
                    "disclose_your_brand": True,
                    "is_ai_generated": True,
                    "is_draft": True,
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "privacy_status": "privacy_status",
                    "title": "title",
                },
                "tiktok_business": {
                    "allow_comment": True,
                    "allow_duet": True,
                    "allow_stitch": True,
                    "auto_add_music": True,
                    "caption": {},
                    "disclose_branded_content": True,
                    "disclose_your_brand": True,
                    "is_ai_generated": True,
                    "is_draft": True,
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "privacy_status": "privacy_status",
                    "title": "title",
                },
                "x": {
                    "caption": {},
                    "community_id": "community_id",
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "poll": {
                        "duration_minutes": 0,
                        "options": ["string"],
                        "reply_settings": "following",
                    },
                    "quote_tweet_id": "quote_tweet_id",
                    "reply_settings": "following",
                },
                "youtube": {
                    "caption": {},
                    "made_for_kids": True,
                    "media": [
                        {
                            "url": "url",
                            "skip_processing": True,
                            "tags": [
                                {
                                    "id": "id",
                                    "platform": "facebook",
                                    "type": "user",
                                    "x": 0,
                                    "y": 0,
                                }
                            ],
                            "thumbnail_timestamp_ms": {},
                            "thumbnail_url": {},
                        }
                    ],
                    "privacy_status": "public",
                    "title": "title",
                },
            },
        )
        assert_matches_type(SocialPostPreviewCreateResponse, social_post_preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostForMe) -> None:
        response = await async_client.social_post_previews.with_raw_response.create(
            caption="caption",
            preview_social_accounts=[
                {
                    "id": "id",
                    "platform": "platform",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_post_preview = await response.parse()
        assert_matches_type(SocialPostPreviewCreateResponse, social_post_preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostForMe) -> None:
        async with async_client.social_post_previews.with_streaming_response.create(
            caption="caption",
            preview_social_accounts=[
                {
                    "id": "id",
                    "platform": "platform",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_post_preview = await response.parse()
            assert_matches_type(SocialPostPreviewCreateResponse, social_post_preview, path=["response"])

        assert cast(Any, response.is_closed) is True
