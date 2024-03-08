import requests

# 定义课程接口
class CourseAPI(object):
    def __init__(self):
        self.url="http://kdtx-test.itheima.net/api/clues/course"

    def add_course(self,course_data,temp_token):
        return requests.post(url=self.url,data=course_data,headers={"Authorization":temp_token})