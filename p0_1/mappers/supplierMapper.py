from models.supplier import Supplier




def mapRowToSupplier(row):
    if row is None:
        return None


    return Supplier(
        id=row["id"],
        companyName=row["company_name"],
        contactName=row["contact_name"],
        contactDesignation=row["contact_designation"],
        city=row["city"],
        contactNo=row["contact_no"]
    )