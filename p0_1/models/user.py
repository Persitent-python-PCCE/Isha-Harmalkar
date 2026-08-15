class User:
    def __init__(self, name, email, password, isAdmin=False, id = None ):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
        
        