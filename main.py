"""
控制文件
"""
from test1.views import app
from test1.models import db


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=True, use_reloader=True)