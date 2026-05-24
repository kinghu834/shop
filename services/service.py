from mapper.sql import Shop,db
def add_shop(product_name,price) :
    user = Shop(
         product_name = product_name,
         price = price
    )
    db.session.add(user)
    db.session.commit()
    return user

def get_message(id) :
    message = Shop.query.get(id)
    return message

def get_value() :
     All = Shop.query.all()
     return All

def get_shop(id,new_price) :
     content = Shop.query.get(id)
     if not content :
          return None
     content.price = new_price
     db.session.commit()
     return content

def del_product(id) :
     value = Shop.query.get(id)
     if not value :
          return None
     db.session.delete(value)
     db.session.commit()
     return value


     



