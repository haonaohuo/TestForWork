def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


"""
终端执行命令

pytest/ py.test
pytest -v 打印详细运行日志信息
pytest -v -s 文件名
pytest 文件名.py 执行单独一个pytest模块
pytest 文件名.py::类名 运行某个模块里面某个类
pytest 文件名.py::类名::方法名 运行某个模块里面某个类里面的方法
pytest -x 文件名 一旦运行到报错，就停止运行
pytest --maxfail=[num] 当运行错误达到num的时候就停止运行
pytest -m[标记名] @pytest.mark.[标记名]将运行有这个标记的测试用例
"""

"""
1、用例设计不要有顺序
2、用例之间不要相互依赖
"""

"""
pytest 常用插件

pip install pytest-ordering 用例顺序
pip install pytest-rerunfailures 用例失败重跑
pip install pytest-assume 断言失败后继续跑
pip install pytest-xdist 分布式执行
"""

"""
使用allure

1、pytest --alluredir ./result 运行用例生成报告
2、allure serve ./result 启用外部web服务展示报告

3、allure generate ./result 在本地生成html文件
"""
