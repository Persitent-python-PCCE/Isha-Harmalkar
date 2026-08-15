from services.cartService import CartService
from models.cart import Cart


class CartController:

    def __init__(self):
        self.cartService = CartService()


    def displayCart(self, cart):
        if cart.isEmpty():
            print("Cart is empty")
            return

        print("-----------CART-----------")

        for item in cart.items:
            subtotal = item.unitPriceAtPurchase * item.qty

            print("Product Id : ", item.productId)
            print("Quantity   : ", item.qty)
            print("Unit Price : ", item.unitPriceAtPurchase)
            print("Subtotal   : ", subtotal)
            print("-------------------------------")

        total = self.cartService.getTotal(cart)
        print("TOTAL      :", total)
        print("------------------------------------------------")


    def addProduct(self, cart):
        print("------------------Add Product --------------------")
        try:
            productId = int(input("Product Id: "))
            qty = int(input("Quantity: "))

            item = self.cartService.addProduct(
                cart, productId, qty
            )

            print("Product added to cart")
            print("Product ID: ", item.productId)
            print("Quantity  : ", item.qty)

        except ValueError as err:
            print(" Could not add product to cart: ", err)


    def removeProduct(self, cart):
        print("-------Remove Product -------")
        try:
            productId = int(input("Product Id: "))

            self.cartService.removeProduct(cart, productId)
            print("Product removed from cart")

        except ValueError as err:
            print("Could not remove product: ", err)



    def updateQuantity(self, cart):
        print("---------Update Quantity-----------------")

        try:
            productId = int(input("Product Id: "))
            qty = int(input("New Quantity: "))

            item = self.cartService.updateQuantity(cart, productId, qty)

            print("Quantity updated")
            print("Product Id: ", item.productId)
            print("Quantity  : ", item.qty)

        except ValueError as err:
            print("Could not update quantity: ", err)

            

            

    