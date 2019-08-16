# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pk = scrapy.Field()
    title = scrapy.Field()
    rate = scrapy.Field()
    img_url = scrapy.Field()
    detail_url = scrapy.Field()
    image_paths = scrapy.Field()


class DubokuMovieItem(scrapy.Item):
    pk = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
    detail_url = scrapy.Field()
