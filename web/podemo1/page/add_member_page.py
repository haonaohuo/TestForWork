from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from web.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member(self, username, account, phonenum):
        # 用户名
        self.find(By.XPATH, '//*[@id="username"]').send_keys(username)
        # 账号
        self.find(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(account)
        # 电话
        self.find(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phonenum)
        # 点击“保存”按钮
        self.find(By.LINK_TEXT, '保存').click()

        checkbox = (By.CSS_SELECTOR, '.ww_checkbox')
        self.wait_for_click(checkbox)

        return True

    def get_member(self, value):
        # 验证联系人添加成功
        # contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

        # titlelist = [element.get_attribute("title") for element in contactlist]
        # titllist = []
        # for element in contactlist:
        #     titllist.append(element.get_attribute("title"))

        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]

            if value in titlelist:
                return True

            total_list = total_list + titlelist
            result: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()

        # return total_list


