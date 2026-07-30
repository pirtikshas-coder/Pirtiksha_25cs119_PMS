from database import db

# ---------------- FUEL INVENTORY ----------------

class FuelInventory(db.Model):
    __tablename__ = "fuel_inventory"

    fuel_id = db.Column(db.Integer, primary_key=True)
    fuel_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    supplier = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)


# ---------------- EMPLOYEE ----------------

class Employee(db.Model):
    __tablename__ = "employee"

    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    shift = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Float, nullable=False)


# ---------------- SUPPLIER ----------------

class Supplier(db.Model):
    __tablename__ = "supplier"

    supplier_id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)


# ---------------- BILLING ----------------

class Billing(db.Model):
    __tablename__ = "billing"

    bill_no = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    billing_date = db.Column(db.String(20), nullable=False)