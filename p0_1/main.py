from config.connection import getConnection

from config.logger import setupLogging
from controllers import supplierController
from controllers.categoryController import CategoryController
from controllers.productController import ProductController
from controllers.supplierController import SupplierController
from controllers.userController import UserController
from menus.adminMenu import AdminMenu
from models.cart import Cart
from controllers.cartController import CartController
from controllers.orderController import OrderController

from menus.userMenu import UserMenu

""" userController = UserController()
user = userController.register()
user = userController.updateUser()

user= userController.getAllUsers()
user = userController.getUser()
user = userController.deleteUser()
 """


""" categoryController = CategoryController()
categoryController.createCategory()
categoryController.getAllCategories()
categoryController.getCategoryById()
categoryController.updateCategory()
categoryController.deleteCategory() """



""" supplierController = SupplierController()
supplierController.createSupplier()
supplierController.getAllSuppliers()
supplierController.getSupplierById()
supplierController.updateSupplier()
supplierController.deleteSupplier() """


""" productController = ProductController()
productController.createProduct()
productController.updateProduct()
productController.getAllProducts()
productController.getProductById()
productController.getProductByCategory()
productController.getProductBySupplier()
productController.deactivateProduct()
productController.activateProduct()
 """


""" cart = Cart(1)
cartController = CartController()
cartController.addProduct(cart)
cartController.addProduct(cart)
cartController.addProduct(cart)
cartController.addProduct(cart)
cartController.displayCart(cart)
cartController.updateQuantity(cart)
cartController.displayCart(cart)
cartController.removeProduct(cart)
cartController.displayCart(cart) """


""" userId = 2

cart = Cart(userId)

cartController  = CartController()
orderController  = OrderController()
productController = ProductController() """


""" user1 = 1
user2  = 2 """

""" orderController.getUserOrders(user1)
orderController.getUserOrders(user2) """


#orderController.getAllOrders()
#orderController.getOrderById()





setupLogging()


while True:
    userController = UserController()

    print("ECOMMERCE SYSTEM")
    print("1. Register as User")
    print("2. Login As User")
    print("3. Login As Admin")
    print("4. Exit")
    choice = input("Enter Choice: ").strip()

    if choice == "1":
        user = userController.register()

        if user:
            print("Registration Successful")
            print("You can now login")

    elif choice  == "2":
        user = userController.login()
        if user:
            userMenu = UserMenu(user)
            userMenu.show()

    elif choice == "3":
        

        admin = userController.login(loginAsAdmin = True)
        if admin:
            adminMenu  = AdminMenu(admin)
            adminMenu.show()

    elif choice == "4":
        print("Thank you for your time")
        break
    else:
        print("INVALID CHOICE")


            




