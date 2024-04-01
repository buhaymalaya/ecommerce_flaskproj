from flask import Blueprint, jsonify
from flask.views import MethodView
from app import db
from schemas import ProductSchema
from models.product_model import ProductModel
from flask_smorest import abort
from . import bp

# - A route that shows a list of all available products

@bp.route('/product')
class ProductList(MethodView):

    @bp.response(200, ProductSchema(many=True))
    def get(self):
        # try:
            # Query all products from the database
        products = ProductModel.query.all()
        return products
        # except:
        #     abort(400, message="Please try again")

    # add product to database
    @bp.arguments(ProductSchema)
    @bp.response(201, ProductSchema)
    def post(self, data):
        try:
            existing_prod = ProductModel.query.filter_by(title=data['title']).first()
            if existing_prod:
                abort(400, message="Title already exists; please try a different one.")

            product = ProductModel()
            product.from_dict(data)
            product.save_product()
            
            return product
        
        except Exception:
            abort(500, message="Unexpected error; please try again.")

# - A route which shows a single product (with the information of the product you just requested)

@bp.route('/product/<int:id>')
class Product(MethodView):
    @bp.response(200, ProductSchema)
    def get(self, id):
    
        product = ProductModel.query.get(id)

        # Check if the product exists
        if product:
            return product
        else:
            abort(400, error='Product not found')

    @bp.arguments(ProductSchema)
    @bp.response(200, ProductSchema)
    def put(self, data, id):
        product = ProductModel.query.get(id)
        if product:
            product.from_dict(data)
            product.save_product()
            return product
        else:
            abort(400, message="Not a valid product")

    def delete(self, id):
        product = ProductModel.query.get(id)
        if product:
            product.del_product()
            return { "Message": "Product deleted"}, 200
        abort(400, message="Not a valid product")