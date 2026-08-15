from dao.productDao import ProductDao
from dao.categoryDao import CategoryDao
from dao.supplierDao import SupplierDao
from models.product import Product


class ProductService:
    def __init__(self):
        self.productDao = ProductDao()
        self.categoryDao = CategoryDao()
        self.supplierDao = SupplierDao()


    def createProduct(self, product: Product):
        if not product.name or not product.name.strip():
            raise ValueError("Product name cannot be empty")

        if product.unitPrice < 0:
            raise ValueError("Unit price cannot be negative")

        if product.stock < 0:
            raise ValueError("Stock cannot be negative")

        product.name = product.name.strip()

        category = self.categoryDao.getCategoryById(product.categoryId)

        if category is None:
            raise ValueError("Category not found")

        supplier = self.supplierDao.getSupplierById(product.supplierId)
        if supplier is None:
            raise ValueError("Supplier not found")

        existingProduct = self.productDao.getProductByName(product.name)
        if existingProduct:
            raise ValueError("Product Already exists")

        return self.productDao.createProduct(product)


    def getProduct(self, productId):
        product = self.productDao.getProductById(productId)
        if product is None:
            raise ValueError("Product not found")

        return product


    def getAllProducts(self):
        return self.productDao.getAllProducts()

    def getAllActiveProducts(self, page=1, pageSize=5):
        if page < 1:
            raise ValueError("Page must be greater than zero")

        if pageSize <= 0:
            raise ValueError("Page size must be greater than zero.")
        return self.productDao.getAllActiveProducts(page, pageSize)


    def getProductsByCategory(self, categoryId):
        category = self.categoryDao.getCategoryById(categoryId)

        if category is None:
            raise ValueError("Category not found")

        return self.productDao.getProductsByCategory(categoryId)


    def getProductsBySupplier(self, supplierId):
        supplier = self.supplierDao.getSupplierById(supplierId)

        if supplier is None:
            raise ValueError("Supplier not found")


        return self.productDao.getProductsBySupplier(supplierId)


    def updateProduct(self, product:Product):
        if not product.name or not product.name.strip():
            raise ValueError("Product name cannot be empty")

        if product.unitPrice < 0:
            raise ValueError("Unit price cannot be negative")


        if product.stock < 0:
            raise ValueError("Stock cannot be negative")

        existingProduct = self.productDao.getProductById(product.id)

        if existingProduct is None:
            raise ValueError("Product not found")

        product.name = product.name.strip()

        category = self.categoryDao.getCategoryById(product.categoryId)

        if category is None:
            raise ValueError("Category Not found")

        supplier  = self.supplierDao.getSupplierById(product.supplierId)
        if supplier is None:
            raise ValueError("Supplier not found")

        existingName = self.productDao.getProductByName(product.name)
        if(existingName is not None and existingName.id != product.id):
            raise ValueError("Product already exists")

        return self.productDao.updateProduct(product)




    def deactivateProduct(self, productId):
        product = self.productDao.getProductById(productId)
        if product is None:
            raise ValueError("Product not found")

        if not product.isActive:
            raise ValueError("Product is already inactive")

        return self.productDao.deactivateProduct(productId)


    def activateProduct(self, productId):
        product = self.productDao.getProductById(productId)

        if product is None:
            raise ValueError("Product not found")

        if product.isActive:
            raise ValueError("Product is already active")

        return self.productDao.activateProduct(productId)
       

    
