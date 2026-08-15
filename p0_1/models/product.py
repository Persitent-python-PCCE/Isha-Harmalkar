class Product:
    def __init__(self, categoryId:int, supplierId:int, name:str, unitPrice:float, stock = 1,isActive=True, id=None):
        self.id = id
        self.categoryId = categoryId
        self.supplierId = supplierId
        self.name = name
        self.unitPrice = unitPrice
        self.stock= stock
        self.isActive = isActive
        