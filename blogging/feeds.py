from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestEntriesFeed(Feed):
    title = "Glorious Blog Feed"
    link = "/rss/"
    description = "RSS Feed of My Glorious Blog"

    def items(self):
        # return Post.objects.all().order_by("-published_date")
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text.replace("\n", "<br>")

    # # This is used if not using get_absolute_url() in models.py
    # def item_link(self, item):
    #     return reverse("blog_detail", args=[item.id])
