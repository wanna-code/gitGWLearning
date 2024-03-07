import json

import requests


def regular_method():
    """
    获取对应地址的图片验证码
    """

    # 发送请求
    response = requests.get(url='http://kdtx-test.itheima.net/api/captchaImage')
    # 查看响应
    print(response.status_code)
    print(response.text)

    dictData: dict = response.json()
    print(dictData.get('uuid'))
    return dictData.get('uuid')
    # 通过json.loads将str类型转换成dict类型
    # print(json.loads(response.text).get("uuid"))


# 使用json格式的请求体获取响应数据
def regular_method2(uuid):
    # 读取json文件数据后更改某个键值并写入源文件
    with open('../data/requestData.json', 'r', encoding='utf-8') as f:
        dictTemp = json.load(f)
        print(dictTemp)
        print(type(dictTemp))
    dictTemp['uuid'] = uuid
    with open('../data/requestData.json', 'w', encoding='utf-8') as f:
        json.dump(dictTemp, f)

    # 请求头
    header_data = {"Content-Type": "application/json"}
    # 请求体
    login_data = {
        "username": "admin",
        "password": "HM_2023_test",
        "code": "2",
        "uuid": dictTemp['uuid']
    }
    # response = requests.post(url='http://kdtx-test.itheima.net/api/login',headers=header_data,
    #                          json='../data/requestData.json')
    response = requests.post(url='http://kdtx-test.itheima.net/api/login', headers=header_data,
                             json=login_data)
    print(response.text)
    print(response.status_code)
    # 获取登录成功返回的登录令牌token值
    print(response.json().get('token'))


if __name__ == "__main__":
    regular_method2(regular_method())
    # print(regular_method.__doc__.strip())


