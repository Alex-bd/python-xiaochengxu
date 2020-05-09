#!D:/CODE/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 18:12
# @Author : Alexdong
# @Site : 
# @File : 更新部门.py
# @Software: PyCharm
# Functional description: 更新部门

import pymysql


def main():
    no = int(input('编号: '))
    name = input('名字: ')
    loc = input('所在地: ')
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='yourname', password='yourpass',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'update tb_dept set dname=%s, dloc=%s where dno=%s',
                (name, loc, no)
            )
        if result == 1:
            print('更新成功!')
    finally:
        con.close()


if __name__ == '__main__':
    main()