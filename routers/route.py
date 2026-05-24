from flask import Blueprint,request,jsonify
from mapper.sql import db,Shop
from services.service import add_shop,get_message,get_value,get_shop,del_product

# 创建蓝图
shop_bp = Blueprint("shop",__name__,url_prefix = "/shop")

@shop_bp.route("",methods= ["POST"])
def add_shop_route() :
    data = request.get_json()
    result = add_shop(data["product_name"],data["price"])
    return "数据添加成功"

@shop_bp.route("/<int:id>",methods = ["GET"])
def get_message_route(id) :
    message = get_message(id)
    if message :
        return {
            "name" : message.product_name,
            "price" : message.price,
            "created_at" : message.created_at
        }
    else :
        return "该商品不存在"

@shop_bp.route("",methods = ["GET"])
def get_value_route() :
     All = get_value()
     return [
          {
               "name" : p.product_name,
               "price" : p.price,
               "created_at" : p.created_at
          } for p in All
     ]

@shop_bp.route("/<int:id>",methods = ["PUT"])
def get_shop_route(id) :
    data = request.get_json()
    if "price" not in data :
         return "缺少修改条件"
    content = get_shop(id,data["price"])
    if not content :
          return "无法找到此商品"
    else :
          return "商品价格修改成功"
@shop_bp.route("/<int:id>",methods = ["DELETE"])
def del_product_route(id) :
          value = del_product(id)
          if value :
               return "商品删除成功"
          else :
               return "无法找到此商品"




