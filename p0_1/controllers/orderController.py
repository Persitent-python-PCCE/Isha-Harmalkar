from services.orderService import OrderService

class OrderController:
    def __init__(self):
        self.orderService = OrderService()

    def checkout(self, cart):
        print("---------CheckOut--------")

        if cart.isEmpty():
            print("Car is empty")
            return

        total = 0

        for item in cart.items:
            subtotal  = (item.unitPriceAtPurchase * item.qty)

            total += subtotal

            print(f"Product Id: {item.productId} |" f"Qty: {item.qty}"f"Price: {item.unitPriceAtPurchase} |"f"Subtotal: {subtotal}")

            print("-------------------------------")
            print("Total: ", total)

            confirm = input("Confirm order? (Y/N): ")

            if confirm.lower() != "y":
                print("Checkput cancelled.")
                return

            try:
                order = self.orderService.checkOut(cart)
                print("Order placed successfully")
                print("Order ID: ", order.id)
                print("Total: ", total)

            except ValueError as err:
                print("Checkout failed: ", err)

            except Exception as err:
                print("Unexcepted error durring checkout: ", err)


    def getUserOrders(self, userId):

        #userId = input("Enter user id: ")    

        try:
            #userId = int(userId)
            orders = self.orderService.getUserOrders(userId)

            if not orders:
                print("You have no orders")
                return

            print("-----My Orders---------")

            for data in orders:
                order = data["order"]
                details = data["details"]
                total = data["total"]

                self.printOrder(order, details, total, showUser=False)
        except ValueError as verr:
            print("Invalid user Id: ", verr)

        except Exception as err:
            print("Error Fetching orders: ", err)



    def getAllOrders(self):
        try:
            orders = self.orderService.getAllOrders()

            if not orders:
                print("No orders found")

                return

            for data in orders:
                order = data["order"]
                details = data["details"]
                total = data["total"]

                self.printOrder(order, details, total, showUser=True)

        except Exception as err:
            print("Error fetching orders: ", err)


    def printOrder(self, order, details, total, showUser=False):
        print("---------------------------------")
        print("Order Id: ", order.id)

        if showUser:
            print("User Id : ", order.userId)

        print("Date   :", order.createdAt)
        print("----------------------")

        for detail in details:
            subtotal = (detail.qty * detail.unitPriceAtPurchase)

            productName = getattr(detail, "productName", f"Product{detail.productId}")

            print(f"Product : {productName}\n"
                    f"Quantity : {detail.qty}\n"
                    f"Price    : {detail.unitPriceAtPurchase}\n"
                    f"Subtotal : {subtotal}\n"

                    )
            print("-------------------------------------")

            print(f"TOTAL             :{total}")
            print("-------------------------------------------")