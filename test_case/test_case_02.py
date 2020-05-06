import pytest
import logging
import time

'''
函数阶级方法
运行于测试 方法 的始末
运行一次测试函数，就会运行一次 setup 和 teardown
'''


# 创建类名时首字母必须大写、大写、大写
class Test_pytest:
    logging.basicConfig(level=logging.DEBUG)

    def setup(self):
        print("Case开始执行")

    def teardown(self):
        print("Case执行结束")

    @pytest.mark.last   # 最后一个执行
    def test_01(self):
        log = logging.getLogger("test_01")
        time.sleep(1)
        log.debug("after 1 sec")
        assert 1 == 1

    # 跳过用例执行
    @pytest.mark.skip
    def test_02(self):
        assert 2 == 1

    def test_03(self):
        log = logging.getLogger("test_03")
        log.debug('after 2 sec')
        assert 2 == 2

    # 用例执行顺序 pip3 install pytest-ordering
    @pytest.mark.run(order=1)   # 第一个执行
    def test_04(self):
        assert 3 == 2


'''
类阶级方法
运行于测试 类 的始末
一个测试内只运行一次 setup_class 和 teardown_class
不关心测试类内有多少个测试函数
'''


# class Test_class:
#
#     def setup_class(self):
#         print("Case开始执行")
#
#     def teardown_class(self):
#         print("Case执行结束")
#
#     def test_00(self, x):
#         return x+1
#
#     # 如果期望给单一用例添加 重试 和 等待 出错时间
#     # 使用pytest装饰器
#     @pytest.mark.flaky(reruns=2, reruns_delay=2)
#     def test_01(self):
#         assert self.test_00(2) == 1
#
#     def test_02(self):
#         assert 2 == 1
#
#     def test_03(self):
#         assert 2 == 2
#
#     def test_04(self):
#         assert 3 == 3


# if __name__ == '__main__':
#     # pytest.main(["-s", "-v", "test_case_02.py"])
#     '''
#     场景:测试用例1000条，一个用例执行1钟，一个测试人员执行需要1000分 钟。
#     通常我们会用人力成本换取时间成本，加几个人一起执行，时间就会缩短。
#     如果10人一起执行只需要100分钟，这就是一种并行测试，分布式场景。
#     解决:pytest分布式执行插件:pytest-xdist，多个CPU或主机执行
#     前提:用例之间都是独立的，没有先后顺序，随机都能执行，可重复运行不 影响其他用例。
#     安装:pip3 install pytest-xdist
#     多个CPU并行执行用例，直接加-n 3是并行数量:pytest -n 3 • 在多个终端下一起执行
#     '''
#     pytest.main(["test_case_02.py"])
