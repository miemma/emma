#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import sitemaps
from django.core.urlresolvers import reverse_lazy


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'landing:home', 'landing:services', 'landing:faq', 'landing:about', 'landing:who'

        ]

    def location(self, item):
        return reverse_lazy(item)