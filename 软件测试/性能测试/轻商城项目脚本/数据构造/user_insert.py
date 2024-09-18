from turtledemo.chaos import coosys

import pymysql

conn = pymysql.Connect(host='www.litemall360.com', port=3306, user='root', password='123456', database='litemall',charset='utf8')

cursor = conn.cursor()

sql1 = "INSERT INTO `litemall`.`litemall_user`(`id`, `username`, `password`, `gender`, `birthday`, `last_login_time`, `last_login_ip`, `user_level`, `nickname`, `mobile`, `avatar`, `weixin_openid`, `session_key`, `status`, `add_time`, `update_time`, `deleted`) VALUES ({}, 'user{}', '$2a$10$lTu9qi0hr19OC800Db.eludFr0AXuJUSrMHi/iPYhKRlPFeqJxlye', 1, NULL, '2024-09-15 12:38:11', '192.168.217.1', 0, 'user{}', '{}', '', '', '', 0, '2019-04-20 22:17:43', '2024-09-15 12:38:11', 0);"

sql2 = "INSERT INTO `litemall`.`litemall_address`(`id`, `name`, `user_id`, `province`, `city`, `county`, `address_detail`, `area_code`, `postal_code`, `tel`, `is_default`, `add_time`, `update_time`, `deleted`) VALUES ({}, 'user{}', {}, '北京市', '市辖区', '东城区', '长安街10000号', '110101', '', '{}', 0, '2024-09-15 12:29:24', '2024-09-15 12:29:24', 0);"

user_start = 110000
for i in range(10000):
    user_id = user_start + i
    mobile = "13011" + str(user_id)
    addr_id = user_start + i
    print("插入第{}条数据，用户id为{}".format(i+1,user_id))
    cursor.execute(sql1.format(user_id,user_id,user_id,mobile))
    cursor.execute(sql2.format(addr_id, user_id, user_id, mobile))

conn.commit()
cursor.close()
conn.commit()