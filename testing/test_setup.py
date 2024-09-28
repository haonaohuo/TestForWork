# setup和teardown被弃用，使用装饰器fixture
import pytest


@pytest.fixture(scope="module")  # scope可以是 function, class, module, package 或 session
def setup_teardown():
    print("设置测试环境")
    yield  # 这里是测试执行的位置
    print("清理测试环境")


def test_example(setup_teardown):
    # 这里是测试代码
    print("test example")
    pass


test_user = ["小明", "小李"]


@pytest.fixture(params=test_user)
def input_user(request):
    # params是一个列表，用来存放我们要参数化的值
    # 固定写法request.param，其中列表test_user有几个元素就调用几次，分别作用在每个用到的函数上
    user = request.param
    return user


def test_user(input_user):
    print(input_user)
    print(f"用户名，{input_user}")


class TestDemo:

    def test_demo1(self, setup_teardown):
        print("test demo1")

    def test_demo2(self, setup_teardown):
        print("test demo2")
