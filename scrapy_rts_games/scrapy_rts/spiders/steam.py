import scrapy
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from items import ScrapyRTSItem
from datetime import date



class SteamRTSSpider(scrapy.Spider):


    name = "Steam"
    allowed_domains = ["store.steampowered.com"]

    def start_requests(self):
        for page in range(10):
            url = "https://store.steampowered.com/search/?tags=1676&category1=998&supportedlang=english&page=" + str(page + 1)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.css('div#search_resultsRows a::attr(href)').getall():
            yield response.follow(link, callback=self.products_parse)
            
    def products_parse(self, response):
        
        game_name = response.css('div.apphub_AppName::text').get()
        developer = response.css('div#developers_list a::text').get()
        publisher = response.css('div.subtitle.column:contains("Publisher") + div.summary.column a::text').get()
        if response.css('div.date::text').get():
            release_date = response.css('div.date::text').get()
        else:
            release_date = 'No Data'
        if response.css('div.user_reviews_summary_row::attr(data-tooltip-html)'):
            rating = int(re.findall('\d*', response.css('div.user_reviews_summary_row::attr(data-tooltip-html)').get())[0])
        else:
            'No Rating'
        if response.css('span.responsive_hidden::text'):
            num_reviews = int(re.search('[0-9,]+', response.css('span.responsive_hidden::text').extract()[1]).group().replace(',', ''))
            apprx_downloads = int(num_reviews) * 70
        else:
            num_reviews = 'No Reviews'
            apprx_downloads = 'No Data'
        platform = 'PC'
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
            date_scraped = str(date.today().strftime('%d-%m-%Y'))
        )

