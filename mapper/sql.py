from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Shop(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    product_name = db.Column(db.String(100))
    price = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.DateTime,default = datetime.now)


