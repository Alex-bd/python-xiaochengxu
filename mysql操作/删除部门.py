#!D:/CODE/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 18:11
# @Author : Alexdong
# @Site : 
# @File : 删除部门.py
# @Software: PyCharm
# Functional description:删除tb_dept表中 输入的编号的部门
import pymysql


def main():
    no = int(input('编号: '))
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='yourname', password='yourpass',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'delete from tb_dept where dno=%s',
                (no, )
            )
        if result == 1:
            print('删除成功!')
    finally:
        con.close()


if __name__ == '__main__':
    main()