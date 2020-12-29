import scrapy

class ScrollSpider(scrapy.Spider):
    start_urls = [
        "https://twitter.com/realDonaldTrump/followers"
    ]

    def parse(self, response, **kwargs):
        for profile in response.css('div.quote'):
            yield {
                'text': profile.css('div.css-1dbjc4n r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l::text').getall(),
                'author': profile.css('small.author::text').get(),
                'tags': profile.css('span.css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0::text').getall(),
            }


            #understand exactly whats going on here
            #######################################'

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
