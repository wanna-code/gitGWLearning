import requests

# 创建登录的接口
class LoginAPI:
    # 接口封装时，依据接口文档封装接口信息，需要的测试数据从测试用例传递、接口方法被调用时需返回对应的响应结果

    def __init__(self):
        self.url_verify="http://kdtx-test.itheima.net/api/captchaImage"
        self.url_login="http://kdtx-test.itheima.net/api/login"
    # 验证码
    def get_verify_code(self):
        return requests.get(url=self.url_verify)
    # 登录
    def login(self,request_body):
        return requests.post(url=self.url_login,json=request_body)

