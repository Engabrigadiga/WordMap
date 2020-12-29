import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wikispider'
    start_urls=[
        'https://en.wikipedia.org/wiki/Donald_Trump',
        'https://en.wikipedia.org/wiki/Videogamedunkey',
    ]

    def parse(self, response):
        for tag_p in response.css('div.bodyContent'):
            print('pass')