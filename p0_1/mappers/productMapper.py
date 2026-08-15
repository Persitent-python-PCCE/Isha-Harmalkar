from models.product import Product

def mapRowToProduct(row):
    if row is None:
        return None


    return Product(
        id=row["id"],
        categoryId=row["category_id"],
        supplierId=row["supplier_id"],
        name=row["name"],
        unitPrice=row["unit_price"],
        stock=row["stock"],
        isActive=row["is_active"]
    )