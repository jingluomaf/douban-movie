# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import psycopg2
import os


class PostgrePipeline(object):

    collection_name = 'scrapy_items'

    def open_spider(self, spider):

        hostname = 'localhost'
        # the username when you create the database
        username = os.environ.get('SQL_USER')
        password = os.environ.get('SQL_PASS')  # change to your password
        database = 'movies'
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute('insert into duboku_movie(id,title,img_url,detail_url) values(%s,%s,%s,%s)',
                         (item['pk'], item['title'], item['img_url'], item['detail_url']))
        self.connection.commit()

# class MovieImagesPipeline(ImagesPipeline):

#     def file_path(self, request, response=None, info=None):
#         return request.meta.get('filename', '')

#     def get_media_requests(self, item, info):
#         img_url = item['img_url']
#         meta_data = {'filename': str(item['pk'])+'.webp'}
#         # for image_url in item['img_url']:
#         yield scrapy.Request(url=img_url, meta=meta_data)

#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image_paths'] = image_paths
#         return item
