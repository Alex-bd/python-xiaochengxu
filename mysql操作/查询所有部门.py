#!D:/CODE/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 18:13
# @Author : Alexdong
# @Site : 
# @File : 查询所有部门.py
# @Software: PyCharm
# Functional description: 查询所有部门

import pymysql
from pymysql.cursors import DictCursor


def main():
    # 建立连接
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='yourname', password='yourpass')
    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute('select dno as no, dname as name, dloc as loc from tb_dept')
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'])
    finally:
        con.close()


if __name__ == '__main__':
    main()