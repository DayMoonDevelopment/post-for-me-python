# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PlatformPost",
    "Metrics",
    "MetricsTikTokBusinessMetricsDto",
    "MetricsTikTokBusinessMetricsDtoAudienceCity",
    "MetricsTikTokBusinessMetricsDtoAudienceCountry",
    "MetricsTikTokBusinessMetricsDtoAudienceGender",
    "MetricsTikTokBusinessMetricsDtoAudienceType",
    "MetricsTikTokBusinessMetricsDtoEngagementLike",
    "MetricsTikTokBusinessMetricsDtoImpressionSource",
    "MetricsTikTokBusinessMetricsDtoVideoViewRetention",
    "MetricsTikTokPostMetricsDto",
    "MetricsInstagramPostMetricsDto",
    "MetricsYouTubePostMetricsDto",
    "MetricsFacebookPostMetricsDto",
    "MetricsFacebookPostMetricsDtoActivityByActionType",
    "MetricsFacebookPostMetricsDtoActivityByActionTypeUnique",
    "MetricsFacebookPostMetricsDtoVideoRetentionGraphAutoplayed",
    "MetricsFacebookPostMetricsDtoVideoRetentionGraphClickedToPlay",
    "MetricsFacebookPostMetricsDtoVideoViewTimeByAgeGender",
    "MetricsFacebookPostMetricsDtoVideoViewTimeByCountry",
    "MetricsFacebookPostMetricsDtoVideoViewTimeByRegion",
    "MetricsTwitterPostMetricsDto",
    "MetricsTwitterPostMetricsDtoNonPublicMetrics",
    "MetricsTwitterPostMetricsDtoOrganicMetrics",
    "MetricsTwitterPostMetricsDtoPublicMetrics",
    "MetricsThreadsPostMetricsDto",
    "MetricsLinkedInPostMetricsDto",
    "MetricsBlueskyPostMetricsDto",
    "MetricsPinterestPostMetricsDto",
    "MetricsPinterestPostMetricsDto_90d",
    "MetricsPinterestPostMetricsDtoLifetimeMetrics",
    "PlatformData",
]


class MetricsTikTokBusinessMetricsDtoAudienceCity(BaseModel):
    city_name: str
    """City name"""

    percentage: float
    """Percentage of audience from this city"""


class MetricsTikTokBusinessMetricsDtoAudienceCountry(BaseModel):
    country: str
    """Country name"""

    percentage: float
    """Percentage of audience from this country"""


class MetricsTikTokBusinessMetricsDtoAudienceGender(BaseModel):
    gender: str
    """Gender category"""

    percentage: float
    """Percentage of audience of this gender"""


class MetricsTikTokBusinessMetricsDtoAudienceType(BaseModel):
    percentage: float
    """Percentage of audience of this type"""

    type: str
    """Type of audience"""


class MetricsTikTokBusinessMetricsDtoEngagementLike(BaseModel):
    percentage: float
    """Percentage value for the metric"""

    second: str
    """Time in seconds for the metric"""


class MetricsTikTokBusinessMetricsDtoImpressionSource(BaseModel):
    impression_source: str
    """Name of the impression source"""

    percentage: float
    """Percentage of impressions from this source"""


class MetricsTikTokBusinessMetricsDtoVideoViewRetention(BaseModel):
    percentage: float
    """Percentage value for the metric"""

    second: str
    """Time in seconds for the metric"""


class MetricsTikTokBusinessMetricsDto(BaseModel):
    address_clicks: float
    """Number of address clicks"""

    app_download_clicks: float
    """Number of app download clicks"""

    audience_cities: List[MetricsTikTokBusinessMetricsDtoAudienceCity]
    """Audience cities breakdown"""

    audience_countries: List[MetricsTikTokBusinessMetricsDtoAudienceCountry]
    """Audience countries breakdown"""

    audience_genders: List[MetricsTikTokBusinessMetricsDtoAudienceGender]
    """Audience genders breakdown"""

    audience_types: List[MetricsTikTokBusinessMetricsDtoAudienceType]
    """Audience types breakdown"""

    average_time_watched: float
    """Average time watched in seconds"""

    comments: float
    """Number of comments on the post"""

    email_clicks: float
    """Number of email clicks"""

    engagement_likes: List[MetricsTikTokBusinessMetricsDtoEngagementLike]
    """Engagement likes data by percentage and time"""

    favorites: float
    """Number of favorites on the post"""

    full_video_watched_rate: float
    """Rate of full video watches as a percentage"""

    impression_sources: List[MetricsTikTokBusinessMetricsDtoImpressionSource]
    """Impression sources breakdown"""

    lead_submissions: float
    """Number of lead submissions"""

    likes: float
    """Number of likes on the post"""

    new_followers: float
    """Number of new followers gained from the post"""

    phone_number_clicks: float
    """Number of phone number clicks"""

    profile_views: float
    """Number of profile views generated"""

    reach: float
    """Total reach of the post"""

    shares: float
    """Number of shares on the post"""

    total_time_watched: float
    """Total time watched in seconds"""

    video_view_retention: List[MetricsTikTokBusinessMetricsDtoVideoViewRetention]
    """Video view retention data by percentage and time"""

    video_views: float
    """Total number of video views"""

    website_clicks: float
    """Number of website clicks"""


