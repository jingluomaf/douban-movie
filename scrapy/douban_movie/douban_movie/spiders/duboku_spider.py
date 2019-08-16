import scrapy
import os
import psycopg2
from ..items import DubokuMovieItem


class DubokuSpider(scrapy.Spider):
    name = "duboku"

    def start_requests(self):
        base_url = 'https://www.duboku.net/vodtype/1-'
        track = 1
        # for i in range(1, 9):
        #     track += i
        url = base_url + str(track)
        yield scrapy.http.Request(url)

    def parse(self, response):
        movies = response.css('div.stui-vodlist__box')
        # filters = response.css("ul.stui-screen__list")
        for movie in movies:
            item_title = movie.css('a::attr(title)').get()
            item_img_url = 'https://www.duboku.net' + \
                movie.css('a::attr(data-original)').get()
            item_detail_url = 'https://www.duboku.net' + \
                movie.css('a::attr(href)').get()

            dubokuMovieItem = DubokuMovieItem(pk=item_detail_url, title=item_title, img_url=item_img_url, detail_url = item_detail_url,
                                              )
            # genres = filters[0].css("a::text").getall()
            # locations = filters[1].css("a::text").getall()
            # times = filters[2].css("a::text").getall()
            # yield dubokuMovieItem
            yield dubokuMovieItem
