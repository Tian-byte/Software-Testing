# 读取json 文件

import json
import os


def read_json(filename,key):
    filepath = os.path.dirname(__file__) + os.sep + "data" + os.sep + filename
    arr = []
    with open(filepath,"r",encoding="utf-8") as f:
        for data in json.load(f).get(key):
            arr.append(tuple(data.values())[1:])
        return arr


if __name__ == '__main__':
    print(read_json("login.json","login"))


