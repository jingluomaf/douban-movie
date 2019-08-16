import scrapy
import os
import psycopg2


class MovieDetailSpider(scrapy.Spider):
    name = "details"

    def start_requests(self):

        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        #     'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #     # 'Accept-Encoding': 'gzip, deflate, sdch, br, utf-8',
        #     'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4;q=0.9',
        # }
        hostname = 'localhost'

        username = os.environ.get('SQL_USER')
        password = os.environ.get('SQL_PASS')
        database = 'movies'
        conn = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database)
        cursor = conn.cursor()
        cursor.execute('SELECT detail_url FROM douban_movie')

        tuple_detailUrls = cursor.fetchall()
        for tuple_url in tuple_detailUrls:
            string_url = ''.join(tuple_url)
            url = string_url.replace(' ', '')
            yield scrapy.http.Request(url)

    def parse(self, response):
        info = response.xpath(
            '//div[@id="info"]')
        # for details in info:
        # actor_details = info.css("span.attrs")
        # actor_names = actor_details.css("a::text").getall()
        # actor_links = info.css("a::attr('href')").getall()
        genre = info.xpath("//span[@property='v:genre']/text()").getall()
        time = info.xpath(
            "//span[@property='v:initialReleaseDate']/text()").getall()
        info_text = info.xpath("//span/text()").getall()
        summary = response.xpath(
            '//div[@id="link-report"]//span/text()')
        # alt_name = info.xpath("/text()").getall()
        # location = info.xpath"/text()".getall()
        print(summary)
        # print(genre)
        # print(time)
        # actor = info.xpath

        # html = response.body
        # yield html
