from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from register_page import RegisterPage


class LoginPage:
    # 接收上一个页面的driver，避免重复创建
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 扫码
    def scan(self):
        pass

    # 进入注册页面
    def goto_register(self):
        self.driver.find_element(By.XPATH, '//*[@id="wework_admin.loginpage_wx2_$"]/main/div[2]/a').click()
        return RegisterPage(self.driver)
