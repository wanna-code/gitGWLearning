import json

from api.course import CourseAPI
from api.login import LoginAPI

class Test_addCourse:

    def setup(self):
        self.ca=CourseAPI()
        self.la=LoginAPI()

    def test_addCourse(self):
        # 获取登录的密码uuid
        uuid_code = self.la.get_verify_code().json().get("uuid")
        request_body = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uuid_code
        }
        #获取由密码得到的动态令牌
        temp_token = self.la.login(request_body).json().get("token")
        with open("../data/courseData.json","r",encoding="utf-8") as f:
            course_data=json.load(f)
        response_res = self.ca.add_course(course_data, temp_token)
        print(response_res.json())

    def teardown(self):
        pass

