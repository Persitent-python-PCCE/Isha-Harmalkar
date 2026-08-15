from config.connection import getConnection
from mappers.orderDetailMapper import mapRowToOrderDetail
from models.orderDetail import OrderDetail

class OrderDetailDao:

    def createOrderDetail(self, orderDetail: OrderDetail, conn):

        query = "INSERT INTO order_details(order_id, product_id, qty, unit_price_at_purchase) VALUES(%s, %s, %s, %s)"

        cursor = conn.cursor()
        cursor.execute(query, (orderDetail.orderId, orderDetail.productId, orderDetail.qty,orderDetail.unitPriceAtPurchase))

        cursor.close()
        return orderDetail


    def getOrderDetails(self, orderId):

        query = "SELECT order_id, product_id, qty, unit_price_at_purchase, created_at, updated_at FROM order_details WHERE order_id = %s"

        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (orderId,))
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return [
            mapRowToOrderDetail(row)
            for row in rows
        ]






