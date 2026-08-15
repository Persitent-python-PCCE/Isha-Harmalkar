from venv import logger

from config.logger import safeRun
from services.productService import ProductService
from models.product import Product


class ProductController:

    def __init__(self):
        self.productService = ProductService()


    def printProduct(self, product: Product):
        print(f"ID: {product.id}")
        print(f"Category: {product.categoryId}")
        print(f"Supplieer: {product.supplierId}")
        print(f"Name: {product.name}")
        print(f"Unit Price: {product.unitPrice}")
        print(f"Stock: {product.stock}")
        print(f"isActive: {product.isActive}")

    @safeRun
    def createProduct(self):
        print("---------Create Product --------")

        categoryId = input("Category Id: ")
        supplierId = input("Supplier Id: ")
        name = input("Product Name: ")
        unitPrice = input("Unit Price: ")
        stock = input("Stock: ")
        isActive = input("Keep Product as Active, (Y/N): ")


        try:
            categoryId = int(categoryId)
            supplierId = int(supplierId)
            unitPrice = float(unitPrice)
            stock = int(stock)
            isActive = True if isActive.lower() == "y" else False

            product = Product(
                categoryId=categoryId,
                supplierId=supplierId,
                name=name,
                unitPrice=unitPrice,
                stock=stock,
                isActive=isActive
            )

            product = self.productService.createProduct(product)
            self.printProduct(product)
            logger.info("Product created: id={product.id}, name={product.name}")
            return product

        except ValueError as err:
            print("Could not create product: ", err)
            logger.exception(f"Could Not  create product: {product.name} because of: {err}")
        except Exception as e:
            print("Unexcpecte error: ", e)
            logger.exception(f"Failed to create product: {product.name} because of: {err}")


        return None

    @safeRun
    def getProductById(self):
        productId = input("Enter product Id: ")

        try:
            productId = int(productId)
            product = self.productService.getProduct(productId)

            print("-------Product--------")
            self.printProduct(product)
            logger.info("Get Product By Id: id={product.id}, name={product.name}")



            return product
        except ValueError as err:
            print("Failed to get Product: ", err)
            logger.exception(f"Failed to get product: {product.id} because of: {err}")


        return None

    @safeRun
    def getAllProducts(self):

        try:
            products = self.productService.getAllProducts()

            if not products:
                print("No products found")
                return []

            print("-------Products------------")
            for p in products:
                self.printProduct(p)
                print("-------------------------------")

            logger.info("Get All Products")


            return products

        except ValueError as err:
            print("Failed to get products: ", err)
            logger.exception(f"Failed to getall  product because of: {err}")




        return []

    
    def getAllActiveProducts(self):
        page = 1
        pageSize = 5

        while True:
    
            try:
                products = self.productService.getAllActiveProducts(page, pageSize)

                if not products:
                    if page == 1:
                        print("No products found")
                        return []
                    print("You are on the last page.")
                    page -= 1
                    input("Press enter to conitnue")
                    continue
                    

                print()

                print(f"-----------------PRODUCTS - PAGE {page}-------------")
                print("-------------------------------")

                for p in products:
                    self.printProduct(p)
                    print("-------------------------------")

                print("N - Next Page")
                print("P - Prev Page")
                print("B - Back")

                choice  = input("Enter Choice: ").strip().lower()

                if choice == "n":
                    page += 1
                    #nextProducts = self.productService.getAllActiveProducts(page + 1, pageSize)

                    
                elif choice == "p":
                    if page == 1:
                        print("Already on the first page.")
                    else:
                        page -= 1

                elif choice == "b":
                    logger.info("Get All Active Products")
                    return
                else:
                    print("Invalid Choice")

            except ValueError as err:
                print("Failed to get products", err)
                logger.exception(f"Failed to get all  ACTIVE product because of: {err}")

                break
            


                


            

    
    
    @safeRun
    def updateProduct(self):
        print("----------Update Product------------")
        productId  = input("Product Id: ")
        categoryId = input("Category Id: ")
        supplierId = input("Supplier Id: ")
        name = input("Product name: ")
        unitPrice = input("Unit price: ")
        stock = input("Stocck: ")
        isActive = input("Activate? yes or no: ")


        try:
            productId = int(productId)
            categoryId = int(categoryId)
            supplierId = int(supplierId)
            unitPrice = float(unitPrice)
            stock = int(stock)
            isActive = isActive.lower() == "y"

            product = Product(
                id=productId,
                categoryId=categoryId,
                supplierId=supplierId,
                name=name,
                unitPrice=unitPrice,
                stock=stock,
                isActive=isActive
            )

            updated = self.productService.updateProduct(product)

            if updated:
                print("Product updated successfully")
                self.printProduct(product)
            else:
                print("Product was not updated")

            return updated
        except ValueError as err:
            print("Failed to update product: ", err)

        return False


    @safeRun
    def getProductByCategory(self):

        categoryId = input("Enter ccategory Id: ")
        try:
            categoryId = int(categoryId)
            products = self.productService.getProductsByCategory(categoryId)

            if not products:
                print("No products found for this category.")
                return []

            print("-------Products----------")

            for p in products:
                self.printProduct(p)
                print("--------------------")

            return products

        except ValueError as err:
            print("Failed to get products by category: ", err)

        return []


    @safeRun
    def getProductBySupplier(self):
    
        supplierId = input("Enter supplier Id: ")
        try:
            supplierId = int(supplierId)
            products = self.productService.getProductsBySupplier(supplierId)

            if not products:
                print("No products found for this supplier.")
                return []

            print("-------Products----------")

            for p in products:
                self.printProduct(p)
                print("--------------------")

            return products

        except ValueError as err:
            print("Failed to get productst by supplier: ", err)

        return []
    

    @safeRun
    def deleteProduct(self):
        pass


    @safeRun
    def deactivateProduct(self):
        print("--------Deactivate Product --------")
        productId = input("Product Id: ")
        try:
            productId = int(productId)
            confirm = input("Are you sure you want to deactivate this product? (Y/ N): ")

            if confirm.lower() != "y":
                print("Deactivation Cancelled")
                return False

            deactivated = self.productService.deactivateProduct(productId)


            if deactivated:
                print("Product Deactived successfully")

            else:
                print("Product was not deactivated")

            return deactivated

        except ValueError as err:
            print("Failed to deactivate: ", err)

        return False


    @safeRun
    def activateProduct(self):
        print("--------Activate Product --------")
        productId = input("Product Id: ")
        try:
            productId = int(productId)

            
            activated = self.productService.activateProduct(productId)


            if activated:
                print("Product Actived successfully")

            else:
                print("Product was not Activated")

            return activated

        except ValueError as err:
            print("Failed to Activate: ", err)

        return False



