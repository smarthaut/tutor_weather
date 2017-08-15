#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 13:35
# @Author  : huanghe
# @Site    : 
# @File    : weather_spider.py
# @Software: PyCharm

from scrapy.spider import Spider
from tutor_weather.items import Weather

class WeatherSpider(Spider):
    name = "weather"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://weather.sina.com.cn']

    def parse(self, response):
        item = Weather()
        item['city'] = response.xpath('//li/a[contains(@href,"weather")]/text()').extract()
        item['url'] = response.xpath('//li/a[contains(@href,"weather")]/@href').extract()
        return item
