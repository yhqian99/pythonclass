# 判断一个数是不是四叶玫瑰数
# 四位的四叶玫瑰数共有3个：1634，8208，9474
# @Time    : 2020/7/22 17:52
# @Author  : yhqian
# @File    : rose.py

number = eval(input("请输入一个四位整数:"))
gw = number % 10                # 对10取余数
sw = number // 10 % 10          # 整除10,  再对10取余数
bw = number // 100 % 10         # 整除100, 再对10取余数
qw = number // 1000 % 10        # 整除1000, 再对10取余数
sum = gw ** 4 + sw ** 4 + bw ** 4 + qw ** 4
if sum == number:
    print(number, "是四叶玫瑰数")
else:
    print(number, "不是四叶玫瑰数")



