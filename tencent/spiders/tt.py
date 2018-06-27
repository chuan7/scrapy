# -*- coding: utf-8 -*-
import scrapy
import re
from tencent.items import TencentItem

class TtSpider(scrapy.Spider):
    name = 'tt'
    allowed_domains = ["tencent.com"]

    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = TencentItem()
            item['positionname'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionlink'] = each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            item['peopleNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]
            
            yield item

            if self.offset <300:
                self.offset += 10

            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)

