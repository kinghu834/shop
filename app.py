from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  # 添加这一行
# 第一步，创建首页
app = Flask(__name__)
# 这是Flask应用的配置项设置，用于告诉Flask-SQLAlchemy扩展"数据库连接字符串存在哪里"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/shop'
# 关闭SQLAlchemy的对象修改追踪功能，不占内存，性能更好
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# 定义数据库表格数据类型
class Shop(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    product_name = db.Column(db.String(100))
    price = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.DateTime,default = datetime.now)
with app.app_context():
#  唤醒flask
    db.create_all()
# 添加数据
@app.route("/shop",methods = ["POST"])
def add_shop() :
    data = request.get_json()
    user = Shop(
         product_name = data["product_name"],
         price = data["price"]
    )
    db.session.add(user)
    db.session.commit()
    return "数据添加成功"
# 查询
@app.route("/shop/<int:id>",methods = ["GET"])
def get_message(id) :
    message = Shop.query.get(id)
    if message :
        return {
            "name" : message.product_name,
            "price" : message.price,
            "created_at" : message.created_at
        }
    else :
        return "该商品不存在"
# 查询商品列表
@app.route("/shop",methods = ["GET"])
def get_value() :
     All = Shop.query.all()
     return [
          {
               "name" : p.product_name,
               "price" : p.price,
               "created_at" : p.created_at
          } for p in All
     ]
    #  从数据库 shop 表中查出所有商品，返回一个列表
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