class MetricsTikTokPostMetricsDto(BaseModel):
    comment_count: float
    """Number of comments on the video"""

    like_count: float
    """Number of likes on the video"""

    share_count: float
    """Number of shares of the video"""

    view_count: float
    """Number of views on the video"""


class MetricsInstagramPostMetricsDto(BaseModel):
    comments: Optional[float] = None
    """Number of comments on the post"""

    follows: Optional[float] = None
    """Number of new follows from this post"""

    ig_reels_avg_watch_time: Optional[float] = None
    """Average watch time for Reels (in milliseconds)"""

    ig_reels_video_view_total_time: Optional[float] = None
    """Total watch time for Reels (in milliseconds)"""

    likes: Optional[float] = None
    """Number of likes on the post"""

    navigation: Optional[float] = None
    """Navigation actions taken on the media"""

    profile_activity: Optional[float] = None
    """Profile activity generated from this post"""

    profile_visits: Optional[float] = None
    """Number of profile visits from this post"""

    reach: Optional[float] = None
    """Total number of unique accounts that have seen the media"""

    replies: Optional[float] = None
    """Number of replies to the story (story media only)"""

    saved: Optional[float] = None
    """Total number of unique accounts that have saved the media"""

    shares: Optional[float] = None
    """Total number of shares of the media"""

    total_interactions: Optional[float] = None
    """Total interactions on the post"""

    views: Optional[float] = None
    """Number of views on the post"""


class MetricsYouTubePostMetricsDto(BaseModel):
    comments: float
    """Number of comments on the video"""

    dislikes: float
    """Number of dislikes on the video"""

    likes: float
    """Number of likes on the video"""

    views: float
    """Number of views on the video"""

    annotation_clickable_impressions: Optional[float] = FieldInfo(alias="annotationClickableImpressions", default=None)
    """Number of clickable annotation impressions"""

    annotation_clicks: Optional[float] = FieldInfo(alias="annotationClicks", default=None)
    """Number of annotation clicks"""

    annotation_click_through_rate: Optional[float] = FieldInfo(alias="annotationClickThroughRate", default=None)
    """Annotation click-through rate"""

    annotation_closable_impressions: Optional[float] = FieldInfo(alias="annotationClosableImpressions", default=None)
    """Number of closable annotation impressions"""

    annotation_close_rate: Optional[float] = FieldInfo(alias="annotationCloseRate", default=None)
    """Annotation close rate"""

    annotation_closes: Optional[float] = FieldInfo(alias="annotationCloses", default=None)
    """Number of annotation closes"""

    annotation_impressions: Optional[float] = FieldInfo(alias="annotationImpressions", default=None)
    """Number of annotation impressions"""

    average_view_duration: Optional[float] = FieldInfo(alias="averageViewDuration", default=None)
    """Average view duration in seconds"""

    average_view_percentage: Optional[float] = FieldInfo(alias="averageViewPercentage", default=None)
    """Average percentage of the video watched"""

    card_click_rate: Optional[float] = FieldInfo(alias="cardClickRate", default=None)
    """Card click-through rate"""

    card_clicks: Optional[float] = FieldInfo(alias="cardClicks", default=None)
    """Number of card clicks"""

    card_impressions: Optional[float] = FieldInfo(alias="cardImpressions", default=None)
    """Number of card impressions"""

    card_teaser_click_rate: Optional[float] = FieldInfo(alias="cardTeaserClickRate", default=None)
    """Card teaser click-through rate"""

    card_teaser_clicks: Optional[float] = FieldInfo(alias="cardTeaserClicks", default=None)
    """Number of card teaser clicks"""

    card_teaser_impressions: Optional[float] = FieldInfo(alias="cardTeaserImpressions", default=None)
    """Number of card teaser impressions"""

    engaged_views: Optional[float] = FieldInfo(alias="engagedViews", default=None)
    """Number of engaged views"""

    estimated_minutes_watched: Optional[float] = FieldInfo(alias="estimatedMinutesWatched", default=None)
    """Estimated minutes watched"""

    estimated_red_minutes_watched: Optional[float] = FieldInfo(alias="estimatedRedMinutesWatched", default=None)
    """Estimated minutes watched by YouTube Premium (Red) members"""

    red_views: Optional[float] = FieldInfo(alias="redViews", default=None)
    """Number of views from YouTube Premium (Red) members"""

    shares: Optional[float] = None
    """Number of shares"""

    subscribers_gained: Optional[float] = FieldInfo(alias="subscribersGained", default=None)
    """Subscribers gained"""

    subscribers_lost: Optional[float] = FieldInfo(alias="subscribersLost", default=None)
    """Subscribers lost"""

    videos_added_to_playlists: Optional[float] = FieldInfo(alias="videosAddedToPlaylists", default=None)
    """Number of times the video was added to playlists"""

    videos_removed_from_playlists: Optional[float] = FieldInfo(alias="videosRemovedFromPlaylists", default=None)
    """Number of times the video was removed from playlists"""


