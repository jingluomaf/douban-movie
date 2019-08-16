import json
import scrapy
# from parsel import Selector
from ..items import DoubanMovieItem
# from twisted.internet import reactor, defer
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.crawler import CrawlerProcess


class MovieSpider(scrapy.Spider):
    name = "movies"

    # This is a built-in Scrapy function that runs first where we'll override the default headers
    # Documentation: https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider.start_requests
    def start_requests(self):
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0'
        # url = 'https://movie.douban.com/subject/27000904/'
        # allowed_domains = ["example.com"]
        # Set the headers here. The important part is "application/json"
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        #     'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #     # 'Accept-Encoding': 'gzip, deflate, sdch, br, utf-8',
        #     'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4;q=0.9',
        # }

        yield scrapy.http.Request(url)

    def parse(self, response):
        nonCompactJson = json.loads(response.body)
        movies = nonCompactJson.get('subjects')
        for movie in movies:
            item_id = int(movie.get('id'))
            item_title = movie.get('title')
            item_img_url = movie.get('cover')
            item_rate = float(movie.get('rate'))
            item_detail_url = movie.get('url')
            doubanMovieItem = DoubanMovieItem(pk=item_id, title=item_title, img_url=item_img_url,
                                              rate=item_rate, detail_url=item_detail_url,)

            yield doubanMovieItem


# class MovieDetailSpider(scrapy.Spider):
#     name = "details"

#     def get_requests(self):
#         # url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0'
#         # url = 'https://movie.douban.com/subject/27000904/'
#         # allowed_domains = ["example.com"]
#         # Set the headers here. The important part is "application/json"
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
#             'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#             # 'Accept-Encoding': 'gzip, deflate, sdch, br, utf-8',
#             'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4;q=0.9',
#         }
#         for url in detailUrls:
#             yield scrapy.http.Request(url, headers=headers)

#     def parse(self, response):
#         html = response.body
#         yield html


# process = CrawlerProcess()
# process.crawl(MovieSpider)
# process.crawl(MovieDetailSpider)
# process.start()


# configure_logging()
# runner = CrawlerRunner()


# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl(MovieSpider)
#     yield runner.crawl(MovieDetailSpider)
#     reactor.stop()


# crawl()
# reactor.run()


# parsedHtml = BeautifulSoup(response.text, 'lxml')
# print(parsedHtml)
# html = response
# with open('test5.html', 'wb') as f:
#     f.write(html.body)
# javascript = response.xpath(
#     '//script[contains(@type, "ld")]').getall()
# for js in javascript:
#     for js2 in js:
#         print(js2.strip())
# print(javascript)
# xml = lxml.etree.tostring(js2xml.parse(javascript), encoding='unicode')
# print(xml)
# selector = Selector(text=xml)
# print(selector)
# selector.css('var[name="data"]').get()
