# 获得要拷贝的文件名
# 读取要拷贝的文件内容
# 打开新的文件
# 将文件内容拷贝到另外一个文件里面
# 关闭新老文件
old_file_name = input('请输入您要拷贝的文件名：')

new_file_name = old_file_name + '.bk'

f_old = open(old_file_name, 'rb')
f_new = open(new_file_name, 'wb')

#  将老文件内容写到新文件里面
old_file_content = f_old.read()
f_new.write(old_file_content)

f_new.close()
f_old.close()