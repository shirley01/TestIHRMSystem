# 按照设计顺序编写员工模块的增删改查场景测试用例脚本
# 如果能按照设计顺序实现员工的增删改查，那么就证明，能够对员工模块进行操作了
# 也就证明能够使用代码完成接口测试

# 导包
import time
import unittest
import logging
import requests
import app
from api.emp_api import EmpApi
from api.login_api import LoginApi
from utils import assert_common_uitls,read_emp_data
from parameterized import parameterized
# 创建测试类
class TestEmp(unittest.TestCase):
    # 初始化
    def setUp(self) -> None:
        # 实例化封装的登录接口
        self.login_api = LoginApi()
        # 实例化封装的添加员工接口
        self.emp_api = EmpApi()
        # 定义员工模块的URL
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

    def tearDown(self) -> None:
        ...

    # 编写测试员工增删改查用例
    def test01_test_emp_operation(self):

        # 1、实现登录接口
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        headers=app.headers)
        #   获取登录接口返回的json数据
        result = response.json()
        # 输出登录的结果
        logging.info("员工模块登录接口的结果为：{}".format(result))
        #   把令牌提取出来，并保存到请求头当中
        token = result.get("data")
        app.headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        logging.info("登录成功后设置的请求头为：{}".format(app.headers))

    # 定义员工数据文件的路径
    filename = app.base_dir + '/data/emp.json'

    @parameterized.expand(read_emp_data(filename,'add_emp'))
    # 2、实现添加员工接口
    def test02_add_emp(self,username,mobile,http_code,success,code,message):

        response = self.emp_api.add_emp(username,mobile,app.headers)
        # 打印添加的结果
        logging.info("添加员工的结果为:{}".format(response.json()))
        #   获取添加员工返回的json数据
        add_result = response.json()
        #   把员工id提取出来，并保存到变量当中
        app.emp_id = add_result.get("data").get("id")
        logging.info("获取的员工ID为:{}".format(app.emp_id))
        # 断言
        assert_common_uitls(self,response,http_code,success,code,message)

    # 3、实现查询员工接口
    @parameterized.expand(read_emp_data(filename, "query_emp"))
    def test03_query_emp(self , http_code, success, code, message):
        # 发送查询员工的接口请求
        response = self.emp_api.query_emp(app.emp_id,app.headers)
        # 打印查询员工的结果
        logging.info("查询员工接口的结果为：{}".format(response.json()))
        # 断言
        assert_common_uitls(self, response,  http_code, success, code, message)

    # 4、实现修改员工接口
    @parameterized.expand(read_emp_data(filename, "modify_emp"))
    def test04_modify_emp(self, username, http_code, success, code, message):
        # 发送修改员工接口的请求
        response = self.emp_api.modify_emp(app.emp_id,username,app.headers)
        # 打印修改员工的结果
        logging.info("修改员工的结果为:{}".format(response.json()))

        # 现在由于修改员工返回的响应数据当中，没有修改的username
        # 所有我们并不知道修改的username有没有成功
        # 那么怎么办？
        # 我们需要连接到ihrm数据库中，然后按照添加员工返回的员工id查询这个员工id对应的
        # username的值，如果数据库的username与修改的username一致，那么就证明修改成功了
        # 实际数据：数据库查询出来的数据；预期：修改的数据
        # 我们执行的SQL语句，在navicat中是查不到任何数据的，原因是因为执行完毕之后，员工被删除了
        # 如果添加员工失败，那么员工ID提取失败，也会导致查询失败

        # 导包
        import pymysql
        # 连接数据库
        conn = pymysql.connect(host="182.92.81.159",user='readuser', password='iHRM_user_2019', database='ihrm')
        # 获取游标
        cursor = conn.cursor()
        # 执行查询的SQL语句
        sql = "select username from bs_user where id={}".format(app.emp_id)
        # 输出SQL语句
        logging.info("打印SQL语句:{}".format(sql))
        cursor.execute(sql)
        # 调试执行的SQL结果
        result = cursor.fetchone()
        logging.info("执行SQL语句查询的结果为:{}".format(result))
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        # 断言数据库查询的结果
        self.assertEqual(username,result[0])

        # 断言
        assert_common_uitls(self, response, http_code, success, code, message)

    # 5、实现删除员工接口
    @parameterized.expand(read_emp_data(filename, "delete_emp"))
    def test05_delete_emp(self, http_code, success, code, message):
        # 发送删除员工接口的请求
        response = self.emp_api.delete_emp(app.emp_id,app.headers)
        # 打印修改员工的结果
        logging.info("修改员工的结果为:{}".format(response.json()))
        # 断言
        assert_common_uitls(self, response,http_code, success, code, message)

