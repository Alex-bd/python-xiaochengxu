#!D:/CODE/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:42
# @Author : Alex-bd
# @Site : 
# @File : 跑马灯.py
# @Software: PyCharm
# Functional description: 跑马灯
import os
import time


def main():
    content = '提前祝何水水生日快乐呀…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()