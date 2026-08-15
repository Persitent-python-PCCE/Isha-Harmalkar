from services.categoryService import CategoryService
from models.category import Category


class CategoryController():

    def __init__(self):
        self.categoryService = CategoryService()


    def createCategory(self):
        print("----------Create Category---------------")
        name = input("Category Name: ")
        category = Category(name=name)

        try:
            category = self.categoryService.createCategory(category)

            print("Category created sucessfully.")
            self.printCategory(category)
            return category

        except ValueError as err:
            print("Cannot create category: ", err)


        return None

    def getCategoryById(self):
        categoryId = input("Enter category id: ")

        try:
            categoryId = int(categoryId)
            category = self.categoryService.getCategoryById(categoryId)
            print("----------Category--------------")
            self.printCategory(category)
            return category

        except ValueError as err:
            print("Could not get category: ", err)

        return None


    def getAllCategories(self):
        try:
            categories  = self.categoryService.getAllCategories()

            if not categories:
                print("No categories found")
                return []

            print("------------Categories-------------")
            for category in categories:
                self.printCategory(category)
                print("------------------")

            return categories

        except ValueError as err:
            print("Could not get categories: ", err)

        return []

    def updateCategory(self):
        print("----------------Update Category-------------------")

        categoryId = input("Catedory Id: ")
        name  = input("New Name: ")
        try:
            categoryId = int(categoryId)
            if not name.strip():
                raise ValueError ("Category name cannot be empty")
            category = Category(
                id=categoryId,name=name
            )
            updated = self.categoryService.updateCategory(category)

            if updated:
                print("Category updated sucesfully.")
                self.printCategory(category)
            else:
                print("Category was not updated.")

            return updated
        except ValueError as err:
            print("Could not update category: ", err )

        return False


    def deleteCategory(self):

        print("---------------Delete Category--------------")
        categoryId = input("Category Id: ")
        try:
            categoryId = int(categoryId)
            confirm = input("Are you sure you want to delete this categor? (YES/NO): ")


            if confirm.lower() != "yes":
                print("Deleltion cancelled")
                return False

            deleted = self.categoryService.deleteCategory(categoryId)

            if deleted:
                print("Category deleted successfully")
            else:
                print("Category was not deleted")

            return deleted

        except ValueError as err:
            print("Could not delete category as: ", err)
        except Exception as e:
            print("Cannot delete category as: ", e)

        return False

      
    
    def printCategory(self, category):
        print(f"ID:    {category.id}")
        print(f"Name:  {category.name}")
  
        