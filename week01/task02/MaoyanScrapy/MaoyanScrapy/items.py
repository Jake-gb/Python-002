# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mv_name=scrapy.Field()
    mv_type=scrapy.Field()
    mv_time=scrapy.Field()
