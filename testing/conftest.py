# conftest.py数据共享，文件名不能修改,全局共享
import pytest


@pytest.fixture(scope='function')  # scope可以是 function（默认）, class, module, package 或 session
def login():
    # setup操作
    print("登录操作")
    # yield相当于return
    yield ["tom", "123456"]
    # teardown操作
    print("登出操作")


# 这段代码是一个Python函数，用于修改pytest收集到的测试项目（test items）。
# pytest_collection_modifyitems是pytest插件中的一个钩子函数（hook）
# 从新编码，执行用例后看得到中文的ids
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
