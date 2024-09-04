# 定义一个函数，读取 data 文件下的某某文件
import json


def read_json_data(path_filename):
    # with open("../data/add_emp.json", "r", encoding="utf-8") as f:
    with open(path_filename, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        list_data = []
        for item in json_data:
            tmp = tuple(item.values())
            list_data.append(tmp)
    return list_data



if __name__ == '__main__':
    read_json_data()