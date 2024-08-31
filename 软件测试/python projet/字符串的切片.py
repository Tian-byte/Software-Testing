# # # 字符串提供了一种语法 用来获取字符串中的一个字符串
# #
# # user_email = 'abcdefg@qq.com'
# # print(user_email[0])
# # # 切片左闭右开 不包含右面的数
# # print(user_email[0: 4])
# #
# #
# # string_length = len(user_email)
# # print(user_email[7:string_length])
# # print(user_email[: 7])
# # print(user_email[7:])
# #
# #
# # # 步长 第三个值
# # print(user_email[0:7:2])
# #
# #
# #
# # '
# my_str = 'aa#bb#cc#ddd#ccc'
# my_str1 = my_str.split('#')
# print(my_str1[0])
#
#
#

my_email = '1473316640'
# result = my_email.split('@')
# print(result)
# print(result[0])
# print(result[1])

# 字符串去除两端空格
a = my_email.strip()
print(a)

# if my_email.isalpha():
if my_email.isdigit():
    print('成功')
else:
    print('失败')
