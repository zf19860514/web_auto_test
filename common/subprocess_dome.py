import subprocess


# shell=True可以直接输入字符串
# res = subprocess.call("ls -l", shell=True)


# 自动生成allure报告
def allure_auto():
    allure_cmd = "allure generate ../report/result -o ../report/html --clean"
    print("成功生成测试报告")
    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        print("报告生成失败")
        raise

# 通过命令  pip3 freeze > requirements.txt 生成全部依赖包，共持续集成使用
