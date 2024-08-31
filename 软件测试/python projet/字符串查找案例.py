# user_email = 'abcdefg@qq.com'
# 1.找字符串 @ 的位置
# 2.活动字符串的字符

user_email = 'abcdefg@qq.com'

a = user_email.find('@')
# 返回@的位置

if a == -1:
    print('@不存在')
else:
    print('@的位置：', a)
