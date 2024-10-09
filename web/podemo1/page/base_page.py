# 基类：最基本的方法，driver实例化，find()等
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # driver: WebDriver
    base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 第一次初始化
            options = Options()
            options.debugger_address = "127.0.0.1:9222"

            service = Service(r"D:\Test\chromedriver-win64\chromedriver_129.0.6668.70_x64.exe")

            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self.base_url != '':
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        return element




