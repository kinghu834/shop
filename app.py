from flask import Flask,request,jsonify
from mapper.sql import db,Shop
from routers import register_routes
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 将flask和数据库进行连接
db.init_app(app)

with app.app_context():
    db.create_all()
# 将路径函数和flask进行绑定
register_routes(app)

@app.route("/home")
def home():
    return "欢迎进入本店"
if __name__ == "__main__" :
        app.run(debug=True)



