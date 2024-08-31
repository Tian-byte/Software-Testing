# 创建一个列表
import random

my_list = []
i = 0
while i < 10:
    random_number = random.randint(1, 100)
    # 将随机数存入列表
    my_list.append(random_number)
    i += 1

print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=False)

# 逆序
my_list.reverse()
print(my_list)