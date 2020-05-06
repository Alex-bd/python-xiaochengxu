#!D:/CODE/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:43
# @Author : Alex-bd
# @Site : 
# @File : yield实现斐波那契.py
# @Software: PyCharm
# Functional description: yield实现斐波那契
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()