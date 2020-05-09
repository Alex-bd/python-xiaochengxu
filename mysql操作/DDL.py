#!D:/CODE/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 18:07
# @Author : Alexdong
# @Site : 
# @File : DDL.py
# @Software: PyCharm
# Functional description:DDL


# -- 创建名为school的数据库并设置默认的字符集和排序方式
# create database school default charset utf8;
#
# -- 切换到school数据库上下文环境
# use school;
#
# -- 创建学院表
# create table tb_college
# (
# collid 		int auto_increment comment '编号',
# collname 	varchar(50) not null comment '名称',
# collintro 	varchar(500) default '' comment '介绍',
# primary key (collid)
# );
#
# -- 创建学生表
# create table tb_student
# (
# stuid 		int not null comment '学号',
# stuname 	varchar(20) not null comment '姓名',
# stusex 		boolean default 1 comment '性别',
# stubirth 	date not null comment '出生日期',
# stuaddr 	varchar(255) default '' comment '籍贯',
# collid 		int not null comment '所属学院',
# primary key (stuid),
# foreign key (collid) references tb_college (collid)
# );
#
# -- 创建教师表
# create table tb_teacher
# (
# teaid 		int not null comment '工号',
# teaname 	varchar(20) not null comment '姓名',
# teatitle 	varchar(10) default '助教' comment '职称',
# collid 		int not null comment '所属学院',
# primary key (teaid),
# foreign key (collid) references tb_college (collid)
# );
#
# -- 创建课程表
# create table tb_course
# (
# couid 		int not null comment '编号',
# couname 	varchar(50) not null comment '名称',
# coucredit 	int not null comment '学分',
# teaid 		int not null comment '授课老师',
# primary key (couid),
# foreign key (teaid) references tb_teacher (teaid)
# );
#
# -- 创建选课记录表
# create table tb_record
# (
# recid 		int auto_increment comment '选课记录编号',
# sid 		int not null comment '选课学生',
# cid 		int not null comment '所选课程',
# seldate 	datetime default now() comment '选课时间日期',
# score 		decimal(4,1) comment '考试成绩',
# primary key (recid),
# foreign key (sid) references tb_student (stuid),
# foreign key (cid) references tb_course (couid),
# unique (sid, cid)
# );