# 元组使用 小括号 可以遍历 但不能修改 限制数据的以外修改

# tuple

# my_tuple = (10, 20, 30)
# print(my_tuple)
# my_tuple = (10,)
# # 元组中只有一个元素的换在元素后面添加,
# my_tuple1 = ((1, 2), (2, 3))

my_tuple = (1, 2, 3, 4, 5)

# for i in my_tuple:
#     print(i)


#  元组支持查询 count index
# 遍历

pos = my_tuple.index(2)
# 返回的是索引
print(pos)

# 元组比列表更节省空间 空间固定 元组支持切片
print(my_tuple[1:])
