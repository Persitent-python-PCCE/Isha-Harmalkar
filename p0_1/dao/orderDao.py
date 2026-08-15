from config.connection import getConnection
from mappers.orderMapper import mapRowToOrder


class OrderDao:
    def createOrder(self, order, conn):

        query = "INSERT INTO orders(user_id) VALUES(%s)"
        cursor = conn.cursor()
        cursor.execute(query, (order.userId,))

        order.id = cursor.lastrowid
        cursor.close()
        return order

    def getOrderById(self, orderId):

        query = "SELECT id, user_id, created_at, updated_at FROM orders WHERE id=%s"
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return mapRowToOrder(row)

    def getOrderByUser(self, userId):
        query = "SELECT id, user_id, created_at, updated_at FROM orders where user_id = %s ORDER BY created_at DESC"
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return [
            mapRowToOrder(row)
            for row in rows
        ]


    def getUserOrdersWithDetails(self, userId):

        query = "SELECT o.id AS order_id, o.user_id, o.created_at AS order_created_at, o.updated_at as order_updated_at, od.product_id, p.name AS product_name,od.qty, od.unit_price_at_purchase FROM orders o JOIN order_details od ON o.id = od.order_id JOIN products p ON od.product_id = p.id WHERE o.user_id = %s ORDER BY o.created_at DESC, od.product_id"

        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (userId, ))

        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def getAllOrdersWithDetails(self):
        query = "SELECT o.id AS order_id, o.user_id, o.created_at AS order_created_at, o.updated_at AS order_updated_at, od.product_id, p.name AS product_name, od.qty, od.unit_price_at_purchase FROM orders o JOIN order_details od ON o.id  = od.order_id JOIN products p ON od.product_id= p.id ORDER BY o.created_at DESC, od.product_id"

        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
