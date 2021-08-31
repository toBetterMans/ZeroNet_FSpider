# -*- coding: utf-8 -*-
import time
from lxml import etree
from logging import getLogger
from selenium import webdriver

class ZeroNet_Ajax_Middleware(object):

    def __init__(self):
        self.logger = getLogger(__name__)
        self.chromeOptions = self.get_chrome()
        self.browser = self.get_browser()

    def get_chrome(self):
        chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('window-size=1280,800')
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_experimental_option('w3c', False)
        return chromeOptions

    def get_browser(self):
        browser = webdriver.Chrome(chrome_options=self.chromeOptions)
        #browser.set_window_size(1280,800)
        return browser

    def process_request(self):
            self.logger.info('Chromedrive is Starting')
            self.browser.get('http://47.56.197.215:43110/13RhXecmBH34X44Nohf2qMogZKH7KzoG78')
            self.browser.switch_to_frame(self.browser.find_element_by_id('inner-iframe'))
            time.sleep(3)
            html = self.browser.page_source
            print(html)

if __name__ == '__main__':
    lz = ZeroNet_Ajax_Middleware()
    lz.process_request()