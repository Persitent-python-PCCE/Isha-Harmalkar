from models.cart import Cart
from models.order import Order
from models.orderDetail import OrderDetail

from dao.orderDao import OrderDao
from dao.orderDetailDao import OrderDetailDao
from dao.productDao import ProductDao
from config.connection import getConnection

from mappers.orderMapper import mapOrdersWithDetails

class OrderService:

    def __init__(self):
        self.orderDao = OrderDao()
        self.orderDetailDao = OrderDetailDao()
        self.productDao = ProductDao()

    def checkOut(self, cart:Cart):
        if cart.isEmpty():
            raise ValueError("Cannor checkout an empty cart")

        conn = getConnection()

        try:

            conn.start_transaction()

            for item in cart.items:
                product = self.productDao.getProductById(item.productId, conn)

                if product is None:
                    raise ValueError("Product ", item.productId, "not found")

                if not product.isActive:
                    raise ValueError("Product ", product.name, "is inactive")

                if item.qty > product.stock:
                    raise ValueError("Insufficient stock for ", product.name, ". \nAvailable: ", product.stock)

                order = Order(userId=cart.userId)


                self.orderDao.createOrder(order, conn)

                for item in cart.items:

                    orderDetail = OrderDetail(
                        orderId=order.id,
                        productId=item.productId,
                        qty=item.qty,
                        unitPriceAtPurchase=item.unitPriceAtPurchase
                    )


                    self.orderDetailDao.createOrderDetail(
                        orderDetail,
                        conn
                    )

                    updated = self.productDao.reduceStock(
                        item.productId,
                        item.qty,
                        conn
                    )

                    if not updated:
                        raise ValueError("Unable to update stock for product ", item.productId)

                conn.commit()
                cart.clear()
                return order

        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close() 


    def getUserOrders(self, userId):
        rows = self.orderDao.getUserOrdersWithDetails(userId)

        return mapOrdersWithDetails(rows)

    def getAllOrders(self):
        rows = self.orderDao.getAllOrdersWithDetails()
        return mapOrdersWithDetails(rows)