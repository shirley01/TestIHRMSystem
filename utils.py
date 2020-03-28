# 封装通用的断言函数
import os
# 导入模块
import json

def assert_common_uitls(self,
                        response,
                        http_code,
                        success,
                        code,
                        message):
    # self:从测试脚本中传入的测试类，继承了unittest.TestCase
    # response : 从测试脚本中传入的响应数据
    # http_code,success,code,message是预期要断言的响应状态码、success、code、message
    self.assertEqual(http_code, response.status_code)  # 与用例中文档的响应状态码进行比较断言
    self.assertEqual(success, response.json().get("success"))  # 与用例文档中的预期json数据中的success的值进行比较
    self.assertEqual(code, response.json().get("code"))  # 与用例文档中预期json数据中的code进行比较
    self.assertIn(message, response.json().get("message"))  # 与用例文档中预期的json数据中的message进行比较


# 封装读取登录数据的函数
def read_login_data(filename):
    # filename:是指登陆数据的路径和名称
    with open(filename,'r',encoding='utf-8') as f:

        # 加载json数据
        jsonData = json.load(f)
        # 定义一个存放数据的空列表
        result_list = []
        # 遍历这个jsonData，取出每一条登陆测试点的数据
        for login_data in jsonData:
            # print("login_data",login_data)
            # 将所有的数据以嵌套元组的形式存放在空列表当中
            result_list.append(tuple(login_data.values()))
    return result_list


def read_emp_data(filename,interface_name):
    with open(filename,'r',encoding='utf-8') as f:
        jsonData = json.load(f)
        # print(jsonData.get("add_emp"))
        result_list = []
        # 存放员工的某个接口的数据到空列表
        result_list.append(tuple(jsonData.get(interface_name).values()))
    return result_list

if __name__ == "__main__":
    filename = os.path.dirname(os.path.abspath(__file__)) + "/data/emp.json"
    print("路径为:" ,filename)
    # result = read_login_data(filename)
    # print(result)
    result = read_emp_data(filename,"add_emp")
    print(result)



