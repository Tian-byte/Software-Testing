# a = 10
# b = 20
# if a > b:
#     ret = a + b
# else:
#     ret = a - b
#
# print('ret = %d ' % ret)
#
# input_username = input('请输入您的用户名：')
# input_password = input('请输入密码：')
#
# correct_name = 'admin'
# correct_password = '123'
# if (input_username == correct_name) and (input_password == correct_password):
#     print('欢迎 %s 登录系统！' % input_username)
# else:
#     print("登录失败")
#
#


#  100 - 80 优秀  80 -60 及格  <60 不及格

a = float(input("请输入您的成绩:"))

if 80 <= a <= 100:
    print('优秀')
elif 80 < a <= 60:
    print('及格')
elif a < 60:
    print('不及格')
else:
    print('请输入合理的成绩')