class MetricsFacebookPostMetricsDtoActivityByActionType(BaseModel):
    action_type: str
    """Action type (e.g., like, comment, share)"""

    value: float
    """Number of actions"""


class MetricsFacebookPostMetricsDtoActivityByActionTypeUnique(BaseModel):
    action_type: str
    """Action type (e.g., like, comment, share)"""

    value: float
    """Number of actions"""


class MetricsFacebookPostMetricsDtoVideoRetentionGraphAutoplayed(BaseModel):
    rate: float
    """Percentage of viewers at this time"""

    time: float
    """Time in seconds"""


class MetricsFacebookPostMetricsDtoVideoRetentionGraphClickedToPlay(BaseModel):
    rate: float
    """Percentage of viewers at this time"""

    time: float
    """Time in seconds"""


class MetricsFacebookPostMetricsDtoVideoViewTimeByAgeGender(BaseModel):
    key: str
    """Demographic key (e.g., age_gender, region, country)"""

    value: float
    """Total view time in milliseconds"""


class MetricsFacebookPostMetricsDtoVideoViewTimeByCountry(BaseModel):
    key: str
    """Demographic key (e.g., age_gender, region, country)"""

    value: float
    """Total view time in milliseconds"""


class MetricsFacebookPostMetricsDtoVideoViewTimeByRegion(BaseModel):
    key: str
    """Demographic key (e.g., age_gender, region, country)"""

    value: float
    """Total view time in milliseconds"""


