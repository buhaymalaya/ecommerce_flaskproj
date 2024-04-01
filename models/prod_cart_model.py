# # JOIN TABLE logic - a user can have many products; a product can belong to many users

# from app import db

# class ProdCartModel(db.Model):

#     __tablename__ = 'prod_cart'

#     id = db.Column(db.Integer, primary_key = True)
#     cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable= False)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable= False)
#     cart = db.relationship("CartModel", back_populates="prod_cart")
#     product = db.relationship("ProductModel", back_populates="carts")

#     def save_prodcart(self):
#         db.session.add(self)
#         db.session.commit()

#     def del_prodcart(self):
#         db.session.delete(self)
#         db.session.commit()

        
