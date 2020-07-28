# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from MaoyanScrapy.items import MaoyanscrapyItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):

        items = []
        mv_list=Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for i, tags in enumerate(mv_list):
            item = MaoyanscrapyItem()
            mv_name=tags.xpath('./div[1]/span/text()')[0].extract().strip()
            mv_type = tags.xpath('./div[2]/text()')[1].extract().strip()
            mv_time = tags.xpath('./div[4]/text()')[1].extract().strip()
            #print(mv_name, mv_type, mv_time)
            item["mv_name"] = mv_name
            item["mv_type"] = mv_type
            item["mv_time"] = mv_time
            items.append(item)
            if i==9:break
        return items

    def start_requests(self):
        base_usrl = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url=base_usrl, callback=self.parse)
