# Media

Types:

```python
from post_for_me.types import MediaCreateUploadURLResponse
```

Methods:

- <code title="post /v1/media/create-upload-url">client.media.<a href="./src/post_for_me/resources/media.py">create_upload_url</a>() -> <a href="./src/post_for_me/types/media_create_upload_url_response.py">MediaCreateUploadURLResponse</a></code>

# SocialPosts

Types:

```python
from post_for_me.types import (
    AccountConfiguration,
    BlueskyConfigurationDto,
    CreateSocialPost,
    DeleteEntityResponse,
    FacebookConfigurationDto,
    InstagramConfigurationDto,
    LinkedinConfigurationDto,
    PinterestConfigurationDto,
    PlatformConfigurationsDto,
    SocialPost,
    SocialPostMedia,
    ThreadsConfigurationDto,
    TiktokConfiguration,
    TwitterConfigurationDto,
    TwitterPoll,
    YoutubeConfigurationDto,
    SocialPostListResponse,
)
```

Methods:

- <code title="post /v1/social-posts">client.social_posts.<a href="./src/post_for_me/resources/social_posts.py">create</a>(\*\*<a href="src/post_for_me/types/social_post_create_params.py">params</a>) -> <a href="./src/post_for_me/types/social_post.py">SocialPost</a></code>
- <code title="get /v1/social-posts/{id}">client.social_posts.<a href="./src/post_for_me/resources/social_posts.py">retrieve</a>(id) -> <a href="./src/post_for_me/types/social_post.py">SocialPost</a></code>
- <code title="put /v1/social-posts/{id}">client.social_posts.<a href="./src/post_for_me/resources/social_posts.py">update</a>(id, \*\*<a href="src/post_for_me/types/social_post_update_params.py">params</a>) -> <a href="./src/post_for_me/types/social_post.py">SocialPost</a></code>
- <code title="get /v1/social-posts">client.social_posts.<a href="./src/post_for_me/resources/social_posts.py">list</a>(\*\*<a href="src/post_for_me/types/social_post_list_params.py">params</a>) -> <a href="./src/post_for_me/types/social_post_list_response.py">SocialPostListResponse</a></code>
- <code title="delete /v1/social-posts/{id}">client.social_posts.<a href="./src/post_for_me/resources/social_posts.py">delete</a>(id) -> <a href="./src/post_for_me/types/delete_entity_response.py">DeleteEntityResponse</a></code>

# SocialPostResults

Types:

```python
from post_for_me.types import SocialPostResult, SocialPostResultListResponse
```

Methods:

- <code title="get /v1/social-post-results/{id}">client.social_post_results.<a href="./src/post_for_me/resources/social_post_results.py">retrieve</a>(id) -> <a href="./src/post_for_me/types/social_post_result.py">SocialPostResult</a></code>
- <code title="get /v1/social-post-results">client.social_post_results.<a href="./src/post_for_me/resources/social_post_results.py">list</a>(\*\*<a href="src/post_for_me/types/social_post_result_list_params.py">params</a>) -> <a href="./src/post_for_me/types/social_post_result_list_response.py">SocialPostResultListResponse</a></code>

# SocialAccounts

Types:

```python
from post_for_me.types import (
    SocialAccount,
    SocialAccountMetadata,
    SocialAccountListResponse,
    SocialAccountCreateAuthURLResponse,
    SocialAccountDisconnectResponse,
)
```

Methods:

