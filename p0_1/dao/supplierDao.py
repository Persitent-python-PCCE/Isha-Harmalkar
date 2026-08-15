from config.connection import getConnection
from mappers.supplierMapper import mapRowToSupplier


class SupplierDao:

    def createSupplier(self, supplier):
        query = "INSERT INTO suppliers(company_name, contact_name,contact_designation,city,contact_no) VALUES(%s, %s, %s, %s, %s)"

        values = (supplier.companyName, supplier.contactName, supplier.contactDesignation, supplier.city, supplier.contactNo)

        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        supplier.id = cursor.lastrowid

        cursor.close()
        conn.close()

        return supplier


    def getSupplierById(self, supplierId):
        query = "SELECT id, company_name, contact_name, contact_designation, city, contact_no FROM suppliers WHERE id=%s"

        conn = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (supplierId,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        return mapRowToSupplier(row)

    def getSupplierByCompanyName(self, companyName):
        query = "SELECT id, company_name, contact_name, contact_designation, city, contact_no FROM suppliers WHERE company_name=%s"
        conn  = getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (companyName,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()


        return mapRowToSupplier(row)

    def getAllSuppliers(self):
        query = "SELECT id, company_name, contact_name, contact_designation, city, contact_no FROM suppliers ORDER BY company_name"
        conn = getConnection()
        cursor  = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [
            mapRowToSupplier(row)
            for row in rows
        ]

    def updateSupplier(self, supplier):
        query = "UPDATE suppliers SET company_name=%s, contact_name=%s,contact_designation=%s,city=%s,contact_no=%s WHERE id = %s"

        values  = (
            supplier.companyName,
            supplier.contactName, 
            supplier.contactDesignation,
            supplier.city,
            supplier.contactNo,
            supplier.id
        )

        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute(query, values)
        conn.commit()

        updated = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return updated


    def deleteSupplier(self, supplierId):
        query = "DELETE FROM suppliers WHERE id=%s"
        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute(query, (supplierId,))
        conn.commit()

        deleted = cursor.rowcount > 0
        cursor.close()
        conn.close()

        return deleted

    

    

