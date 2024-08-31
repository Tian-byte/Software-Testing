# 在指定位置插入 插入和删除
# 创建一个空列表
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(10)
my_list.append(10)
my_list.insert(4, 1)
my_list.insert(2,200)
print(my_list)
my_list.pop(2)
my_list.pop(1)

my_list.remove(10)
print(my_list)
my_list.clear()
print(len(my_list))
