# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小区地段
    community=scrapy.Field()
    #房源编号
    id=scrapy.Field()
    #户型
    door=scrapy.Field()
    #装修
    decorate=scrapy.Field()
    #面积
    area=scrapy.Field()
    #楼层
    floor=scrapy.Field()
    #总楼层
    floort=scrapy.Field()
    #契证
    deed=scrapy.Field()
    #小学
    pschool=scrapy.Field()
    #中学
    lschool=scrapy.Field()
    #土地性质
    nature=scrapy.Field()
    #单价
    unitprice=scrapy.Field()
    #总价
    totalprice=scrapy.Field()
    #证件
    certificate=scrapy.Field()
    #手机号
    phone=scrapy.Field()
    #更新日期
    date=scrapy.Field()
    pass
