import scrapy
from scrapy.exceptions import CloseSpider
from google_play_scraper import app as gpapp
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from items import ScrapyRTSItem
from datetime import date


class MobileRTSSpider(scrapy.Spider):

    name = "Android"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps/category/GAME_STRATEGY?hl=en&gl=US"]
    scraped_items = 0
    max_items = 150

    def parse(self, response):
        for link in response.css('div[role="listitem"] a::attr(href)').getall():
            yield response.follow(link, callback=self.products_parse)
        

    def products_parse(self, response):

        self.scraped_items += 1
        if self.scraped_items > self.max_items:
            raise CloseSpider(f'Scraped {self.max_items} items')
        
        url = str(response)
        id_index = url.find("id=") + 3
        app_id = url[id_index:-1]

        game_data = gpapp(
        app_id,
        lang='en', 
        country='us' 
        )

        stylization = response.css('div.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-INsAgc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.Rj2Mlf.OLiIxf.PDpWxe.P62QJc.LQeN7.LMoCf span::text').getall()
        
        game_name = game_data['title']
        developer = game_data['developer']
        publisher = game_data['developer']
        release_date = game_data['released']
        rating = int(game_data['score'] * 20)
        num_reviews = game_data['reviews']
        apprx_downloads = game_data['realInstalls']
        platform = 'Android'
        if 'Stylized-realistic' in stylization:
            style = 'Stylized-realistic'
        elif 'Realistic' in stylization:
            style = 'Realistic'
        else:
            style = 'Stylized'

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