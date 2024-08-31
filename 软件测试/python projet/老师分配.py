# 以个学校 3个办公室 现在有8位老师待工位分配，请编写程序，完成随机分配

import random

# 定义学校和办公室
school = [[], [], []]


def create_teachers():
    """创建老师列表"""
    # 定义列表保存老师
    teacher_list = []
    index = 1
    while index <= 8:
        # 创建老师的名字
        teacher_name = '老师' + str(index)
        teacher_list.append(teacher_name)
        index += 1

    return teacher_list


teacher_lists = create_teachers()

# 分配老师
for teacher in teacher_lists:
    office_number = random.randint(0, 2)
    # 给老师随机分配办公室
    school[office_number].append(teacher)

# 产看各个老师办公室
for office in school:
    for person in office:
        print(person, end=' ')
    print()
