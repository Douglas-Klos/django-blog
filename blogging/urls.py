from django.urls import path
from blogging.views import (
    stub_view,
    list_view,
    detail_view,
    add_post_view,
    unpublished_view,
)
from blogging.feeds import LatestEntriesFeed

urlpatterns = [
    path("", list_view, name="blog_index"),
    path("posts/<int:post_id>/", detail_view, name="blog_detail"),
    path("unpublished/", unpublished_view, name="unpublished_view"),
    path("add/", add_post_view, name="add_post_view"),
    path("rss/", LatestEntriesFeed(), name="rss_view"),
]
