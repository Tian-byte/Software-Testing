# # # # 打印 1- 100数字
# # #
# # # i = 1
# # # while i <= 100:
# # #     print(i)
# # #     i = i + 1
# # # print('END')
# # #
# # #
# #
# #
# # # 打印1-100 之间的偶数
# # # i = 1
# # # while i <= 100:
# # #     if i % 2 == 0:
# # #         print(i)
# # #     i = i + 1
# #
# #
# # # 计算1-100的结果
# #
# # i = 1
# # And = 0
# # while i <= 100:
# #     And += i
# #     i += 1
# # print(And)
# #
# # # 计算1-100 之间的奇数和
# # a = 1
# # Sum = 0
# # while a <= 100:
# #     if a % 2 == 1:
# #         Sum = Sum + a
# #     a += 1
# # print(Sum)
#
# a = 1
# Sum = 0
# while a <= 100:
#
#     if a == 50:
#         a += 1
#         continue
#
#     Sum += a
#     a += 1
# print(Sum)
#


a = 1
add = 0

while a <= 100:
    print(a)
    if a == 50:
        break
    a = a+1
