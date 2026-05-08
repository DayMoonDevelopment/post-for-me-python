# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import social_post_preview_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.social_post_media_param import SocialPostMediaParam
from ..types.account_configuration_param import AccountConfigurationParam
from ..types.platform_configurations_dto_param import PlatformConfigurationsDtoParam
from ..types.social_post_preview_create_response import SocialPostPreviewCreateResponse

__all__ = ["SocialPostPreviewsResource", "AsyncSocialPostPreviewsResource"]


class SocialPostPreviewsResource(SyncAPIResource):
    """
    Social Post Previews allow you to see what a Social Post will create for each account in the post.
    """

    @cached_property
    def with_raw_response(self) -> SocialPostPreviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DayMoonDevelopment/post-for-me-python#accessing-raw-response-data-eg-headers
        """
        return SocialPostPreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SocialPostPreviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DayMoonDevelopment/post-for-me-python#with_streaming_response
        """
        return SocialPostPreviewsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        caption: str,
        preview_social_accounts: Iterable[social_post_preview_create_params.PreviewSocialAccount],
        account_configurations: Optional[Iterable[AccountConfigurationParam]] | Omit = omit,
        media: Optional[Iterable[SocialPostMediaParam]] | Omit = omit,
        platform_configurations: Optional[PlatformConfigurationsDtoParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialPostPreviewCreateResponse:
        """
        Create Post Previews

        Args:
          caption: Caption text for the post

          preview_social_accounts: Array of social accounts. Can preview non connected accounts, just specify a
              random ID

          account_configurations: Account-specific configurations for the post

          media: Array of media URLs associated with the post

          platform_configurations: Platform-specific configurations for the post

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/social-post-previews",
            body=maybe_transform(
                {
                    "caption": caption,
                    "preview_social_accounts": preview_social_accounts,
                    "account_configurations": account_configurations,
                    "media": media,
                    "platform_configurations": platform_configurations,
                },
                social_post_preview_create_params.SocialPostPreviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialPostPreviewCreateResponse,
        )


class AsyncSocialPostPreviewsResource(AsyncAPIResource):
    """
    Social Post Previews allow you to see what a Social Post will create for each account in the post.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSocialPostPreviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DayMoonDevelopment/post-for-me-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSocialPostPreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSocialPostPreviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DayMoonDevelopment/post-for-me-python#with_streaming_response
        """
        return AsyncSocialPostPreviewsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        caption: str,
        preview_social_accounts: Iterable[social_post_preview_create_params.PreviewSocialAccount],
        account_configurations: Optional[Iterable[AccountConfigurationParam]] | Omit = omit,
        media: Optional[Iterable[SocialPostMediaParam]] | Omit = omit,
        platform_configurations: Optional[PlatformConfigurationsDtoParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialPostPreviewCreateResponse:
        """
        Create Post Previews

        Args:
          caption: Caption text for the post

          preview_social_accounts: Array of social accounts. Can preview non connected accounts, just specify a
              random ID

          account_configurations: Account-specific configurations for the post

          media: Array of media URLs associated with the post

          platform_configurations: Platform-specific configurations for the post

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/social-post-previews",
            body=await async_maybe_transform(
                {
                    "caption": caption,
                    "preview_social_accounts": preview_social_accounts,
                    "account_configurations": account_configurations,
                    "media": media,
                    "platform_configurations": platform_configurations,
                },
                social_post_preview_create_params.SocialPostPreviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialPostPreviewCreateResponse,
        )


class SocialPostPreviewsResourceWithRawResponse:
    def __init__(self, social_post_previews: SocialPostPreviewsResource) -> None:
        self._social_post_previews = social_post_previews

        self.create = to_raw_response_wrapper(
            social_post_previews.create,
        )


class AsyncSocialPostPreviewsResourceWithRawResponse:
    def __init__(self, social_post_previews: AsyncSocialPostPreviewsResource) -> None:
        self._social_post_previews = social_post_previews

        self.create = async_to_raw_response_wrapper(
            social_post_previews.create,
        )


class SocialPostPreviewsResourceWithStreamingResponse:
    def __init__(self, social_post_previews: SocialPostPreviewsResource) -> None:
        self._social_post_previews = social_post_previews

        self.create = to_streamed_response_wrapper(
            social_post_previews.create,
        )


class AsyncSocialPostPreviewsResourceWithStreamingResponse:
    def __init__(self, social_post_previews: AsyncSocialPostPreviewsResource) -> None:
        self._social_post_previews = social_post_previews

        self.create = async_to_streamed_response_wrapper(
            social_post_previews.create,
        )
