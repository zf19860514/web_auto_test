import subprocess
import os.path
from selenium import webdriver


# shell=True可以直接输入字符串
# res = subprocess.call("ls -l", shell=True)


# 自动生成allure报告
def allure_auto():
    allure_cmd = "allure generate ../web_auto_test/report/result -o ../web_auto_test/report/html --clean"
    try:
        subprocess.call(allure_cmd, shell=True)
        print("成功生成测试报告")
    except:
        print("报告生成失败")
        raise

# 通过命令  pip3 freeze > requirements.txt 生成全部依赖包，共持续集成使用


def rm_rf():
    html = "../web_auto_test/report/html"
    result = "../web_auto_test/report/result"
    if os.path.exists(html):
        subprocess.call("rm -rf" + " " + html, shell=True)
    else:
        print("html文件夹不存在")
    if os.path.exists(result):
        subprocess.call("rm -rf" + " " + result, shell=True)
    else:
        print("result文件夹不存在")


def web_driver():
    # chrome驱动下载http://chromedriver.storage.googleapis.com/index.html
    # 和自己浏览器版本一致
    global driver
    driver = webdriver.Chrome(executable_path="../web_auto_test/common/chromedriver")
    # driver.get("file://" + os.path.abspath("../report/html/index.html"))
    driver.get("file://" + os.path.abspath("../web_auto_test/report/report.html"))


# if __name__ == '__main__':
#     web_driver()
