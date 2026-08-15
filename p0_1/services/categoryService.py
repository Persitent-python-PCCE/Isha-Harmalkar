from dao.categoryDao import CategoryDao


class CategoryService:

    def __init__(self):
        self.categoryDao = CategoryDao()


    def createCategory(self, category):
        if not category.name or not category.name.strip():
            raise ValueError("Category name cannot be empty")

        category.name = category.name.strip()
        existingCategory = self.categoryDao.getCategoryByName(category.name)

        if existingCategory:
            raise ValueError("Category already exists")

        return self.categoryDao.createCategory(category)


    def getCategoryById(self, categoryId):

        category = self.categoryDao.getCategoryById(categoryId)

        if category is None:
            raise ValueError("Category not found")

        return category


    def getAllCategories(self):
        return self.categoryDao.getAllCategories()


    def updateCategory(self, category):
        if not category.name or not category.name.strip():
            raise ValueError("Category name cannot be empty")


        existingCategory = self.categoryDao.getCategoryById(category.id)


        if existingCategory is None:
            raise ValueError("Category not found")

        category.name = category.name.strip()

        existingName = self.categoryDao.getCategoryByName(category.name)

        if (existingName is not None and existingName.id != category.id):
            raise ValueError("Category already exists")

        return self.categoryDao.updateCategory(category)


    def deleteCategory(self, categoryId):
        category = self.categoryDao.getCategoryById(categoryId)
        if category is None:
            raise ValueError("Category not found")

        return self.categoryDao.deleteCategory(categoryId)

    