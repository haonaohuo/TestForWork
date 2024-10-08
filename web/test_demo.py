import shelve

import pytest
from selenium.webdriver.common.by import By
from time import sleep
from base import Base


class TestDemo(Base):
    def test_demo(self, get_driver):
        self.driver.get("https://www.baidu.com")
        sleep(2)

    def test_weixin(self, get_driver):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()

    def test_cookies(self, get_driver):
        # get_cookies()可以获取当前打开页面的cookies
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '1688851023127693'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': 'a5841951'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'sameSite': 'Lax',
             'secure': False,
             'value': 'JDm7u2wnD4-kBwgT22QSYyQBqkQKuSJkqXWery1jzEsduFFd5k6E3Br2ph6P_-RTc8hEgaIR0F_H5uVWYgQGaRzA4Oc7JK-hcPsrb1rAeuX4oNS0BROlMVoURLeyfdvQGPNLdsqSnB9JKvDD6p2WlZK9LeOz-edEa7K4-npMvCKZWnOlpKUQYYY7Xl9W0fLKZpNcLu2yfbGTyySyhPM20FK1CBKSI7-jF3kNl35rmoyNaGc4oMBUrr-opN9HzAph5G94cSQAWoHpAyNseB7-5Q'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '3812061814712432'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1759889512, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': 'true'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '1970325064178245'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': 'ue9Nklhw-LgHWbvF8wGSeNgy8m3oLYGCNBmI0fd5-r5NN7qNwGuiQ1-1mVKu8yIP'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '1'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1730945512, 'httpOnly': False, 'name': 'ww_lang', 'path': '/',
             'sameSite': 'Lax', 'secure': False, 'value': 'cn,zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '1688851023127693'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1730945553, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'zh'} ]

        # shelve，python内置模块，专门用来对数据进行持久化储存的库，相当于小型数据库
        # 可以通过key，value来把数据保存到shelve中
        # db = shelve.open("cookies")
        # db['cookie'] = cookies
        # db.close()

        # 提前打开需要加入cookie的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        for cookie in cookies:
            # add_cookie() 加入cookies
            self.driver.add_cookie(cookie)
        # 再次打开，或刷新注入过cookie的页面，就能跳过登录了
        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(3)
