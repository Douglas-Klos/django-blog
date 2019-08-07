from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestEntriesFeed(Feed):
    title = "My Blog Feed"
    link = "/rss/"
    description = "RSS Feed of my glorious blog"

    def items(self):
        return Post.objects.all().order_by('-published_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blog_detail', args=[item.id])
