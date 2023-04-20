import scrapy
from scrapy.exceptions import CloseSpider
from datetime import date
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from items import ScrapyRTSItem


class PS4RTSSpider(scrapy.Spider):

    name = "PS4"
    allowed_domains = ["www.metacritic.com"]
    start_urls = ["https://www.metacritic.com/browse/games/genre/userscore/real-time/ps4?view=condensed"]
    scraped_items = 0
    max_items = 150

    def parse(self, response):
        for link in response.css('td.details a.title::attr(href)').getall():
            yield response.follow(link, callback=self.products_parse)
            
    def products_parse(self, response):
        self.scraped_items += 1
        if self.scraped_items >= self.max_items:
            raise CloseSpider(f'Scraped {self.max_items} items')
        
        game_name = response.css('a.hover_none h1::text').get()
        developer = response.css('li.summary_detail.developer span.data a.button::text').get()
        publisher = [re.search('((?:[A-Z]\w+[ -]?)+)', i).group() for i in response.css('li.summary_detail.publisher span.data a::text').getall()]
        release_date = response.css('li.summary_detail.release_data span.data::text').get()
        rating = int(float(response.css('div.userscore_wrap.feature_userscore a.metascore_anchor div::text').get()) * 10)
        num_reviews = int(re.search('\d+', response.css('div.userscore_wrap.feature_userscore div.summary p span.count a::text').get()).group())
        apprx_downloads = num_reviews * 7000
        platform = 'PS4'
        style = 'Not Specified'

        yield ScrapyRTSItem(
            game_name = game_name,
            developer = developer,
            publisher = publisher,
            release_date = release_date,
            rating = rating,
            num_reviews = num_reviews,
            apprx_downloads = apprx_downloads,
            platform = platform,
            style = style,
            date_scraped = date.today().strftime('%d-%m-%Y')
        )

class XboxRTSSpider(scrapy.Spider):

    name = "Xbox"
    allowed_domains = ["www.metacritic.com"]
    start_urls = ["https://www.metacritic.com/browse/games/genre/userscore/real-time/xboxone?view=condensed"]
    scraped_items = 0
    max_items = 150

    def parse(self, response):
        for link in response.css('td.details a.title::attr(href)').getall():
            yield response.follow(link, callback=self.products_parse)
            
    def products_parse(self, response):
        self.scraped_items += 1
        if self.scraped_items >= self.max_items:
            raise CloseSpider(f'Scraped {self.max_items} items')
        
        game_name = response.css('a.hover_none h1::text').get()
        developer = response.css('li.summary_detail.developer span.data a.button::text').get()
        publisher = [re.search('((?:[A-Z]\w+[ -]?)+)', i).group() for i in response.css('li.summary_detail.publisher span.data a::text').getall()]
        release_date = response.css('li.summary_detail.release_data span.data::text').get()
        rating = int(float(response.css('div.userscore_wrap.feature_userscore a.metascore_anchor div::text').get()) * 10)
        num_reviews = int(re.search('\d+', response.css('div.userscore_wrap.feature_userscore div.summary p span.count a::text').get()).group())
        apprx_downloads = num_reviews * 7000
        platform = 'Xbox One'
        style = 'Not Specified'

        print(game_name)
        print(platform)
        print(rating)
        yield ScrapyRTSItem(
            game_name = game_name,
            developer = developer,
            publisher = publisher,
            release_date = release_date,
            rating = rating,
            num_reviews = num_reviews,
            apprx_downloads = apprx_downloads,
            platform = platform,
            style = style,
            date_scraped = date.today().strftime('%d-%m-%Y')
        )

class SwitchRTSSpider(scrapy.Spider):

    name = "Switch"
    allowed_domains = ["www.metacritic.com"]
    start_urls = ["https://www.metacritic.com/browse/games/genre/userscore/real-time/switch?view=condensed"]
    scraped_items = 0
    max_items = 5

    def parse(self, response):
        for link in response.css('td.details a.title::attr(href)').getall():
            yield response.follow(link, callback=self.products_parse)
            
    def products_parse(self, response):
        self.scraped_items += 1
        if self.scraped_items > self.max_items:
            raise CloseSpider(f'Scraped {self.max_items} items')
        
        game_name = response.css('a.hover_none h1::text').get()
        developer = response.css('li.summary_detail.developer span.data a.button::text').get()
        publisher = [re.search('((?:[A-Z]\w+[ -]?)+)', i).group() for i in response.css('li.summary_detail.publisher span.data a::text').getall()]
        release_date = response.css('li.summary_detail.release_data span.data::text').get()
        rating = int(float(response.css('div.userscore_wrap.feature_userscore a.metascore_anchor div::text').get()) * 10)
        num_reviews = int(re.search('\d+', response.css('div.userscore_wrap.feature_userscore div.summary p span.count a::text').get()).group())
        apprx_downloads = num_reviews * 7000
        platform = 'Switch'
        style = 'Not Specified'

        yield ScrapyRTSItem(
            game_name = game_name,
            developer = developer,
            publisher = publisher,
            release_date = release_date,
            rating = rating,
            num_reviews = num_reviews,
            apprx_downloads = apprx_downloads,
            platform = platform,
            style = style,
            date_scraped = date.today().strftime('%d-%m-%Y')
        )