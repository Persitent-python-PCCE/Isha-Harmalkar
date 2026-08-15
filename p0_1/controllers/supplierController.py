from services.supplierService import SupplierService
from models.supplier import Supplier


class SupplierController:

    def __init__(self):
        self.supplierService = SupplierService()

    def printSupplier(self, supplier):
        print(f"ID:                  {supplier.id}")
        print(f"Company:             {supplier.companyName}")
        print(f"Contact Name:         {supplier.contactName}")
        print(f"Contact Designation:       {supplier.contactDesignation}")

        print(f"City:          {supplier.city}")
        print(f"Contact No:    {supplier.contactNo}")


    def createSupplier(self):
        print("----------------------Create Supplier-------------")
        companyName = input("Company Name: ")
        contactName = input("Contact Name: ")
        contactDesignation = input("Contact Designation: ")
        city = input("City: ")
        contactNo = input("Contact Number: ")


        supplier = Supplier(
            companyName=companyName,
            contactName=contactName,
            contactDesignation=contactDesignation,
            city=city,
            contactNo=contactNo
        )

        try:
            supplier = self.supplierService.createSupplier(supplier)
            print("Supllier created successfully")
            self.printSupplier(supplier)
            return supplier

        except ValueError as err:
            print(f"Creating Supplier Failed: ",err)

        return None

    def getSupplierById(self):
        supplierId  = input("Enter supplier ID: ")
        try:
            supplierId = int(supplierId)
            supplier = self.supplierService.getSupplierById(supplierId)
            print("---------Supplier---------------")
            self.printSupplier(supplier)
            return supplier

        except ValueError as err:
            print("Getting supplier failed: ", err)

        return None


    def getAllSuppliers(self):
        try:
            suppliers = self.supplierService.getAllSuppliers()

            if not suppliers:
                print("No suppliers found")
                return []

            print("------------Suppliers----------")

            for supplier in suppliers:
                self.printSupplier(supplier)
                print("------------------------------------------")

            return suppliers

        except ValueError as err:
            print("Could not get all suppliers: ", err)

        return []


    def updateSupplier(self):
        print("-------Update Supplier-------------------")
        supplierId = input("Supplier Id: ")
        companyName  = input("Company Name: ")
        contactName = input("Contact Name: ")
        contactDesignation = input("Contact Designation: ")
        city = input("City: ")
        contactNo = input("Contact number: ")

        try:
            supplierId  = int(supplierId)
            supplier = Supplier(
                id=supplierId,
                companyName=companyName,
                contactName=contactName,
                contactDesignation=contactDesignation,
                city=city,
                contactNo=contactNo
            )
            updated = self.supplierService.updateSupplier(supplier)

            if updated:
                print("Supplier updated succcessfully")
                self.printSupplier(supplier)
            else:
                print("Supplier was not updated")

            return updated

        except ValueError as err:
            print("Could not update supplier: ", err)

        return False



    def deleteSupplier(self):

        print("------------Delete Supplier -----------")
        supplierId = input("Supplier Id: ")
        try:
            supplierId = int(supplierId)
            confirm = input("Are you sure you want to delete this supplier? (yes or no): ")

            if confirm.lower() != "yes":
                print("Deletion Cancelled")
                return False
            deleted = self.supplierService.deleteSupplier(supplierId)

            if deleted:
                print("Supplier deleted successfully")
            else:
                print("Supplier was not deleted")

            return deleted

        except ValueError as err:
            print("Could not delete supplier: ", err)

        return False

