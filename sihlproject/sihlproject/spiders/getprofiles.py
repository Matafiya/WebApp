import json
import scrapy
import os
class QuotesSpider(scrapy.Spider):
    name = "getprofiles"

    def start_requests(self):
        print('current dir is' +os.getcwd())
        with open ("product.json") as f:
            papers = json.load(f)
        urls = []
        for paper in papers:
            urls.append(paper["infolink"])
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for profile in response.css('div.accordion-content ul li'):
            if profile.css('a.accordion-title::text').get() is not None:
                yield {
                    'paper':response.css('title::text').getall(),
                    'printer':profile.css('a.accordion-title::text').get(),
                    'profiles':profile.css('ul.naked-list li a::attr(href)').getall()
                }