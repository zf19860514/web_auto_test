import pytest
from common.subprocess_dome import *

if __name__ == '__main__':
    pytest.main(["test_case"])
    allure_auto()  # 调用自动生成报告方法
