import os


def file_rename():
    os.rename('a.txt.bk', 'hello.txt')


# 文件删除
def test01():
    os.remove('C:/Users/田园佳/Desktop/1_数电(1).docx')


def test2():
    os.mkdir('C:/Users/田园佳/Desktop/1_数电(1).docx')


def test3():
    os.rmdir('C:/Users/田园佳/Desktop/1_数电(1).docx')


def test4():
    # 获得和设置工作目录
    content = os.listdir()
    print(content)


# 获得和设置工作目录
def test5():
    cwd = os.getcwd()
    print(cwd)
    os.chdir('C:/Users/田园佳/Desktop')
    os.mkdir('aaa')

test5()
# test4()
# test3()
# test2()

# file_rename()
