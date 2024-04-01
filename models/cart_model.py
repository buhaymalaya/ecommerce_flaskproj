from app import db

# logic - a cart can only have one user; one user can only have one cart
# a cart should contain many products; a product can belong in many carts


class CartModel(db.Model):

    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable= False)
    # products = db.relationship("ProductModel", backref="cart")
    # quantity = db.Column(db.Integer)

    # users = db.relationship("UserModel", back_populates="users", uselist=False)
    # products = db.relationship("ProductModel", back_populates="products", uselist=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# class CartModel(db.Model):
#     __tablename__ = 'cart'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     # product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable= False)

#     # Define one-to-one relationship with user
#     user = db.relationship("UserModel", back_populates="cart")
#     # many to many below; backref creates reverse link
#     # products = db.relationship("ProductModel", secondary="prod_cart", backref="cart")
#     prod_cart = db.relationship("ProdCartModel", back_populates="cart")