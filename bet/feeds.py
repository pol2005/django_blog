# coding=utf-8
from django.contrib.syndication.views import Feed
from .models import Article

class LatestEntriesFeed(Feed):
    title = "Betvision.gr "
    link = "/rss/"
    description = "Στοιχηματικά και αθλητικά νέα."

    def items(self):
        return Article.published.order_by('-publish')[:40]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body
