from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from login_page import LoginPage
from register_page import RegisterPage


class IndexPage:
    def __init__(self):
        service = Service(r"D:\Test\chromedriver-win64\chromedriver_129.0.6668.70_x64.exe")

        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)

        self.driver.get('https://work.weixin.qq.com/')

    # 进入登录页面
    def goto_login(self):
        # 点击登录按钮
        self.driver.find_element(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return LoginPage(self.driver)

    # 进入注册页面
    def goto_register(self):
        # 点击注册按钮
        self.driver.find_element(By.XPATH, '//*[@id="tmp"]/div[1]/a').click()
        return RegisterPage(self.driver)
