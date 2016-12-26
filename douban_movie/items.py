# -*- coding: utf-8 -*-
import scrapy
class DoubanMovieItem(scrapy.Item):
    no = scrapy.Field()
    movie_name = scrapy.Field()
    director = scrapy.Field()
    writer = scrapy.Field()
    actor = scrapy.Field()
    type = scrapy.Field()
    region = scrapy.Field()
    language = scrapy.Field()
    date = scrapy.Field()
    length = scrapy.Field()
    another_name = scrapy.Field()
    introduction = scrapy.Field()
    grade = scrapy.Field()
    comment_times = scrapy.Field()