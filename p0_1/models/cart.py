from models.orderDetail import OrderDetail

class Cart:
    def __init__(self, userId):
        self.userId = userId
        self.items = []

    def addItem(self, orderDetail):
        self.items.append(orderDetail)     

    def removeItem(self, productId):
        for item in self.items:
            if item.productId == productId:
                self.items.remove(item)
                return True

        return False


    def clear(self):
        self.items.clear()

    def isEmpty(self):
        return len(self.items) == 0


    