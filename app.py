from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  # 添加这一行
# 第一步，创建首页
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# 定义数据库表格数据类型
class Shop(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    product_name = db.Column(db.String(10))
    price = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.DateTime,default = datetime.now)
with app.app_context():
#  唤醒flask
    db.create_all()
# 添加数据
@app.route("/shop",methods = ["POST"])
def add_shop() :
    users = [
    Shop(product_name = "纸巾",price = 100),
    Shop(product_name = "鞋子",price = 200),
    Shop(product_name = "手机",price = 300),
    Shop(product_name = "自行车",price = 400)
    ]
    db.session.add_all(users)
    db.session.commit()
    return "数据添加成功"
# 查询
@app.route("/shop/<int:id>",methods = ["GET"])
def get_massage(id) :
    massage = Shop.query.get(id)
    if massage :
        return {
            "name" : massage.product_name,
            "price" : massage.price,
            "created_at" : massage.created_at
        }
    else :
        return "该商品不存在"
# 修改商品价格
@app.route("/shop/<int:id>",methods = ["PUT"])
def update_shop(id) :
     data = request.get_json()
     content = Shop.query.get(id)
     if not content :
          return "无法找到此商品"
     
     if "price" in data :
          content.price = data["price"]
          db.session.commit()
          return "商品价格修改成功"
# 删除数据
@app.route("/shop/<int:id>",methods = ["DELETE"])
def del_product(id) :
    #  data = request.get_json()
     value = Shop.query.get(id)
     if not value :
          return "无法找到此商品"
     
     if value :
          db.session.delete(value)
          db.session.commit()
          return "商品数据删除成功"


@app.route("/home")
def home():
    return "欢迎进入本店"
if __name__ == "__main__" :
        app.run(debug=True)



