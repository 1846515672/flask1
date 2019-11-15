"""
视图文件
"""
from test1 import api
import hashlib
from flask import Response, session
from sqlalchemy import and_, or_
from flask import request, redirect
from test1 import app
from flask import Flask,send_file
from flask import render_template
from test1.models import *
import random
from flask_restful import Resource


class CourseApi(Resource):
    def __init__(self):
        self.result = {
            "version": "v1",
            "code": "200",
            "data": [],
            "methods": "",
            "pageiation": {}
        }
    def to_dict(self, obj):
        query_str = str(obj.query).split("SELECT")[1].split("FROM")[0].strip()
        key_list = [k.split(" AS ")[1].replace("course_","") for k in query_str.split(",")]
        obj_to_dict = dict(
            zip(key_list, [getattr(obj, key) for key in key_list])
        )
        return obj_to_dict

    def get(self, id=None, page_num=None, page=None, field=None, value=None):
        if id:
            course_list = Course.query.get(int(id))
            data = self.to_dict(course_list)
            self.result["data"].append(data)
        else:
            if page == "page":
                page_obj = Course.query.order_by(db.desc("id")).paginate(int(page_num), 15)#第一个参数是页码,第二个参数是每页条数
                if field and str(value):
                    dicts = {field:value}
                    page_obj = Course.query.filter_by(**dicts).paginate(int(page_num),15)
                self.result["pageiation"]["has_next"] = page_obj.has_next
                self.result["pageiation"]["has_prev"] = page_obj.has_prev
                self.result["pageiation"]["next_num"] = page_obj.next_num
                self.result["pageiation"]["page"] = page_obj.page
                self.result["pageiation"]["pages"] = page_obj.pages
                self.result["pageiation"]["per_page"] = page_obj.per_page
                self.result["pageiation"]["prev_num"] = page_obj.prev_num
                self.result["pageiation"]["total"] = page_obj.total
                course_list = page_obj.items
            else:

                #如果有过滤条件,就按照过滤条件查询否则返回所有数据
                if field and str(value):
                    dicts = {field:value}
                    course_list = Course.query.filter_by(**dicts).all()
                else:
                    course_list = Course.query.all()
            self.result["data"] = [self.to_dict(i) for i in course_list]
        self.result["methods"] = request.method
        return self.result

    def post(self):
        self.result["methods"] = request.method
        return self.result

    def put(self, id):
        self.result["methods"] = request.method
        return self.result

    def detete(self):
        self.result["methods"] = request.method
        return self.result

api.add_resource(CourseApi,
                 "/CourseApi/",
                 "/CourseApi/<int:id>/",
                 "/CourseApi/<string:field>/<string:value>/",
                 "/CourseApi/<string:field>/<string:value>/<string:page>/<int:page_num>/",
                 "/CourseApi/page/<string:page>/<int:page_num>/"
                 )


# @app.route("/page_2/")
# @app.route("/page_2/<int:id>/")
# def page_2(id=1):
#     return "id is %s"%id


@app.route("/")
def index_ajax():
    return render_template("index.html")

@app.route("/ajax_user/", methods=["get", "post"])
def ajax_user():
    result = {"is_user": False}
    if request.method == "POST":
        nick_name = request.form.get("nick_name")
        email = request.form.get("email")
        password = request.form.get("password")
        print(nick_name,email,password,111)
        user = User()
        user.nick_name = nick_name
        user.email = email
        user.password = set_password(password)
        user.save()
        result["is_user"] = True
    return result

def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

