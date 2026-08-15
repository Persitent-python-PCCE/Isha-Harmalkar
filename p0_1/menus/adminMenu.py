

from controllers.categoryController import CategoryController
from controllers.orderController import OrderController
from controllers.productController import ProductController
from controllers.supplierController import SupplierController
from controllers.userController import UserController


class AdminMenu:

    def __init__(self, user):
        self.user = user
        self.userController = UserController()
        self.orderController  = OrderController()
        self.productController = ProductController()
        self.categoryController = CategoryController()
        self.supplierController = SupplierController()
        

    def show(self):
     

        while True:
            print("----------ADMIN PANEL----------------")
            print("1. Manage Users")
            print("2. Manage Categories")
            print("3. Manage Suppliers")
            print("4. Manage Products")
            print("5. View All Orders")           
            print("6. Exit Admin Panel")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.userMenu()
                
            elif choice == "2":
                self.categoryMenu()
            elif choice == "3":
                self.supplierMenu()
                
            elif choice == "4":
                self.productMenu()
            elif choice == "5":
                self.orderController.getAllOrders()
            
            elif choice == "6":
                print("Exiting Admin Panel")
                break          
            
            else:
                print("Invalid choice")


    def userMenu(self):
        while True:
            print("-----------------------USER MANAGEMENT------------------------------")
            print("1. Get User")
            print("2. Get All Users")
            print("3. Update User")
            print("4. Delete User")
            print("5. Back")

            choice = input("Enter chocie: ").strip()

            if choice == "1":
                self.userController.getUser()

            elif choice == "2":
                self.userController.getAllUsers()

            elif choice == "3":
                self.userController.updateUser()

            elif choice == "4":
                self.userController.deleteUser()

            elif choice == "5":
                break

            else:
                print("Invalid Choice")


    def categoryMenu(self):
        while True:

            print("---------------------------CATEGORY MANAGEMENT------------------------")
            print("1. Create Category")
            print("2. Get Category")
            print("3. Get All Categories")
            print("4. Update Category")
            print("5. Delete Category")
            print("6. Back")

            choice  = input("Enter Choice: ").strip()
            if choice == "1":
                self.categoryController.createCategory()

            elif choice == "2":
                self.categoryController.getCategoryById()

            elif choice == "3":
                self.categoryController.getAllCategories()

            elif choice == "4":
                self.categoryController.updateCategory()
            

            elif choice == "5":
                self.categoryController.deleteCategory()

            elif choice == "6":
                break

            else:
                print("Invalid Choice")


    def supplierMenu(self):

        while True:
            print("------------------SUPPLIER MANAGEMENT--------------------------")
            print("1. Create Supplier")
            print("2. Get Supplier")
            print("3. Get All supliers")
            print("4. Update Supplier By Id")
            print("5. Delete Supplier")
            print("6. Back")

            choice = input("Enter choice: ")

            if choice == "1":
                self.supplierController.createSupplier()

            elif choice == "2":
                self.supplierController.getSupplierById()

            elif choice == "3":
                self.supplierController.getAllSuppliers()

            elif choice == "4":
                self.supplierController.updateSupplier()

            elif choice == "5":
                self.supplierController.deleteSupplier()
            elif choice == "6":
                break

            else:
                print("Invalid Choice")



    def productMenu(self):

        while True:
            print("------------------PRODUCT MANAGEMENT--------------")

            print("1. CREATE Product")
            print("2. Get Product")
            print("3. Get All Products")
            print("4. Update Product")
            print("5. Deactivate Product")
            print("6. Activate Product")
            print("7. Back")

            choice = input("Enter Choice").strip()

            if choice == "1":
                self.productController.createProduct()

            elif choice == "2":
                self.productController.getProductById()
            elif choice == "3":
                self.productController.getAllProducts()
            elif choice == "4":
                self.productController.updateProduct()
            elif choice == "5":
                self.productController.deactivateProduct()
            elif choice == "6":
                self.productController.activateProduct()
            elif choice == "7":
                break
            else:
                print("Invalid Choice")





