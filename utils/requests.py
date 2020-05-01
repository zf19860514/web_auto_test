import requests


# 封装Get请求
def get_requests(url, headers):
    # 1.定义请求方式和传值
    r = requests.get(url, headers=headers)
    # 2.获取返回code
    code = r.status_code
    # 3.获取返回json
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 4.创建字典
    res = dict()
    # 5.保存内容字典
    res["code"] = code
    res["body"] = body
    # 6.返回字典
    return res


# 封装post请求
# None函数表示不传也可以执行
def post_requests(url, json=None, headers=None):
    # 1.定义请求方式和传值
    r = requests.post(url, json=json, headers=headers)
    # 2.获取返回code
    code = r.status_code
    # 3.获取返回json
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 4.创建字典
    res = dict()
    # 5.保存内容字典
    res["code"] = code
    res["body"] = body
    # 6.返回字典
    return res


# 组合封装 占放
def requests_api(method, url, json=None, headers=None):
    if method == requests.get:
        return requests.get(url, headers=headers)
    if method == "post":
        return requests.post(url, json=json, headers=headers)
    else:
        return "方法错误"
    # code = r.status_code
    # try:
    #     body = r.json()
    # except Exception as e:
    #     body = r.text
    # res = dict()
    # res["code"] = code
    # res["body"] = body
    # return res


