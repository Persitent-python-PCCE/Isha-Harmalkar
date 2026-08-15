from models.orderDetail import OrderDetail
from dao.productDao import ProductDao


class CartService:


    def __init__(self):
        self.productDao = ProductDao()

    def addProduct(self, cart, productId, qty):
        if qty <= 0:
            raise ValueError("Quantity must be greater than zero")

        product = self.productDao.getProductById(productId)

        if product is None:
            raise ValueError("Product not found")

        if not product.isActive:
            raise ValueError("Product is inactive")

        if product.stock <= 0:
            raise ValueError("Product is out of stock")

        for item in cart.items:
            if item.productId == productId:
                newQty = item.qty + qty


                if newQty > product.stock:
                    raise ValueError("Only ", product.stock, "units avaliable")

                item.qty = newQty
                return item

        if qty > product.stock:
            raise ValueError("Only ", product.stock, "units avaliable")

        orderDetail = OrderDetail(
            productId=product.id,
            unitPriceAtPurchase=product.unitPrice,
            qty=qty
        )

        cart.addItem(orderDetail)
        return orderDetail

    def removeProduct(self, cart, productId):
        removed = cart.removeItem(productId)

        if not removed:
            raise ValueError("Product not found in cart")

        return True


    def updateQuantity(self, cart, productId, qty):
        if qty <= 0:
            raise ValueError("Quantity must be greater than zero")

        product = self.productDao.getProductById(productId)

        if product is None:
            raise ValueError("Product not found")

        if not product.isActive:
            raise ValueError("Product is inactive")

        if qty > product.stock:
            raise ValueError("Only ", {product.stock}, "units available")

        for item in cart.items:
            if item.productId == productId:
                item.qty = qty
                return item

        raise ValueError("Product not found in cart")


    def getTotal(self, cart):
        total = 0

        for item in cart.items:
            total += (item.unitPriceAtPurchase * item.qty) 

        return total

    def clearCart(self, cart):
        cart.clear()