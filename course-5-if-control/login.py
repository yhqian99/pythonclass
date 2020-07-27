# if嵌套
# @Time    : 2020/7/26 15:06
# @Author  : yhqian
# @File    : login.py

# 预设一个用户名和密码
username = "张三"
password = "12345"
name = input("请输入用户名：")
pwd = input("请输入密码：")
if name == username:
    if pwd == password:
        print("登录成功")
    else:
        print("用户名或密码错")
else:
    print("用户名不存在")


