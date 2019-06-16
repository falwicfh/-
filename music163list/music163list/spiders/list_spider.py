# -*- coding: utf-8 -*-
import scrapy
from music163list.items import Music163ListItem
from scrapy_redis.spiders import RedisSpider

class ListSpiderSpider(RedisSpider):
    # 爬虫名
    name = 'list_spider'
    # 允许域名
    allowed_domains = ['music.163.com']
    # 入口URL（爬取的目标URL）,扔到调度器
    #start_urls = ['https://music.163.com/#/discover/playlist']
    redis_key = 'list_spider:start_urls'
#默认的解析方法
    def parse(self, response):
        #循环首页音乐的条目
        music_list = response.xpath('//ul[@class="m-cvrlst f-cb"]/li')
        for i_item in music_list:
            music_item = Music163ListItem()
            music_item['歌单名'] = i_item.xpath('.//p[@class="dec"]/a/@title').extract()
            music_item['用户名'] = i_item.xpath('.//p[2]/a/@title').extract()
            music_item['点击量'] = i_item.xpath('.//div/div/span[2]/text()').extract()
            #将数据传输到piplines ,进行存储
            yield music_item
        #解析下一页

        next_link = response.xpath('//div[@id="m-pl-pager"]/div/a[11]/@href').extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://music.163.com"+next_link,callback=self.parse)