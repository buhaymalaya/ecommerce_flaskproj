# from flask.views import MethodView
# from flask_smorest import abort

# from flask_jwt_extended import jwt_required

# from . import bp
# from schemas import ProdCartSchema
# from models.prod_cart_model import ProdCartModel

# @bp.route('/prodcart')
# class ProdCartList(MethodView):
    
#     @bp.arguments(ProdCartSchema)
#     def post(self, prodcart_data):

#         try:
#             product = ProdCartModel()
#             product.from_dict(prodcart_data)

#             product.save_prodcart()

#             return product
#         except:
#             abort(400, message=f"{product.title} failed to add")

# # - A route that shows a list of all available products

#     @bp.response(200, ProdCartSchema(many=True))
#     def get(self):
#         return ProdCartModel.query.all()

# @bp.route('/prodcart/<product_id>')
# class ProdCart(MethodView):

# # - A route which shows a single product (with the information of the product you just requested)

#     @bp.response(200, ProdCartSchema)
#     def get(self, product_id):
#         try: 
#             return ProdCartModel.query.get(product_id)
#         except:
#             abort(400, message="Product not found")

#     @bp.arguments(ProdCartSchema)
#     @bp.response(201, ProdCartSchema)
#     def put(self, product_data, product_id):
            
#         print(product_data)
#         product = ProdCartModel.query.get(product_id)
#         if not product:
#             abort(400, message="Product not found")
#         product.save_prodcart()
#         return product

#     def delete(self, product_id):

#         product = ProdCartModel.query.get(product_id)
#         if not product:
#             abort(400, message="Product not found")
        
#         product.del_prodcart()
#         return {'Message': f'Product: {product} deleted'}, 200

