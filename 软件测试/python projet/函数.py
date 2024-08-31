# # # # # def my_sum():
# # # # #     i = 1
# # # # #     s = 0
# # # # #     while i <= 100:
# # # # #         s = s + i
# # # # #         i += 1
# # # # #
# # # # #     print(s)
# # # # #
# # # # #
# # # # # # 函数调用
# # # # # my_sum()
# # # # #
# # # # #
# # # # #
# # # #
# # # #
# # # # def my_add(a, b):
# # # #     c = int(a) + int(b)
# # # #     print(c)
# # # #
# # # #
# # # # a = input()
# # # # b = input()
# # # # my_add(a, b)
# # #
# # # # 函数的返回值
# # #
# # # def my_add(a, b):
# # #     return a + b
# # #
# # #
# # # print(my_add(1, 3))
# #
# #
# # # 编写一个函数 进行加减乘除
# #
# # def jia(a, b, c):
# #     if c == '+':
# #         return int(a) + int(b)
# #     elif c == '-':
# #         return int(a) - int(b)
# #     elif c == '*':
# #         return int(a) * int(b)
# #     elif c == '/':
# #         return int(a) / int(b)
# #     else:
# #         print('输入错误！')
# #
# #
# # print(jia(1, 2, '-'))
# #
# #
# #
# #
#
# # 函数的缺省参数 （默认参数）
#
# def my_function(num=100):
#     print('num:', num)
#
#
# my_function()
#
# # 局部变量和全局变量
# # 局部变量 在函数的内部   全局变量在函数外部定义的变量
#
# # 一般定义全局变量 g_
# g_val = 100
#
#
# def my_fun1():
#     print(g_val)
#
#
# def my_fun2():
#     print(g_val)
#
#
#

my_number=100


def my_fun():
    my_number = 200
    print(my_number)


my_fun()
print(my_number)