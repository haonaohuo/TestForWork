import pytest
from web.podemo1.page.main_page import MainPage
from time import sleep


class TestWX:
    @pytest.fixture()
    def get_driver(self):
        self.main = MainPage()

    # 添加联系人
    def test_addmember(self, get_driver):
        username = '小虾米97'
        account = '123456789197'
        phonenum = '12345678997'

        # addmember = self.main.goto_addmember()
        # addmember.add_member(username, account, phonenum)
        # assert username in addmember.get_member()
        addmember = self.main.goto_contacts().goto_addmember()
        addmember.add_member(username, account, phonenum)
        # sleep(3)
        assert True is addmember.get_member(username)