class MetricsFacebookPostMetricsDto(BaseModel):
    activity_by_action_type: Optional[List[MetricsFacebookPostMetricsDtoActivityByActionType]] = None
    """Total activity breakdown by action type"""

    activity_by_action_type_unique: Optional[List[MetricsFacebookPostMetricsDtoActivityByActionTypeUnique]] = None
    """Unique users activity breakdown by action type"""

    comments: Optional[float] = None
    """Number of comments (from post object)"""

    fan_reach: Optional[float] = None
    """Number of fans who saw the post"""

    media_views: Optional[float] = None
    """Number of times the photo or video was viewed"""

    nonviral_reach: Optional[float] = None
    """Number of people who saw the post via non-viral distribution"""

    organic_reach: Optional[float] = None
    """Number of people who saw the post via organic distribution"""

    paid_reach: Optional[float] = None
    """Number of people who saw the post via paid distribution"""

    reach: Optional[float] = None
    """Total number of unique people who saw the post"""

    reactions_anger: Optional[float] = None
    """Number of anger reactions"""

    reactions_by_type: Optional[object] = None
    """Breakdown of all reaction types"""

    reactions_haha: Optional[float] = None
    """Number of haha reactions"""

    reactions_like: Optional[float] = None
    """Number of like reactions"""

    reactions_love: Optional[float] = None
    """Number of love reactions"""

    reactions_sorry: Optional[float] = None
    """Number of sad reactions"""

    reactions_total: Optional[float] = None
    """Total number of reactions (all types)"""

    reactions_wow: Optional[float] = None
    """Number of wow reactions"""

    shares: Optional[float] = None
    """Number of shares (from post object)"""

    video_avg_time_watched: Optional[float] = None
    """Average time video was viewed in milliseconds"""

    video_complete_views_organic: Optional[float] = None
    """Number of times video was viewed to 95% organically"""

    video_complete_views_organic_unique: Optional[float] = None
    """Number of unique people who viewed video to 95% organically"""

    video_complete_views_paid: Optional[float] = None
    """Number of times video was viewed to 95% via paid distribution"""

    video_complete_views_paid_unique: Optional[float] = None
    """Number of unique people who viewed video to 95% via paid distribution"""

    video_length: Optional[float] = None
    """Length of the video in milliseconds"""

    video_retention_graph_autoplayed: Optional[List[MetricsFacebookPostMetricsDtoVideoRetentionGraphAutoplayed]] = None
    """Video retention graph for autoplayed views"""

    video_retention_graph_clicked_to_play: Optional[
        List[MetricsFacebookPostMetricsDtoVideoRetentionGraphClickedToPlay]
    ] = None
    """Video retention graph for clicked-to-play views"""

    video_social_actions_unique: Optional[float] = None
    """Number of unique people who performed social actions on the video"""

    video_view_time: Optional[float] = None
    """Total time video was viewed in milliseconds"""

    video_view_time_by_age_gender: Optional[List[MetricsFacebookPostMetricsDtoVideoViewTimeByAgeGender]] = None
    """Video view time breakdown by age and gender"""

    video_view_time_by_country: Optional[List[MetricsFacebookPostMetricsDtoVideoViewTimeByCountry]] = None
    """Video view time breakdown by country"""

    video_view_time_by_distribution_type: Optional[object] = None
    """Video view time breakdown by distribution type"""

    video_view_time_by_region: Optional[List[MetricsFacebookPostMetricsDtoVideoViewTimeByRegion]] = None
    """Video view time breakdown by region"""

    video_view_time_organic: Optional[float] = None
    """Total time video was viewed in milliseconds via organic distribution"""

    video_views: Optional[float] = None
    """Number of times video was viewed for 3+ seconds"""

    video_views_15s: Optional[float] = None
    """Number of times video was viewed for 15+ seconds"""

    video_views_60s: Optional[float] = None
    """
    Number of times video was viewed for 60+ seconds (excludes videos shorter than
    60s)
    """

    video_views_autoplayed: Optional[float] = None
    """Number of times video was autoplayed for 3+ seconds"""

    video_views_by_distribution_type: Optional[object] = None
    """Video views breakdown by distribution type"""

    video_views_clicked_to_play: Optional[float] = None
    """Number of times video was clicked to play for 3+ seconds"""

    video_views_organic: Optional[float] = None
    """Number of times video was viewed for 3+ seconds organically"""

    video_views_organic_unique: Optional[float] = None
    """Number of unique people who viewed the video for 3+ seconds organically"""

    video_views_paid: Optional[float] = None
    """Number of times video was viewed for 3+ seconds via paid distribution"""

    video_views_paid_unique: Optional[float] = None
    """
    Number of unique people who viewed the video for 3+ seconds via paid
    distribution
    """

    video_views_sound_on: Optional[float] = None
    """Number of times video was viewed with sound on"""

    video_views_unique: Optional[float] = None
    """Number of unique people who viewed the video for 3+ seconds"""

    viral_reach: Optional[float] = None
    """Number of people who saw the post in News Feed via viral reach"""


class MetricsTwitterPostMetricsDtoNonPublicMetrics(BaseModel):
    """Non-public metrics for the Tweet (available to the Tweet owner or advertisers)"""

    impression_count: float
    """Number of times this Tweet has been viewed via promoted distribution"""

    url_link_clicks: float
    """Number of clicks on links in this Tweet via promoted distribution"""

    user_profile_clicks: float
    """Number of clicks on the author's profile via promoted distribution"""


