# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyRTSItem(scrapy.Item):
    _id = scrapy.Field()
    game_name = scrapy.Field()
    developer = scrapy.Field()
    publisher = scrapy.Field()
    release_date = scrapy.Field()
    rating = scrapy.Field()
    num_reviews = scrapy.Field()
    apprx_downloads = scrapy.Field()
    platform = scrapy.Field() 
    style = scrapy.Field() 
    date_scraped = scrapy.Field()
