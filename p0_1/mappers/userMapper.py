from models.user import User



def mapRowToUser(row):
    if row is None:
        return None


    
    return User(
        id=row["id"],
        name=row["name"],
        email=row["email"],
        password=row["password"],
        isAdmin=row["is_admin"]
    )