class MetricsTwitterPostMetricsDtoOrganicMetrics(BaseModel):
    """Organic metrics for the Tweet (available to the Tweet owner)"""

    impression_count: float
    """Number of times this Tweet has been viewed organically"""

    like_count: float
    """Number of Likes of this Tweet from organic distribution"""

    reply_count: float
    """Number of Replies of this Tweet from organic distribution"""

    retweet_count: float
    """Number of Retweets of this Tweet from organic distribution"""

    url_link_clicks: float
    """Number of clicks on links in this Tweet from organic distribution"""

    user_profile_clicks: float
    """Number of clicks on the author's profile from organic distribution"""


class MetricsTwitterPostMetricsDtoPublicMetrics(BaseModel):
    """Publicly available metrics for the Tweet"""

    bookmark_count: float
    """Number of times this Tweet has been bookmarked"""

    impression_count: float
    """Number of times this Tweet has been viewed"""

    like_count: float
    """Number of Likes of this Tweet"""

    quote_count: float
    """Number of Quotes of this Tweet"""

    reply_count: float
    """Number of Replies of this Tweet"""

    retweet_count: float
    """Number of Retweets of this Tweet"""


class MetricsTwitterPostMetricsDto(BaseModel):
    non_public_metrics: Optional[MetricsTwitterPostMetricsDtoNonPublicMetrics] = None
    """Non-public metrics for the Tweet (available to the Tweet owner or advertisers)"""

    organic_metrics: Optional[MetricsTwitterPostMetricsDtoOrganicMetrics] = None
    """Organic metrics for the Tweet (available to the Tweet owner)"""

    public_metrics: Optional[MetricsTwitterPostMetricsDtoPublicMetrics] = None
    """Publicly available metrics for the Tweet"""


class MetricsThreadsPostMetricsDto(BaseModel):
    likes: float
    """Number of likes on the post"""

    quotes: float
    """Number of quotes of the post"""

    replies: float
    """Number of replies on the post"""

    reposts: float
    """Number of reposts of the post"""

    shares: float
    """Number of shares of the post"""

    views: float
    """Number of views on the post"""


class MetricsLinkedInPostMetricsDto(BaseModel):
    click_count: Optional[float] = FieldInfo(alias="clickCount", default=None)
    """Number of clicks"""

    comment_count: Optional[float] = FieldInfo(alias="commentCount", default=None)
    """Number of comments"""

    engagement: Optional[float] = None
    """Engagement rate"""

    impression_count: Optional[float] = FieldInfo(alias="impressionCount", default=None)
    """Number of impressions"""

    like_count: Optional[float] = FieldInfo(alias="likeCount", default=None)
    """Number of likes"""

    share_count: Optional[float] = FieldInfo(alias="shareCount", default=None)
    """Number of shares"""

    time_watched: Optional[float] = FieldInfo(alias="timeWatched", default=None)
    """TIME_WATCHED: The time the video was watched in milliseconds.

    Video auto-looping will continue to increase this metric for each subsequent
    play
    """

    time_watched_for_video_views: Optional[float] = FieldInfo(alias="timeWatchedForVideoViews", default=None)
    """
    TIME_WATCHED_FOR_VIDEO_VIEWS: The time watched in milliseconds for video
    play-pause cycles that are at least 3 seconds. Video auto-looping will continue
    to increase this metric for each subsequent play. Analytics data for this metric
    will be available for six months
    """

    video_view: Optional[float] = FieldInfo(alias="videoView", default=None)
    """VIDEO_VIEW: Video views with play-pause cycles for at least 3 seconds.

    Auto-looping videos are counted as one when loaded. Each subsequent auto-looped
    play doesn't increase this metric. Analytics data for this metric won't be
    available after six months
    """

    viewer: Optional[float] = None
    """VIEWER: Unique viewers who made engaged plays on the video.

    Auto-looping videos are counted as one when loaded. Each subsequent auto-looped
    play doesn't increase this metric. Analytics data for this metric won't be
    available after six months
    """


class MetricsBlueskyPostMetricsDto(BaseModel):
    like_count: float = FieldInfo(alias="likeCount")
    """Number of likes on the post"""

    quote_count: float = FieldInfo(alias="quoteCount")
    """Number of quotes of the post"""

    reply_count: float = FieldInfo(alias="replyCount")
    """Number of replies on the post"""

    repost_count: float = FieldInfo(alias="repostCount")
    """Number of reposts of the post"""


