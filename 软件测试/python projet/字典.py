#
# my_dict = {key1: value1, key2 : value2}
# 健是唯一的，如果重复最后的一个健值对会替换前面的，值不唯一
# 字典不支持索引 切片操作 字典的查询性能优于列表

def test01():
    my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
    # print(my_dict['name'])
    # my_dict['age'] = 999
    # print(my_dict)
    # my_dict['score'] = 99
    # my_dict['name'] = '里斯'
    # del my_dict['name']
    #
    # # my_dict.clear()
    # del my_dict['age']

    # print(i)
    # # 只遍历出来健
    # key_list = my_dict.keys()
    # print(list(key_list))
    # value_list = my_dict.values()
    # print(list(value_list))
    #
    key_value_list = my_dict.items()

    for i in key_value_list:
        print(i)


test01()
