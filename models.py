from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class product_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String())
    price = db.Column(db.Integer())

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price