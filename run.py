import pytest
from common.subprocess_dome import *
import time

if __name__ == '__main__':
    rm_rf()  # 调用删除resuit和html文件夹方法
    pytest.main()
    # allure_auto()  # 调用自动生成报告方法
    # web_driver()

