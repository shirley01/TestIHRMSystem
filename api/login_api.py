# ihrm人力资源管理系统伪代码
# 利用reponse = requests.post("http://182.92.81.159/api/sys/login",json={"mobile":"","password":""})

# 封装登陆接口
import requests # 导入requests 模块，利用requests模块封装登录接口

# 定义封装的登录API类
class LoginApi:
    def __init__(self):
        # 定义ihrm登录接口url
        self.login_url = "http://182.92.81.159/api/sys/login"

    # 定义封装的登录函数
    def login(self,jsonData,headers):
        response = requests.post(url=self.login_url,json = jsonData,headers=headers)
        return response

if __name__ == "__main__":
    login_api = LoginApi()
    jsonData = {"mobile":"13800000002","password":"123456"}
    headers = {"Content-Type":"application/json"}
    response = login_api.login(jsonData,headers)
    print("登陆的结果为:",response.json())