from models.orderDetail import OrderDetail

def mapRowToOrderDetail(row):
    if row is None:
        return None

    return OrderDetail(
        orderId=row["order_id"],
        product=row["product_id"],
        productId=row["product_id"],
        qty=row["qty"],
        unitPriceAtPurchase=row["unit_price_at_purchase"]
    )