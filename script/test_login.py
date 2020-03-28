# 导包
import unittest
import logging
from utils import assert_common_uitls
import app
from api.login_api import LoginApi

# class LoginConfig:
#     # 定义请求头
#     headers = {"Content-Type": "application/json"}

# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self) -> None:
        # 实例化LoginApi登录的接口
        self.login_api = LoginApi()

    def tearDown(self) -> None:
        ...

    # 编写测试函数
    # 登陆成功
    def test01_login_success(self):
        # logging.info("app.headers是{}".format(app.headers))
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile":"13800000002","password":"123456"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        # response = self.login_api.login(jsonData, LoginConfig.headers)
        response = self.login_api.login(jsonData,app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码，success,code,msg
        # self.assertEqual(200, response.status_code)  # 与用例中文档的响应状态码进行比较断言
        # self.assertEqual(True, response.json().get("success"))  # 与用例文档中的预期json数据中的success的值进行比较
        # self.assertEqual(10000, response.json().get("code"))  # 与用例文档中预期json数据中的code进行比较
        # self.assertIn("操作成功", response.json().get("message"))  # 与用例文档中预期的json数据中的message进行比较

        # 导入封装通用断言的函数
        assert_common_uitls(self,response,200,True,10000,"操作成功")

    # 密码错误
    def test02_password_is_error(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "error"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 20001, "用户名或密码错误")

    # 账号不存在
    def test03_mobile_is_not_exist(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13800000033", "password": "123456"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 20001, "用户名或密码错误")

    # 输入的手机号码有英文符号
    def test04_mobile_has_eng(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "1380000A0X2", "password": "123456"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码有特殊符号
    def test05_mobile_has_special(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "1380(*00002", "password": "123456"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码为空:断言失败就以为代码写错了,实际工作中断言是帮助我们接口有没有问题的一种技术
    # 如果断言失败了，那么说明这个接口有Bug
    def test06_mobile_is_None(self):   # 断言失败：有Bug,需要提Bug
        # 定义登陆成功所需要的请求体error
        jsonData = {"mobile": "", "password": "123456"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test07_password_is_None(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": ""}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参 -- 多出一个参数
    def test08_more_params(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "123456","sign":"123"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, True, 10000, "操作成功")

    # 少参-缺少mobile
    def test09_less_mobile(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"password": "123456"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 20001, "用户名或密码错误")
    # 少参-缺少password
    def test10_less_password(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13800000002"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参
    def test11_none_params(self):
        # 定义登陆成功所需要的请求体
        jsonData = None

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    # 错误参数--输入错误的参数
    def test12_params_is_error(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mboile": "13800000002", "password": "123456"}

        # 利用封装的登录请求接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果（首先要导入日志模块）
        logging.info("登录的结果为：{}".format(response.json()))

        # 导入封装通用断言的函数
        assert_common_uitls(self, response, 200, False, 20001, "用户名或密码错误")

