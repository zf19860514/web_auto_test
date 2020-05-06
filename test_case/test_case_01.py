import requests
from utils.requests import *
import pytest
import allure
from common.subprocess_dome import *
from data.body_data import *


@allure.feature("核心接口，一级标签")  # allure定义一级标签
class Test_Auto:
    # 登录
    # 单个参数传递，参数对应值，类型必须为可迭代类型，一般用list
    phone_list = ["15210013568", "1521001356", "152100013568"]

    @allure.title("登录用例1")  # allure自定义用例名称
    @allure.description("执行3次登录用例")  # allure添加用例描述
    @allure.story("执行6次登录接口，二级标签")  # allure定义二级标签
    @allure.severity(allure.severity_level.BLOCKER)  # 定义用例级别BLOCKER为P-2级别
    @pytest.mark.parametrize("phone", phone_list)  # 调用parametrize方法需传递，自定义参数名和参数对应值
    def test_1_login(self, phone):
        url = "https://android-api-v5-0.yangcong345.com/login"
        body = {"countryCode": "",
                "gps": "[40.00946, 116.5311]",
                "locationProvider": "lbs",
                "locationType": "5",
                "name": phone,
                "password": "a123456"
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, json=body, headers=headers)
        assert r.status_code == 200, r.json()
        # 定义全局变量用global
        global authorization
        authorization = {"authorization": r.headers["authorization"]}
        print(r.status_code)
        allure.dynamic.title(phone)  # 参数传递下动态获取用例名称

    # 登录传递多个参数
    # 传递时每个元素都是一个元祖，元祖里的每个元素和参数顺序必须一一对应
    phone_possword = [("15210013568", "a123456"), ("1521001356", "123456"), ("15210013569", "a123456")]

    @allure.title("登录用例2")
    @allure.description("执行3次注册用例")
    @allure.severity(allure.severity_level.CRITICAL)  # 定义用例级别CRITICAL为P-1级别
    @pytest.mark.parametrize(("phone", "possword"), phone_possword)
    def test_2_login01(self, phone, possword):
        url = "https://android-api-v5-0.yangcong345.com/login"
        body = {"countryCode": "",
                "gps": "[40.00946, 116.5311]",
                "locationProvider": "lbs",
                "locationType": "5",
                "name": phone,
                "password": possword
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, json=body, headers=headers)
        assert r.status_code == 200, r.json()
        allure.dynamic.title(phone)

    # 获取章节消息
    @allure.title("获取章节消息")
    @allure.story("三级标签")
    @allure.severity(allure.severity_level.MINOR)  # 定义用例级别MINOR为P0级别
    def test_3_play(self):
        url = "https://android-api-v5-0.yangcong345.com/study/course/3805afa8-57f7-11e7-914c-172a125ccf26/detail"
        r = get_requests(url, authorization)
        print(r)

    # 开屏
    @allure.title("开屏")
    @allure.severity(allure.severity_level.NORMAL)  # 定义用例级别NORMAL为P1级别
    def test_4_kaiping(self):
        url = "https://android-api-v5-0.yangcong345.com/config/welcome?position=common"
        headers = {
            "device": "b16628936b41d5e2",
            "client-type": "android-app",
            "client-version": "5.17.2",
            "client-channel": "huawei",
            "timestamp": "1576049537326",
            "appid": "A3E256BE-1391-448C-8869-0FC8ADC0C915",
            "sign": "617039394363BEB5E8E31FE685C19EB0"
        }
        # update函数将2个字典组合
        headers.update(authorization)
        r = get_requests(url, headers)
        print(r)

    # 切换学段
    @allure.story("四级标签")
    @allure.title("切换学段")
    @allure.severity(allure.severity_level.TRIVIAL)  # 定义用例级别为TRIVIALP2级别
    def test_5_quanhuan(self):
        url = "https://api-v5-0.yangcong345.com/api/revenue/user"
        headers = {"content-type": "application/json"}
        headers.update(authorization)
        body = {"stageId": 3}
        # 传递参数时要和定义的方法，顺序一致，不能颠倒
        r = post_requests(url, body, headers)


if __name__ == '__main__':
    # 单独执行单个方法时，路径后面添加::+方法名
    # pytest.main(["test_case_01.py::test_01_login01"])
    pytest.main(["test_case_01.py"])