@app.route("/al/")
def add_label():
    string1 = "UI CAD"
    for i in string1.split( ):
        l = Label()
        l.l_name = i
        l.description = "%s课啊, 好好玩啊!"%i
        # l.save()
    course1 = [{'src': 'https://dn-simplecloud.shiyanlou.com/ncn63.jpg', 'alt': '新手指南之玩转实验楼'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/ncn1.jpg', 'alt': 'Linux 基础入门（新版）'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1480389303324.png', 'alt': 'Kali 渗透测试 - 后门技术实战（10个实验）'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1480389165511.png', 'alt': 'Kali 渗透测试 - Web 应用攻击实战'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1482113947345.png', 'alt': '使用OpenCV进行图片平滑处理打造模糊效果'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1482807365470.png', 'alt': '使用 Python 解数学方程'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1482215587606.png', 'alt': '跟我一起来玩转Makefile'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1480386391850.png', 'alt': 'Kali 渗透测试 - 服务器攻击实战（20个实验）'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1482113981000.png', 'alt': '手把手教你实现 Google 拓展插件'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1482113522578.png', 'alt': 'DVWA之暴力破解攻击'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1482113485097.png', 'alt': 'Python3实现简单的FTP认证服务器'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1481689616072.png', 'alt': 'SQLAlchemy 基础教程'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1481511769551.png', 'alt': '使用OpenCV&&C++进行模板匹配'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1481512189119.png', 'alt': 'Metasploit实现木马生成、捆绑及免杀'},
     {'src': 'https://dn-simplecloud.shiyanlou.com/1480644410422.png', 'alt': 'Python 3 实现 Markdown 解析器'}]
    for c in course1:
        course2 = Course()
        course2.c_name = c["alt"]
        course2.picture = c["src"]
        course2.show_number = random.randint(100,1000)
        course2.c_time_number = random.randint(1,40)
        course2.class_label = random.choice(Label.query.all())
        # course2.save()
    return "hello word"

# @app.route("/", methods=["get", "post"])
# def index():
#     register = request.args.get("register")
#     if request.method == "POST":
#         username = request.form.get("name")
#         email = request.form.get("email")
#         password = request.form.get("password")
#
#         user = User()
#         user.nick_name = username
#         user.password = set_password(password)
#         user.email = email
#         user.save()
#         register = True
#     response = Response(render_template("index.html", **locals()))
#     return response

@app.route("/courses/index/<path:url_arg>/")
def courses_index(url_arg):
    label_list = Label.query.all()#返回标签
    # course_list = Course.query.all()#所有课程
    # search_key = request.args.get("search")#获取get请求的参数
    # #过滤课程类型
    # if c_type == "all":
    #     course_list = Course.query.all()#所有课程
    # else:
    #     course_list = Course.query.filter_by(c_type = int(c_type))
    # if search_key:
    #     course_list = Course.query.filter(
    #         Course.c_name.like("%{}%".format(search_key))
    #     ).all() #模糊查询

    args = url_arg.split("/")
    len_arg = len(args)
    # 如果参数的个数是两个，那么安照参数1是类型 参数2是标签进行查询
    #设置全局变量,防止在判断的时候有条件分支缺失导致变量不存在
    c_type = ""#url传递过来的课程类型
    label = ""#url传递过来的课程标签
    referer_url = ""#提供label重新定位的参数
    referer_urll = "" #提供给c_type重新定位的参数
    if len_arg == 2:#请求由类型也有标签
        c_type, label = args#分解参数
        #查询python所有免费或者付费
        referer_url = "/courses/index/%s/"%c_type #定义label标签的链接
        referer_urll = label + "/" #定义课程类型的链接
        label_id = Label.query.filter_by(l_name = label)[0].id #获取对应的标签
        course_list = Course.query.filter(
            and_(
                Course.c_type == int(c_type),
                Course.label_id == label_id
            )
        )#查询对应的所有课程
        #url只有一个路由请求参数
    elif len_arg == 1:
        arg, = args #获取参数
        if arg.isdigit(): #通过类型判断参数是c_type 函数label
            c_type = arg #请求参数是c_type
            referer_url = "/courses/index/%s/"%c_type #定义label标签的链接
            if int(c_type) == 3:#判断全部
                course_list = Course.query.all()
            else:
                course_list = Course.query.filter_by(c_type=int(c_type))
        else:
            label = arg
            referer_urll = label+"/"#定义c_type标签的链接
            course_list = Label.query.filter_by(l_name=label)[0].c_label
    #如果参数的个数是一个，那么需要检查是类型还是标签
        #参数是类型，就查询当前类型的多有商品
        #参数是标签，查询所有当前标签的课程
    print("c_type:%s"%c_type)
    print("label:%s"%label)
    return render_template("courses/index.html", **locals())

# @app.route("/login/", methods=["get", "post"])
# def login():
#     response = redirect("/")#跳转回首页
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")
#
#         user = User.query.filter_by(email=email).first()
#         if user:
#             request_password = set_password(password)
#             if request_password == user.password:
#                 response.set_cookie("email", user.email)
#     return response

# @app.route("/logout/")
# def logout():
#     response = redirect("/")
#     response.delete_cookie("email")
#     return response

@app.route("/courses/show/")
def courses_show():
    return render_template("courses/show.html", **locals())

@app.route("/courses/show2/")
def courses_show2():
    return render_template("courses/show2.html", **locals())

@app.route("/courses/reports/")
def courses_reports():
    return render_template("courses/reports.html", **locals())

@app.route("/get_test/", methods=["GET", "POST"])
def get_test():
    """
    page_size = 5
    page = 1 page_start 0
    page = 2 page_start 5
    page = 3 page_start 10
    page = 4 page_start (n-1)*page_size
    :return:
    """
    # req = int(request.args.get("page", 1))
    # page_size = 5
    # start = (req-1) * page_size
    # course_list = Course.query.offset(start).limit(page_size).all()
    course = ""
    label_list = Label.query.all()
    if request.method == "POST":
        data = request.form
        c_name = data.get("c_name")
        show_number = data.get("show_number")
        c_time_number = data.get("c_time_number")
        label = data.get("label")
        description = data.get("description")
        logo = request.files.get("logo")
        #保存文件分为两步
        #文件保存到服务器
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "static\img\%s"%logo.filename
        )
        logo.save(file_path)
        #文件路径保存到数据库中
        course = Course()
        course.c_name = c_name
        course.show_number = show_number
        course.c_time_number = c_time_number
        course.description = description
        course.picture = "/static\img\%s"%logo.filename #保存图片路径
        course.class_label = Label.query.get(int(label))#保存外键
        course.save()
    return render_template("yes.html", **locals())

