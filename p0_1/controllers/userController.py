from services.userService import UserService
from models.user import User


class UserController:
    def __init__(self):
        self.userService = UserService()

    def register(self):

        print("----------Register------------")
        name = input("Name: ")
        email = input("Email: ")
        password = input("Password: ")

        user = User(
            name=name,
            email=email,
            password=password
        )

        try:
            newUser = self.userService.register(user)

            print("User registered with id: ", newUser.id)
            self.printUser(newUser)

            return newUser

        except ValueError as err:
            print("Error: ",err)
            return None

        #return None


    def login(self, loginAsAdmin = False):
        print("----------Login---------")

        email = input("Email: ")
        password = input("Password: ")

        try:
            user = self.userService.login(email,password, loginAsAdmin)
            print("You have logged in as ", user.name)
            return user

        except ValueError as err:
            print("Login Error: ", err)

        return None


    def getUser(self):
        userId = input("Enter user Id: ")
        try:
            userId = int(userId)

            user = self.userService.getUser(userId)

            print("--------Get User------")
            self.printUser(user)
            return user
        except ValueError as err:
            print("Failed to get User: ", err)

        return None


    def getAllUsers(self):
        try:
            users = self.userService.getAllUsers()

            if not users:
                print("No users found")
                return []

            print("----------Users----------")
            for user in users:
                self.printUser(user)

            return users
        except ValueError as err:
            print("Error while getting all users: ", err)

        return []

    def updateUser(self):
        print("-----------Update User---------------")
        userId = input("UserID: ")
        name = input("New Name: ")
        email=input("New Email: ")
        password = input("New password:")

        try:
            userId = int(userId)
            user = User(
                id=userId,
                name=name,
                email=email,
                password=password
            )

            updated = self.userService.updateUser(user)

            if updated:
                print("User updated succcessfully.")
                self.printUser(user)
            else:
                print("User was not updated")

            return updated
        except ValueError as err:
            print("Updating error: ", err)

        return False

    def deleteUser(self):
        print("-----------Delete User--------")

        userId = input("user id: ")
        try:
            userId = int(userId)
            confirm = input("Are yus ure you want to delete? [Y/N]")
            if confirm.lower() != "y":
                print("delete cancelled")
                return False

            deleted = self.userService.deleteUser(userId)

            if deleted:
                print("User deleted successfully")
            else:
                print("User was not deleted")

            return deleted

        except ValueError as err:
            print("Could not delete as: ", err)

        return False
        



    

    def printUser(self, user):
        print(f"ID:    {user.id}")
        print(f"Name:  {user.name}")
        print(f"Email: {user.email}")
        print(f"Admin: {user.isAdmin}")

    