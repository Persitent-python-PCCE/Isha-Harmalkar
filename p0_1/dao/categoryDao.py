from config.connection import getConnection
from mappers.categoryMapper import mapRowToCategory



class CategoryDao:



    def createCategory(self, category):

        query = "INSERT INTO categories(name) VALUES(%s)"

        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute(query, (category.name,))
        conn.commit()

        category.id = cursor.lastrowid

        cursor.close()
        conn.close()

        return category


    def getCategoryById(self, categoryId):
        query = "SELECT id, name FROM categories WHERE id=%s"
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(query, (categoryId,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()


        return mapRowToCategory(row)


    def getCategoryByName(self, name):
        query = "SELECT id, name FROM categories WHERE name = %s"
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        return mapRowToCategory(row)


    def getAllCategories(self):
        query = "SELECT id, name FROM categories ORDER BY name"

        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [
            mapRowToCategory(row)
            for row in rows
        ]

    def updateCategory(self, category):
        query = "UPDATE categories SET name=%s WHERE id=%s"
        values = (category.name, category.id)


        conn = getConnection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(query, values)
        conn.commit()
        updated = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return updated


    def deleteCategory(self, categoryId):
        query = "DELETE FROM categories WHERE id=%s"

        
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(query, (categoryId,))

        conn.commit()
        deleted = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return deleted
