import pytest


# 如果测试用例里，需要用到fixture的返回值，fixture的名字需要以参数的形式传入到方法里，不能使用装饰器的方式。
def test_case1(login):
    # login是从conftest.py文件里调用的fixture
    print(login)
    print("用例1")


@pytest.mark.usefixtures("login")
def test_case2():
    # print(login)
    print("用例2")


def test_case3():
    print("用例3")
