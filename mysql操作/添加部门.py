#!D:/CODE/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 18:10
# @Author : Alexdong
# @Site : 
# @File : 添加部门.py
# @Software: PyCharm
# Functional description:向tb_dept里 添加一个部门
import pymysql


def main():
    no = int(input('编号: '))
    name = input('名字: ')
    loc = input('所在地: ')
    # 1. 创建数据库连接对象
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='yourpass')
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                'insert into tb_dept values (%s, %s, %s)',
                (no, name, loc)
            )
        if result == 1:
            print('添加成功!')
        # 4. 操作成功提交事务
        con.commit()
    finally:
        # 5. 关闭连接释放资源
        con.close()


if __name__ == '__main__':
    main()