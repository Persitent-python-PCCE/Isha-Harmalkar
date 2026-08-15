from dao.userDao import UserDao
from models.user import User
import bcrypt


class UserService:
    def __init__(self):
        self.userDao = UserDao()


    def register(self, user):
        if not user.name or not user.name.strip():
            raise ValueError("Name cannot be empty")
        if not user.email or not user.email.strip():
            raise ValueError("Email cannot be empty")
        if not user.password:
            raise ValueError("Password cannot be empty")

        """  email = email.strip()
        name = myname.strip()
        password = password.strip() """

        existingUser = self.userDao.getUserByEmail(user.email.strip())
        

        if existingUser:
            raise ValueError("Email already registered")
        password = user.password.strip()

        hashedPassword = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())

        newUser = User(
            name=user.name.strip(),
            email=user.email.strip(),
            password=hashedPassword.decode("utf-8")
        )
        return self.userDao.createuser(newUser)

    def login(self, email, password, loginAsAdmin=False):
        user = self.userDao.getUserByEmail(email)
        


        if user is None:
            raise ValueError("Invalid email or password") #user doe snot exist for this email, msg capped to not reveal

        #print("Inside login, printing fetched password: ", user.password)
        #print("Inside login, printing password: ", password)

        #validPassword = user.password == password
        validPassword = bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8"))
        if not validPassword:
            raise ValueError("Invalid email or password")

        if loginAsAdmin and not user.isAdmin:
            raise ValueError("You do not have admin access")

        return user

    def getUser(self, userId):
        user = self.userDao.getUserById(userId)

        if user is None:
            raise ValueError("User not found")

        return user

    def getAllUsers(self):
        return self.userDao.getAllUsers()

    def updateUser(self, user):
        existingUser = self.userDao.getUserById(user.id)

        if existingUser is None:
            raise ValueError("User not found")

        exisitngEmailUser = self.userDao.getUserByEmail(user.email)

        if(exisitngEmailUser is not None and exisitngEmailUser.id != user.id):
            raise ValueError("Email already registered")

        return self.userDao.updateUser(user)



    def deleteUser(self, userId):
        user = self.userDao.getUserById(userId)

        if user is None:
            raise ValueError("User not found")

        return self.userDao.deleteUser(userId)




