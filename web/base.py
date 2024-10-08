import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class Base():
    @pytest.fixture()
    def get_driver(self):
        # 复用当前打开的浏览器
        # windows在cmd输入后面命令启动浏览器 D:\Test\chrome-win64\chrome.exe --remote-debugging-port=9222
        options = Options()
        options.debugger_address = "127.0.0.1:9222"

        # 手动指定webdriver地址，防止自动下载，启动慢
        service = Service(r"D:\Test\chromedriver-win64\chromedriver_129.0.6668.70_x64.exe")

        # self.driver = webdriver.Chrome(service=service, options=options)
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

        yield

        self.driver.quit()
