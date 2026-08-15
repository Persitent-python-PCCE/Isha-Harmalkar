from models.category import Category



def mapRowToCategory(row):
    if row is None:
        return None
    
    return Category(
        id=row["id"],
        name=row["name"]
    )