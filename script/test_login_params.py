# 导包
import unittest
import logging
from utils import assert_common_uitls,read_login_data
import app
from api.login_api import LoginApi
from parameterized import parameterized

# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self) -> None:
        # 实例化LoginApi登录的接口
        self.login_api = LoginApi()

    def tearDown(self) -> None:
        ...

    # 定义要加载的登录数据的路径
    filename = app.base_dir + '/data/login.json'

    # 编写测试函数
    # 登陆成功
    @parameterized.expand(read_login_data(filename))
    def test01_login(self, case_name, jsonData, http_code, success, code, message):
        # 定义登陆成功所需要的请求体
        jsonData = jsonData

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData,app.headers)

        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self,response, http_code, success, code, message)
