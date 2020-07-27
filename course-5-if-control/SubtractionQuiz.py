# 训练一年级学生10以内减法
# @Time    : 2020/7/17 17:00
# @Author  : yhqian
# @File    : SubtractionQuiz.py

import random

# 随机产生两个一位数
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# 如果num1<num2, 两数交换
if num1 < num2:
    num1, num2 = num2, num1

# 从控制台接收答案
answer = eval(input(str(num1) + "-" + str(num2) + "="))

# 判断正误
if answer == (num1 - num2):
    print('答对了')
else:
    print('答错了')
