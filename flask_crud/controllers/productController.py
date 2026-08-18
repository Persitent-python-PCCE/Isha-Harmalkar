from flask import Blueprint, request, jsonify

from dao.productDao import ProductDao
import dao
from services.productService import ProductService

productController = Blueprint("productController", __name__)
productService = ProductService(ProductDao())


@productController.route("/products", methods=["GET"])
def getProducts():
    try:
        products = productService.getAllProducts()

        return jsonify([product.toDict() for product in products]), 200

    except Exception as e:
        return jsonify({"error" : str(e)}), 400


@productController.route("/products/<int:id>", methods=["GET"])
def getProductById(id):
    try:
        print("prdt id: ", id)
        product = productService.getProductById(id)
        print("Product is ", product)
    
     

        return jsonify({
            "message" : "product retrieved successfully",
            "product" : product.toDict()
        }), 200
    except ValueError as ve:
        return jsonify({"error" : str(ve)}), 400
    except Exception as e:
        return jsonify({"error" : str(e)}), 400



@productController.route("/products", methods=["POST"])
def createProduct():
    data = request.get_json()
    try:
        product  = productService.createProduct(data)
        return jsonify({
            "message": "product created",
            "product": product.toDict()
        }), 201

    except Exception as e:
        return jsonify({"error" : str(e)}), 400


@productController.route("/products/<int:p_id>", methods=["PUT"])
def updateProduct(p_id):
    #id = request.args.get("id")
    data = request.get_json()
    try:
        product = productService.updateProduct(p_id, data)
        return jsonify({
            "message" : "product updated",
            "product" : product.toDict()
        }), 201

    except Exception as e:
        return jsonify({"error" : str(e)}), 400


@productController.route("/products/<int:p_id>", methods=["DELETE"])
def deleteProduct(p_id):
    #id = request.args.get("id")
    try:
        res = productService.deleteProduct(p_id)
        return jsonify({
                    "message" : "product deleted"
                    
                }), 200



    except Exception as e:
        return jsonify({"error" : str(e)}), 400







    
