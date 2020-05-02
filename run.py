import pytest
from common.subprocess_dome import *

if __name__ == '__main__':
    pytest.main(["test_case"])
    allure_auto()  # 调用自动生成报告方法

# 通过命令  pip3 freeze > requirements.txt 生成全部依赖包，共持续集成使用
