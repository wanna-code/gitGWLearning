import pytest
# 测试脚本层：关注测试数据准备、断言及业务处理等
from api.login import LoginAPI

class TestImage:
    def setup(self):
        self.login_api=LoginAPI()

    def teardown(self):
        pass

    def test_login_access(self):
        verify_code = self.login_api.get_verify_code()
        print(verify_code.status_code)
        uuid=verify_code.json().get("uuid")
        request_body={
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uuid
        }
        login_res=self.login_api.login(request_body)
        print(login_res.json())

# if __name__=="__main__":
#     pytest.main(['-s'])
