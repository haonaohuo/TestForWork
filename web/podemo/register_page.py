from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 填写注册信息
    def register(self):
        self.driver.find_element(By.XPATH, '//*[@id="corp_name"]').send_keys('haonaohuo')
        self.driver.find_element(By.XPATH, '//*[@id="manager_name"]').send_keys('好恼火')
        self.driver.find_element(By.XPATH, '//*[@id="register_tel"]').send_keys('12345678910')

        return True
