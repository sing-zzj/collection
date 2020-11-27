# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    标题 = scrapy.Field()
    作者 = scrapy.Field()
    内容 = scrapy.Field()

