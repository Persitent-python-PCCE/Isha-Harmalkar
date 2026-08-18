from models.product import Product


class ProductService:
    def __init__(self, productDao):
        self.productDao  = productDao

    def getAllProducts(self):
        return self.productDao.getAllProducts()

    def getProductById(self, id):
        product =  self.productDao.getProductById(id)
        if product is None:
            raise ValueError("product not found")

        return product


    def getProductByName(self, name):
        return self.productDao.getProductByName(name)

    def createProduct(self, data):
        product = Product(
            name=data["name"],
            category=data["category"],
            price=data["price"],
            quantity=data["quantity"],
            description=data.get("description")

        )
        print("prdt service create data:", data)
        return self.productDao.saveProduct(product)



    def updateProduct(self,p_id,  data):
        print("prdt id: ", p_id, "prdt service data: ", data)

        exists = self.productDao.getProductById(p_id)
        

        if not exists:
            raise ValueError("product does not exist. Cannot update unexisitng product.")

        print("product exits")
        

        return self.productDao.updateProduct(p_id, data)

    def deleteProduct(self, p_id):
        product  = self.productDao.getProductById(p_id)
        print("del ser product id", p_id)
        if not product:
            raise ValueError("product does not exists, hence cannot be deleted.")

        return self.productDao.deleteProduct(product)

