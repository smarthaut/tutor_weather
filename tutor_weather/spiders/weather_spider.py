#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 13:35
# @Author  : huanghe
# @Site    : 
# @File    : weather_spider.py
# @Software: PyCharm

from scrapy.spider import Spider
from scrapy.http import Request
from tutor_weather.items import Weather

class WeatherSpider(Spider):
    name = "weather"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://weather.sina.com.cn']

    def parse(self, response):
        item = Weather()
        tenDay = response.xpath('//*[@id="blk_fc_c0_scroll"]');
        item['city'] = response.xpath('//h4[contains(@id,"slider_ct_name")]/text()').extract()
        urls = response.xpath('//li/a[contains(@href,"weather")]/@href').extract()
        item['date'] = response.xpath('//p[contains(@class,"wt_fc_c0_i_date")]/text()').extract()
        item['dayDesc'] = tenDay.css('img.icons0_wt::attr(title)').extract()
        item['dayTemp'] = tenDay.css('p.wt_fc_c0_i_temp::text').extract()
        yield item
        for url in urls:
            yield Request(url,callback=self.parse)

