# if 语句基本案例
# @Time    : 2020/7/19 11:18
# @Author  : yhqian
# @File    : IfBasics.py

# 单向判断: 将两个数 num1 和 num2 按降序排列
num1, num2 = 1, 9
if num1 < num2:
    # t = num1
    # num1 = num2
    # num2 = t
    num1, num2 = num2, num1
print(num1, num2)

# 双向判断: 判断一个数的奇偶性
number = 8
if number % 2 == 0:
    print(number, "是偶数")
else:
    print(number, "是奇数")

# 多重判断：将百分制成绩转换为A,B,C,D,F五个等级
score = 87
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(score, " grade is " + grade)




