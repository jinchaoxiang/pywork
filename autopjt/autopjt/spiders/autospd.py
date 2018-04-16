# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['ruifc.cn']
    start_urls = ['http://www.ruifc.cn/sale/page1.html']

    def parse(self, response):
        url = "http://www.ruifc.cn"
        child_urls = response.xpath("//li[@class='lirq0']//a//@href").extract()
        for i in range(1, 3):
            for child_url in child_urls:
                yield scrapy.Request(url + child_url, callback=self.parse_item)
            start_url = "http://www.ruifc.cn/sale/page" + str(i) + ".html"
            print(start_url)
            yield Request(start_url, callback=self.parse)
        pass

    def parse_item(self, response):
        item = AutopjtItem()
        communitystr = response.xpath("//ul[5]//li[4]/text()").extract()
        item["community"] = communitystr[0].strip()
        idstr = response.xpath("//input[@name='YWZ']/@value").extract()
        item["id"] = idstr[0][5:idstr[0].index(".")]
        doorstr = response.xpath("//ul[6]//li[4]/text()").extract()
        item["door"] = doorstr[0].strip()
        decoratestr = response.xpath("//ul[7]//li[4]/text()").extract()
        item["decorate"] = decoratestr[0].strip()
        areastr = response.xpath("//ul[8]//li[4]//font/text()").extract()
        item["area"] = areastr[0].strip()
        floorstr = response.xpath("//ul[7]//li[2]/text()").extract()
        item["floor"] = floorstr[0].strip()
        floortstr = response.xpath("//ul[8]//li[2]/text()").extract()
        item["floort"] = floortstr[0].strip()
        deedstr = response.xpath("//ul[9]//li[4]/text()").extract()
        item["deed"] = deedstr[0].strip()
        pschoolstr = response.xpath("//ul[10]//li[2]/text()").extract()
        item["pschool"] = pschoolstr[0].strip()
        lschoolstr = response.xpath("//ul[10]//li[4]/text()").extract()
        item["lschool"] = lschoolstr[0].strip()
        naturestr = response.xpath("//ul[11]//li[4]/text()").extract()
        item["nature"] = naturestr[0].strip()
        unitpricestr = response.xpath("//ul[12]//li[4]/text()").extract()
        item["unitprice"] = unitpricestr[0].strip()
        totalpricestr = response.xpath("//ul[13]//li[4]//font/text()").extract()
        item["totalprice"] = totalpricestr[0].strip()
        certificatestr = response.xpath("//ul[13]//li[2]/text()").extract()
        item["certificate"] = certificatestr[0].strip()
        phonestr = response.xpath("//ul[3]//li[4]//b/text()").extract()
        item["phone"] = phonestr[0].strip()
        datestr = response.xpath("//ul[2]//li[2]//text()").extract()
        item["date"] = datestr[0].strip()
        yield item
        pass
