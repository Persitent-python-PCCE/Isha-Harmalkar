from config.connection import getConnection
from models.user import User
from mappers.userMapper import mapRowToUser

class UserDao:

    """     def __init__(self):
        self.conn = getConnection() """

    def createuser(self, user):
        conn = getConnection()
        cursor = conn.cursor()

        query = "INSERT INTO users (name, email, password, is_admin) VALUES (%s,%s,%s,%s)" 
        values = (user.name, user.email, user.password, user.isAdmin)

        cursor.execute(query, values)
        conn.commit()
        user.id = cursor.lastrowid
        cursor.close()
        conn.close()

        return user


    def getUserById(self, userId):
        conn = getConnection()
        #cursor = conn.cursor()

        query = "SELECT id, name, email, password, is_admin FROM users WHERE id=%s" 
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (userId,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()



        if row is None:
            return None

        
        return mapRowToUser(row)

    def getUserByEmail(self, email):
        query = "SELECT id, name, email, password, is_admin FROM users WHERE email = %s"
        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (email,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()


        if row is None:
            return None

        
        return mapRowToUser(row)




    def getAllUsers(self):
        query = "SELECT id, name, email, password, is_admin FROM users"
        conn = getConnection()
        cursor  = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [
            mapRowToUser(row) for row in rows
        ]


    def updateUser(self, user):
        query = "UPDATE users SET name=%s,email=%s,password=%s,is_admin=%s WHERE id=%s"
        values = (user.name, user.email, user.password, user.isAdmin, user.id)

        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute(query, values)
        conn.commit()

        updated = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return updated


    def deleteUser(self, userId):
        query = "DELETE FROM users WHERE id=%s"
        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute(query, (userId,))
        conn.commit()
        deleted = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return deleted
        

    
        


    
