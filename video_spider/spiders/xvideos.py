# -*- coding: utf-8 -*-
import scrapy


class XvideosSpider(scrapy.Spider):
    name = 'xvideos'
    allowed_domains = ['xvideos.com']
    start_urls = ['http://xvideos.com/']

    def parse(self, response):
        pass
