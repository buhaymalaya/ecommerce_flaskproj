from flask import Blueprint, jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from . import bp
from flask_smorest import abort

from models.user_model import UserModel
from models.product_model import ProductModel
from models.cart_model import CartModel 

from schemas import ProductSchema, UserSchema, CartSchema


@bp.route('/carttotal/<int:user_id>')
class CartList(MethodView):
    
    # tested - route that shows list of all items and total in cart for one user
    
    def get(self, user_id):
        # access cart items for the given user_id
        cart_items = CartModel.query.filter_by(user_id=user_id).all()

        if cart_items:
            # to store cart items
            serialized_cart = []

            for cart_item in cart_items:
                # access respective product for cart item
                product = ProductModel.query.get(cart_item.product_id)

                # convert ProductModel to a dict
                product_dict = {
                    'id': product.id,
                    'title': product.title,
                    'body': product.body,
                    'price': product.price
                }

                serialized_cart.append(product_dict)

            total_price = sum(product_dict['price'] for product_dict in serialized_cart)

            return {
                'cart': serialized_cart,
                'total_price': total_price
            }, 200
        else:
            return {'message': 'Cart is empty'}, 404



# tested - route that removes all items from a specific user's cart at once
    
    def delete(self):
        data = request.get_json()
        user_id = data.get('user_id')
        cart_items = CartModel.query.filter_by(user_id=user_id).all()
        if cart_items:
            for cart_item in cart_items:
                cart_item.delete()  
            return jsonify({'message': 'Cart cleared successfully'}), 200
        else:
            return jsonify({'message': 'Cart is already empty'}), 404



@bp.route('/cart/<int:user_id>')
class CartList(MethodView):
# tested with access token - user able to add a product to cart but only if logged in
    @jwt_required()
    @bp.response(201, ProductSchema)
    def post(self):
        data = request.get_json()
        user_id = get_jwt_identity()
        product_id = data.get('product_id')
        product = ProductModel.query.get(product_id)
        user = UserModel.query.get(user_id)
        if user and product:
            added_by_user = CartModel.query.filter_by(product_id = product_id).filter_by(user_id = user_id).all()
            if added_by_user:
                return product
            cartModel = CartModel(user_id=user_id, product_id=product_id)
            cartModel.save()
            return product
        abort(400, message="Invalid User or Product")



@bp.route('/cart/<int:user_id>/<int:product_id>')
class Cart(MethodView):

# tested - a route that removes a specific product from a specific user's cart
  
    def delete(self, user_id, product_id):
        product = ProductModel.query.get(product_id)
        user = UserModel.query.get(user_id)
        if user and product:
            cart_items = CartModel.query.filter_by(product_id=product_id).filter_by(user_id=user_id).all()
            if cart_items:
                for cart_item in cart_items:
                    cart_item.delete()
                db.session.commit()
                return {'message': 'Product removed from cart successfully'}, 201
            else:
                return {'message': 'Product is not in the cart'}, 404
        else:
            return {'message': 'Invalid User or Product'}, 400


# tested - retrieve users who have a specified product in their cart
        
@bp.route('/cart/<int:product_id>')
class Cart(MethodView):

    @bp.response(200, UserSchema(many=True))
    def get(self, product_id):
        product = ProductModel.query.get(product_id)
        if not product:
            abort(400, message="Invalid Product")

        products = CartModel.query.filter_by(product_id = product_id).all()

        return [UserModel.query.get(product.user_id) for product in products]    



