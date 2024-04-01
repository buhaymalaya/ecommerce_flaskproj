from datetime import datetime

from app import db

class ProductModel(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)

    # cart = db.relationship("CartModel", back_populates="products")

    # Define many-to-many relationship with users through prod_cart
    # secondary=prod_cart indicates that this is the join table handling many to many link
    # users = db.relationship("UserModel", secondary='prod_cart', back_populates="products")


    def from_dict(self, a_dict):
        self.title = a_dict['title']
        setattr(self, 'body', a_dict['body'])
        self.price = a_dict['price']

    def save_product(self):
        db.session.add(self)
        db.session.commit()

    def del_product(self):
        db.session.delete(self)
        db.session.commit()

    