import json
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "getprofiles"

    def start_requests(self):
        with open ("./product.json") as f:
            papers = json.load(f)
        urls = []
        for paper in papers:
            urls.append(paper["infolink"])
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for profile in response.css('ul.naked-list'):
            yield {
                'profiles': profile.css('a::attr(href)').getall()
            }