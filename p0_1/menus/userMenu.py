from controllers.productController import ProductController
from controllers.userController import UserController
from models.cart import Cart
from controllers.cartController import CartController
from controllers.orderController import OrderController




class UserMenu:
    def __init__(self, user):
        self.user = user
        self.cartController  = CartController()
        self.orderController  = OrderController()
        self.productController = ProductController()       

    def show(self):

        cart = Cart(self.user.id)          


        while True:
            print("----------WELCOME----------------")
            print("1. View Products")
            print("2. Add Product to Cart")
            print("3. View Cart")
            print("4. Update Cart Qty")
            print("5. Remove From Cart")
            print("6. Checkout")
            print("7. Get Order History")
            print("8. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.productController.getAllActiveProducts()

            elif choice == "2":
                self.cartController.addProduct(cart)

            elif choice == "3":
                self.cartController.displayCart(cart)

            elif choice == "4":
                self.cartController.updateQuantity(cart)

            elif choice == "5":
                self.cartController.removeProduct(cart)

            elif choice == "6":
                self.orderController.checkout(cart)                

            elif choice =="7":
                self.orderController.getUserOrders(self.user.id)
            elif choice == "8":
                print("Thank you..")
                break
            else:
                print("Invalid choice")

