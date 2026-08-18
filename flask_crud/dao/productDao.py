from sqlalchemy import delete

from models.product import Product
from config.database import db

class ProductDao:

    def getAllProducts(self):
        return Product.query.all()


    def getProductById(self, id):
        return Product.query.get(id)

    def getByName(self, name):
        products = db.session.execute(
            db.select(Product).where(Product.name == name).scalara().first()
        )
        return products

    def saveProduct(self, product):
        print("prdt dao create: ", product)
        db.session.add(product)
        db.session.commit()
        return product


    def updateProduct(self, p_id, data):
            print("prdt dao update data: ", data)
            product = Product.query.get(p_id)
            product.id = p_id
            product.name = data["name"]
            product.price = data["price"]
            product.quantity = data["quantity"]
            product.category = data["category"]
            db.session.commit()
            return product


    def deleteProduct(self, product):
       
        db.session.delete(product)
        db.session.commit()
        return True