- <code title="post /v1/social-accounts">client.social_accounts.<a href="./src/post_for_me/resources/social_accounts.py">create</a>(\*\*<a href="src/post_for_me/types/social_account_create_params.py">params</a>) -> <a href="./src/post_for_me/types/social_account.py">SocialAccount</a></code>
- <code title="get /v1/social-accounts/{id}">client.social_accounts.<a href="./src/post_for_me/resources/social_accounts.py">retrieve</a>(id) -> <a href="./src/post_for_me/types/social_account.py">SocialAccount</a></code>
- <code title="patch /v1/social-accounts/{id}">client.social_accounts.<a href="./src/post_for_me/resources/social_accounts.py">update</a>(id, \*\*<a href="src/post_for_me/types/social_account_update_params.py">params</a>) -> <a href="./src/post_for_me/types/social_account.py">SocialAccount</a></code>
- <code title="get /v1/social-accounts">client.social_accounts.<a href="./src/post_for_me/resources/social_accounts.py">list</a>(\*\*<a href="src/post_for_me/types/social_account_list_params.py">params</a>) -> <a href="./src/post_for_me/types/social_account_list_response.py">SocialAccountListResponse</a></code>
- <code title="post /v1/social-accounts/auth-url">client.social_accounts.<a href="./src/post_for_me/resources/social_accounts.py">create_auth_url</a>(\*\*<a href="src/post_for_me/types/social_account_create_auth_url_params.py">params</a>) -> <a href="./src/post_for_me/types/social_account_create_auth_url_response.py">SocialAccountCreateAuthURLResponse</a></code>
- <code title="post /v1/social-accounts/{id}/disconnect">client.social_accounts.<a href="./src/post_for_me/resources/social_accounts.py">disconnect</a>(id) -> <a href="./src/post_for_me/types/social_account_disconnect_response.py">SocialAccountDisconnectResponse</a></code>

# SocialAccountFeeds

Types:

```python
from post_for_me.types import (
    FacebookActivityByActionType,
    FacebookVideoRetentionGraph,
    FacebookVideoViewTimeByDemographic,
    PinterestMetricsWindow,
    PlatformPost,
    TiktokBusinessVideoMetricPercentage,
    YoutubePostPlatformData,
    SocialAccountFeedListResponse,
)
```

Methods:

- <code title="get /v1/social-account-feeds/{social_account_id}">client.social_account_feeds.<a href="./src/post_for_me/resources/social_account_feeds.py">list</a>(social_account_id, \*\*<a href="src/post_for_me/types/social_account_feed_list_params.py">params</a>) -> <a href="./src/post_for_me/types/social_account_feed_list_response.py">SocialAccountFeedListResponse</a></code>

# Webhooks

Types:

```python
from post_for_me.types import Webhook, WebhookListResponse
```

Methods:

- <code title="post /v1/webhooks">client.webhooks.<a href="./src/post_for_me/resources/webhooks.py">create</a>(\*\*<a href="src/post_for_me/types/webhook_create_params.py">params</a>) -> <a href="./src/post_for_me/types/webhook.py">Webhook</a></code>
- <code title="get /v1/webhooks/{id}">client.webhooks.<a href="./src/post_for_me/resources/webhooks.py">retrieve</a>(id) -> <a href="./src/post_for_me/types/webhook.py">Webhook</a></code>
- <code title="patch /v1/webhooks/{id}">client.webhooks.<a href="./src/post_for_me/resources/webhooks.py">update</a>(id, \*\*<a href="src/post_for_me/types/webhook_update_params.py">params</a>) -> <a href="./src/post_for_me/types/webhook.py">Webhook</a></code>
- <code title="get /v1/webhooks">client.webhooks.<a href="./src/post_for_me/resources/webhooks.py">list</a>(\*\*<a href="src/post_for_me/types/webhook_list_params.py">params</a>) -> <a href="./src/post_for_me/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v1/webhooks/{id}">client.webhooks.<a href="./src/post_for_me/resources/webhooks.py">delete</a>(id) -> <a href="./src/post_for_me/types/delete_entity_response.py">DeleteEntityResponse</a></code>

# SocialPostPreviews

Types:

```python
from post_for_me.types import (
    CreateSocialPostPreview,
    SocialPostPreview,
    SocialPostPreviewCreateResponse,
)
```

Methods:

- <code title="post /v1/social-post-previews">client.social_post_previews.<a href="./src/post_for_me/resources/social_post_previews.py">create</a>(\*\*<a href="src/post_for_me/types/social_post_preview_create_params.py">params</a>) -> <a href="./src/post_for_me/types/social_post_preview_create_response.py">SocialPostPreviewCreateResponse</a></code>
