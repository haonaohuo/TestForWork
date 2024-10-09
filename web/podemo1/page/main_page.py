from selenium.webdriver.common.by import By
from web.podemo1.page.add_member_page import AddMemberPage
from web.podemo1.page.base_page import BasePage
from web.podemo1.page.contacts_page import ContactsPage


class MainPage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#/index'

    # 进入添加成员页面
    def goto_addmember(self):
        # click addmember
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        return AddMemberPage(self.driver)

    # 进入通讯录页面
    def goto_contacts(self):
        self.find(By.XPATH, '//*[@id="menu_contacts"]').click()
        return ContactsPage(self.driver)
