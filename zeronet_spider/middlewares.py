# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
import random
import scrapy
from scrapy import Request
from scrapy import signals
from logging import getLogger
from selenium import webdriver
from fake_useragent import UserAgent
from scrapy.utils.project import get_project_settings
from selenium.common.exceptions import TimeoutException


class HttpProxyDownloadMiddleware(object):
    def process_request(self, request, spider):
        settings = get_project_settings()
        request.meta['proxy'] = random.choice(settings.get('HTTP_PROXY'))
        # print(random.choice(settings.get('HTTP_PROXY')))

class RandomUserAgentMiddleware(object):
    def __init__(self):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        settings = get_project_settings()
        self.ua_type = settings.get('USER_AGENT_TYPE')

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)
        request.headers.setdefault('User-Agent', get_ua())
        pass


class StickyDepthSpiderMiddleware:
    def process_spider_output(self, response, result, spider):
        key_found = response.meta.get('depth', None)
        for x in result:
            if isinstance(x, Request) and key_found is not None:
                x.meta.setdefault('depth', key_found)
            yield x


class ZeroNet_Ajax_Middleware(object):

    def __init__(self):
        self.logger = getLogger(__name__)
        self.chromeOptions = self.get_chrome()
        self.browser = self.get_browser()

    def get_chrome(self):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('window-size=1280,800')
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_experimental_option('w3c', False)
        return chromeOptions

    def get_browser(self):
        browser = webdriver.Chrome(chrome_options=self.chromeOptions)
        browser.set_page_load_timeout(10)   # 页面加载超时时间
        browser.set_script_timeout(10)  # 页面js加载超时时间
        return browser

    def process_request(self, request, spider):
        try:
            if  "43110" in request.url:
                self.logger.info('Chromedrive is Starting')
                self.browser.get(request.url)
                try:
                    self.browser.switch_to_frame(self.browser.find_element_by_id('inner-iframe'))
                    time.sleep(3)
                    html = self.browser.page_source
                    # self.browser.quit()
                    return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8', request=request, status=200)
                except:
                    pass
        except TimeoutException:
            return scrapy.http.HtmlResponse(url=request.url, status=500, request=request)



class ZeroNetSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZeroNetDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
