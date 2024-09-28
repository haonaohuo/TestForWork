import sys
import os
import pytest

# pytest命令行运行报错找不到包，先把项目地址添加到系统的环境变量里，再使用以下两行代码
# r表示\不转译
# sys.path.append(r"D:\Test\pythonProject\pytest测试")
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from pythonCode.calculator import Calculator
import yaml

calc = Calculator()


# 解析测试数据文件
def get_datas():
    with open(r"D:\Test\pythonProject\pytest测试\testing\datas\calc.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add"]["datas"]
        add_ids = datas["add"]["ids"]

        return [add_datas, add_ids]


# 解析测试步骤文件
def steps(add_steps_file, calc, a, b, expect):
    with open(add_steps_file, encoding='utf-8') as f:
        steps = yaml.safe_load(f)

        for step in steps:
            if 'add' == step:
                print("step: add")
                result = calc.add(a, b)
            elif 'add1' == step:
                print("step: add1")
                result = calc.add1(a, b)
            assert expect == result


@pytest.fixture()
def begin():
    print("计算开始")

    yield

    print("计算结束")


class TestCalc:

    # 装饰器传参
    # @pytest.mark.parametrize('a,b,expect', [
    #     [1, 1, 2],
    #     [100, 100, 200],
    #     [0.1, 0.1, 0.2]
    # ], ids=[
    #     'int_case',
    #     'bignum_case',
    #     'float_case'
    # ])

    @pytest.mark.parametrize('a, b, expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect, begin):
        result = calc.add(a, b)
        assert result == expect

    # def test_add1(self, begin):
    #     result = calc.add(100, 100)
    #     assert result == 200
    #
    # def test_add2(self, begin):
    #     result = calc.add(0.1, 0.1)
    #     assert result == 0.2

    # 捕捉分母为0
    @pytest.mark.parametrize('a,b', [
        [0.1, 0],
        [10, 0]
    ])
    def test_div_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            calc.div(a, b)

    def test_add_steps(self):
        a = 1
        b = 1
        expect = 2
        steps(r'D:\Test\pythonProject\pytest测试\testing\steps\add_steps.yml', calc, a, b, expect)
