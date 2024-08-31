# 使用open函数打开一个文件

# fa = open('a.txt', 'w')
#
#
# my_content = 'hello world! 第一次打开文件!\n'
#
# fa.write(my_content)
fb = open('b.txt', 'r')
my_content = fb.read()
print(my_content)
# 关闭文件
fb.close()
