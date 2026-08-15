class Supplier:
    def __init__(self, companyName, contactName, contactNo,contactDesignation=None, city=None,  id=None):
        self.id = id
        self.companyName = companyName
        self.contactName = contactName
        self.contactDesignation = contactDesignation
        self.city = city
        self.contactNo = contactNo