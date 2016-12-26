# -*- coding: utf-8 -*-

BOT_NAME = 'douban_movie'

SPIDER_MODULES = ['douban_movie.spiders']
NEWSPIDER_MODULE = 'douban_movie.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = ' Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 默认的头
DEFAULT_REQUEST_HEADERS = {
                           'Referer': 'https://movie.douban.com/'
}

ITEM_PIPELINES = {
   'douban_movie.pipelines.DoubanMoviePipeline': 300,
}
