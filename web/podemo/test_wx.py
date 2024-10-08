import pytest
from index_page import IndexPage


class TestWX:
    @pytest.fixture()
    def get_driver(self):
        self.index = IndexPage()

        yield

        # self.index.driver.quit()

    def test_register(self, get_driver):
        assert self.index.goto_login().goto_register().register()

        # assert self.index.goto_register().register()

