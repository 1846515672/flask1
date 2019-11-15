"""
定义数据库模型
"""
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from test1 import db



class Model(db.Model):
    __abstract__ = True #代表当前类为抽象类,不会再继承过程当中执行
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        session = db.session()
        session.add(self)
        session.commit()

    def delete(self):
        session = db.session()
        session.delete(self)
        session.commit()

user_course = db.Table(
    'user_course',#表名
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"))
)#只用于关系表


# class Role(Model):
#     r_name = db.Column(db.String(32))
#     description = db.Column(db.Text)
#     user_role = db.relationship("User", backref="role")#加入uselist=False
# 表示一对一

class User(Model):
    # __tablename__="user"
    nick_name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))
    # role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    # course = db.relationship("Course", secondary=user_course, backref="c_user")
    # def __repr__(self):
    #     return self.u_name

class Course(Model):
    c_name = db.Column(db.String(32))#课程名称
    description = db.Column(db.String(32))#课程描述
    picture = db.Column(db.String(32))#课程logo
    show_number = db.Column(db.Integer)#观看人数
    c_time_number = db.Column(db.Integer)#课时
    state = db.Column(db.Integer, default=1)#课程状态 0即将上线,1上线
    c_type = db.Column(db.Integer,default=0)#课程类型 0免费, 1限时免费,2vip会员
    label_id = db.Column(db.Integer, db.ForeignKey("label.id"))

    def __repr__(self):
        return self.c_name

class Label(Model):
    l_name = db.Column(db.String(32))  # 标签名称
    description = db.Column(db.Text)  # 标签描述
    c_label = db.relationship("Course", backref="class_label")

    def __repr__(self):
        return self.l_name





