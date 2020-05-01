import pytest

'''
函数阶级方法
运行于测试 方法 的始末
运行一次测试函数，就会运行一次 setup 和 teardown
'''


# 创建类名时首字母必须大写、大写、大写
class Test_pytest:

    def setup(self):
        print("Case开始执行")

    def teardown(self):
        print("Case执行结束")

    def test_01(self):
        assert 1 == 1

    def test_02(self):
        assert 2 == 1

    def test_03(self):
        assert 2 == 2

    def test_04(self):
        assert 3 == 2


'''
类阶级方法
运行于测试 类 的始末
一个测试内只运行一次 setup_class 和 teardown_class
不关心测试类内有多少个测试函数
'''


class Test_class:

    def setup_class(self):
        print("Case开始执行")

    def teardown_class(self):
        print("Case执行结束")

    def test_00(self, x):
        return x+1

    # 如果期望给单一用例添加 重试 和 等待 出错时间
    # 使用pytest装饰器
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_01(self):
        assert self.test_00(2) == 1

    def test_02(self):
        assert 2 == 1

    def test_03(self):
        assert 2 == 2

    def test_04(self):
        assert 3 == 3


if __name__ == '__main__':
    pytest.main(["-s", "test_case_02.py"])