#cookie
@app.route("/cookies/")
def COOKIE():
    # response = Response("设置cookie")
    # response.set_cookie("name", "laobian")
    """
    key, cookie的键
    value="",cookie的值
    max_age = None,cookie的寿命
    expires = None,cookie的过期时间
    path = "/", cookie在当前项目的作用域
    domain = None, cookie起作用的子域名
    """
    cookie = request.cookies.get("name")#获取cookie
    print(cookie)
    response = Response("设置cookie")
    response.set_cookie("name", "laobian")
    response.delete_cookie("name") #删除cookie

    # 设置session
    session["username"] = "laobian"#设置session的值
    session.get("username") #获取session
    del session["username"] #删除session
    return "设置session"
    # return response

@app.route("/boos/")
def boos():
    return render_template("boos.html", **locals())

@app.route("/developer/index/")
def developer_index():
    return render_template("developer/index.html", **locals())

@app.route("/paths/index/")
def paths_index():
    return render_template("paths/index.html", **locals())

@app.route("/questions/index/")
def questions_index():
    return render_template("questions/index.html", **locals())

@app.route("/questions/show/")
def questions_show():
    return render_template("questions/show.html", **locals())

@app.route("/bootcamp/index/")
def bootcamp_index():
    return render_template("bootcamp/index.html", **locals())

@app.route("/vip/index/")
def vip_index():
    return render_template("vip/index.html", **locals())

@app.route("/privacy/index/")
def privacy_index():
    return render_template("privacy/index.html", **locals())

@app.route("/labs/index/")
def labs_index():
    return render_template("labs/index.html", **locals())

@app.route("/edu/index/")
def edu_index():
    return render_template("edu/index.html", **locals())

@app.route("/edu/uestc/")
def edu_uestc():
    return render_template("edu/uestc.html", **locals())