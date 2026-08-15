from dao.supplierDao import SupplierDao



class SupplierService:

    def __init__(self):
        self.supplierDao = SupplierDao()

    def createSupplier(self, supplier):

        if not supplier.companyName or not supplier.companyName.strip():
            raise ValueError("Company name cannot be empty")
        if not supplier.contactName or not supplier.contactName.strip():
            raise ValueError("Contact name cannot be empty")
        if not supplier.contactNo or not supplier.contactNo.strip():
            raise ValueError("Contact number cannot be empty")
               

        supplier.companyName = supplier.companyName.strip()
        supplier.contactName = supplier.contactName.strip()
        supplier.contactN0 = supplier.contactNo.strip()

        if supplier.contactDesignation:
            supplier.contactDesignation = supplier.contactDesignation.strip()

        if supplier.city:
            supplier.city = supplier.city.strip()

        

        existingSupplier = self.supplierDao.getSupplierByCompanyName(supplier.companyName)

        if existingSupplier:
            raise ValueError("Supplier alreaady exists.")
        return self.supplierDao.createSupplier(supplier)


    def getSupplierById(self, supplierId):

        supplier = self.supplierDao.getSupplierById(supplierId)

        if supplier is None:
            raise ValueError("Supplier not found")

        return supplier


    def getAllSuppliers(self):
        return self.supplierDao.getAllSuppliers()


    def updateSupplier(self, supplier):
        if not supplier.companyName or not supplier.companyName.strip():
            raise ValueError("Company name cannot be empty")

        if not supplier.contactName or not supplier.contactName.strip():
            raise ValueError("Contact name cannot be empty")

        existingSupplier = self.supplierDao.getSupplierById(supplier.id)

        if existingSupplier is None:
            raise ValueError("Supplier not found")

        supplier.companyName = supplier.companyName.strip()
        supplier.contactName = supplier.contactName.strip()

        existingName = self.supplierDao.getSupplierByCompanyName(supplier.companyName)

        if(existingName is not None and existingName.id != supplier.id):
            raise ValueError("Supplier already exists")

        return self.supplierDao.updateSupplier(supplier)


    def deleteSupplier(self, supplierId):
        supplier = self.supplierDao.getSupplierById(supplierId)
        if supplier is None:
            raise ValueError("Supplier not found")

        return self.supplierDao.deleteSupplier(supplierId)
    

     