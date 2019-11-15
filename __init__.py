# 实例化
from flask_bootstrap import Bootstrap
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api

app = Flask(__name__)#创建实例
bootstrap = Bootstrap(app)
api = Api(app)

base_path = os.path.abspath(os.path.dirname(__file__))

# 配置数据库路径
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_path, "orm.sqlite3")
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/sy"
#请求结束自动提交数据库操作
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

#flask.1版本之后添加的跟踪修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

app.config["SECRET_KEY"] = "123"

#app加载数据库orm
db = SQLAlchemy(app)