class MetricsPinterestPostMetricsDto_90d(BaseModel):
    """Last 90 days of Pin metrics"""

    comment: Optional[float] = None
    """Number of comments on the Pin"""

    impression: Optional[float] = None
    """Number of times the Pin was shown (impressions)"""

    last_updated: Optional[str] = None
    """The last time Pinterest updated these metrics"""

    outbound_click: Optional[float] = None
    """Number of clicks from the Pin to an external destination (outbound clicks)"""

    pin_click: Optional[float] = None
    """Number of clicks on the Pin to view it in closeup (Pin clicks)"""

    profile_visit: Optional[object] = None
    """Number of visits to the author's profile driven from the Pin"""

    reaction: Optional[float] = None
    """Total number of reactions on the Pin"""

    save: Optional[float] = None
    """Number of saves of the Pin"""

    user_follow: Optional[object] = None
    """Number of follows driven from the Pin"""

    video_10s_views: Optional[float] = None
    """Number of video views of at least 10 seconds"""

    video_average_time: Optional[float] = None
    """Average watch time for the video"""

    video_p95_views: Optional[float] = None
    """Number of video views that reached 95% completion"""

    video_total_time: Optional[float] = None
    """Total watch time for the video"""

    video_views: Optional[float] = None
    """Number of video views"""


class MetricsPinterestPostMetricsDtoLifetimeMetrics(BaseModel):
    """Lifetime Pin metrics"""

    comment: Optional[float] = None
    """Number of comments on the Pin"""

    impression: Optional[float] = None
    """Number of times the Pin was shown (impressions)"""

    last_updated: Optional[str] = None
    """The last time Pinterest updated these metrics"""

    outbound_click: Optional[float] = None
    """Number of clicks from the Pin to an external destination (outbound clicks)"""

    pin_click: Optional[float] = None
    """Number of clicks on the Pin to view it in closeup (Pin clicks)"""

    profile_visit: Optional[object] = None
    """Number of visits to the author's profile driven from the Pin"""

    reaction: Optional[float] = None
    """Total number of reactions on the Pin"""

    save: Optional[float] = None
    """Number of saves of the Pin"""

    user_follow: Optional[object] = None
    """Number of follows driven from the Pin"""

    video_10s_views: Optional[float] = None
    """Number of video views of at least 10 seconds"""

    video_average_time: Optional[float] = None
    """Average watch time for the video"""

    video_p95_views: Optional[float] = None
    """Number of video views that reached 95% completion"""

    video_total_time: Optional[float] = None
    """Total watch time for the video"""

    video_views: Optional[float] = None
    """Number of video views"""


class MetricsPinterestPostMetricsDto(BaseModel):
    api_90d: Optional[MetricsPinterestPostMetricsDto_90d] = FieldInfo(alias="90d", default=None)
    """Last 90 days of Pin metrics"""

    lifetime_metrics: Optional[MetricsPinterestPostMetricsDtoLifetimeMetrics] = None
    """Lifetime Pin metrics"""


Metrics: TypeAlias = Union[
    MetricsTikTokBusinessMetricsDto,
    MetricsTikTokPostMetricsDto,
    MetricsInstagramPostMetricsDto,
    MetricsYouTubePostMetricsDto,
    MetricsFacebookPostMetricsDto,
    MetricsTwitterPostMetricsDto,
    MetricsThreadsPostMetricsDto,
    MetricsLinkedInPostMetricsDto,
    MetricsBlueskyPostMetricsDto,
    MetricsPinterestPostMetricsDto,
]


class PlatformData(BaseModel):
    """Platform-specific data for the post"""

    title: str
    """Title of the post"""


class PlatformPost(BaseModel):
    caption: str
    """Caption or text content of the post"""

    media: List[List[object]]
    """Array of media items attached to the post"""

    platform: str
    """Social media platform name"""

    platform_account_id: str
    """Platform-specific account ID"""

    platform_post_id: str
    """Platform-specific post ID"""

    platform_url: str
    """URL to the post on the platform"""

    social_account_id: str
    """ID of the social account"""

    external_account_id: Optional[str] = None
    """External account ID from the platform"""

    external_post_id: Optional[str] = None
    """External post ID from the platform"""

    metrics: Optional[Metrics] = None
    """Post metrics and analytics data"""

    platform_data: Optional[PlatformData] = None
    """Platform-specific data for the post"""

    posted_at: Optional[datetime] = None
    """Date the post was published"""

    social_post_id: Optional[str] = None
    """ID of the social post"""

    social_post_result_id: Optional[str] = None
    """ID of the social post result"""
