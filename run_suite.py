# 导包
import unittest
import time

from HTMLTestRunner_PY3 import HTMLTestRunner

import app
from script.test_login_params import TestLogin
from script.test_emp_func import TestEmp
# 创建测试套件
suite = unittest.TestSuite()
# 添加测试用例到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))

# 定义测试报告名称
# ihrm_report_path = app.base_dir + '/report/ihrm{}.html'.format(time.strftime("%Y%m%d %H%M%S"))
ihrm_report_path = app.base_dir + '/report/ihrm.html'
with open(ihrm_report_path,'wb') as f:
    # 实例化htmltestrunner
    runner = HTMLTestRunner(f,verbosity=2,title="管理系统ihrm人力资源",description="这是使用HTMLTestRunner_PY3生成的报告")
    # 使用实例化htmltestrunner运行测试套件
    runner.run(suite)








