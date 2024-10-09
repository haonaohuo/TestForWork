from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from web.podemo1.page.add_member_page import AddMemberPage
from web.podemo1.page.base_page import BasePage



class ContactsPage(BasePage):
    # 进入添加成员页面
    def goto_addmember(self):
        # sleep(3)
        # 点击【添加联系人】按钮
        # self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        # 显示等待，10秒钟内尝试元素是否可点击(不能处理)
        # element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # element = self.wait_for_click(locator)
        # element.click()

        # 重复点击【添加联系人】按钮，直到成功
        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, 'username')
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        return AddMemberPage(self.driver)
