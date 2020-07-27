# 计算身体质量指数BMI
# @Time    : 2020/7/22 16:39
# @Author  : yhqian
# @File    : bmi.py

weight = eval(input('请输入体重公斤数：'))
height = eval(input('请输入数身高米数：'))
bmi = weight / (height * height)
print("bmi=", bmi)

if bmi < 18.5:
    print("偏瘦")
elif 18.5 <= bmi < 23:
    print("正常")
elif 23 <= bmi < 25:
    print("偏胖")
elif 25 <= bmi < 30:
    print("肥胖")
else:
    print("重度肥胖")
