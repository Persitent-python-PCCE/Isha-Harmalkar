from config.connection import getConnection
from mappers.productMapper import mapRowToProduct
from models.product import Product
import logging

logger = logging.getLogger(__name__)

class ProductDao:

    def createProduct(self, product: Product):

        query = "INSERT INTO products(category_id, supplier_id, name, unit_price, stock, is_active) VALUES(%s, %s, %s, %s, %s, %s)"

        values = (product.categoryId,
                  product.supplierId,
                  product.name,
                  product.unitPrice,
                  product.stock,
                  product.isActive
                  )

        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

        product.id = cursor.lastrowid

        cursor.close()
        conn.close()
        return product


    def getProductById(self, productId, conn=None):

        shouldCloseConn  = False

        query = "SELECT id, category_id, supplier_id, name, unit_price, stock, is_active FROM products WHERE id=%s"

        if conn is None:
            conn = getConnection()
            shouldCloseConn  = True
        cursor = conn.cursor(dictionary=True)

        cursor.execute(query, (productId,))

        row = cursor.fetchone()
        cursor.close()

        if shouldCloseConn:
            conn.close()

        return mapRowToProduct(row)

    def getProductByName(self, name):
        query = "SELECT id, category_id, supplier_id, name, unit_price, stock, is_active FROM products WHERE name=%s"
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        return mapRowToProduct(row)


    def getAllProducts(self):
        query  = "SELECT id, category_id, supplier_id, name, unit_price, stock, is_active FROM products ORDER BY id"
        conn  = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()


        return [mapRowToProduct(row)
                for row in rows
                ]

    def getAllActiveProducts(self, page=1, pageSize=5):
            offset = (page - 1) * pageSize
            query  = "SELECT id, category_id, supplier_id, name, unit_price, stock, is_active FROM products WHERE is_active = True ORDER BY id LIMIT %s OFFSET %s"
            conn  = getConnection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (pageSize, offset,))
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
    
    
            return [mapRowToProduct(row)
                    for row in rows
                    ]

    def getProductsByCategory(self, categoryId):
        query = "SELECT id, category_id, supplier_id, name, unit_price, stock, is_active FROM products WHERE category_id=%s ORDER BY name"

        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (categoryId,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [
            mapRowToProduct(row)
            for row in rows
        ]

    def getProductsBySupplier(self, supplierId):
        query = "SELECT id, category_id, supplier_id, name, unit_price, stock, is_active FROM products WHERE supplier_id=%s ORDER BY name"
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (supplierId,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [mapRowToProduct(row)
                for row in rows
                ]

    def updateProduct(self, product:Product):
        query  = "UPDATE products SET category_id = %s, supplier_id = %s, name = %s, unit_price = %s, stock = %s, is_active = %s WHERE id = %s"
        values  = (
            product.categoryId,
            product.supplierId,
            product.name,
            product.unitPrice,
            product.stock,
            product.isActive,
            product.id
        )

        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute(query, values)
        conn.commit()
        updated = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return updated

    def deactivateProduct(self, productId):
        query = "UPDATE products SET is_active = FALSE WHERE id = %s"
        conn  = getConnection()
        cursor = conn.cursor()
        cursor.execute(query, (productId,))
        conn.commit()
        deactivated = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return deactivated

    def activateProduct(self, productId):
        query = "UPDATE products SET is_active = TRUE WHERE id = %s"
        conn  = getConnection()
        cursor = conn.cursor()
        cursor.execute(query, (productId,))
        conn.commit()
        activated = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return activated


    def deleteProduct(self, productId):
        query = "DELETE FROM products WHERE id=%s"
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(query, (productId,))
        conn.commit()
        deleted = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return deleted

    def reduceStock(self, productId, qty, conn):
        query = "UPDATE products SET stock = stock - %s WHERE id = %s AND stock >= %s AND is_active = TRUE"

        cursor = conn.cursor()

        cursor.execute(query, (qty, productId, qty))

        updated = cursor.rowcount > 0
        cursor.close()
        return updated


    
    