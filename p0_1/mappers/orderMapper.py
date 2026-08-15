from models.order import Order
from models.orderDetail import OrderDetail

def mapRowToOrder(row):
    if row is None:
        return None

    return Order(
        id=row["id"],
        userId=row["user_id"]
    )


def mapOrdersWithDetails( rows):
    if rows is None:
        return None

    orders = {}

    for row in rows:
        orderId = row["order_id"]
        if orderId not in orders:
            order = Order(
                id=row["order_id"],
                userId=row["user_id"],
                createdAt=row["order_created_at"]
            )

            orders[orderId] = {
                "order" : order,
                "details" : [],
                "total" : 0
            }

        detail = OrderDetail(
            orderId=row["order_id"],
            productId=row["product_id"],
            qty=row["qty"],
            unitPriceAtPurchase=row["unit_price_at_purchase"],
            productName=row["product_name"]
        )

        orders[orderId]["details"].append(detail)

        orders[orderId]["total"] += (
            detail.qty * detail.unitPriceAtPurchase
        )

    return list(orders.values())