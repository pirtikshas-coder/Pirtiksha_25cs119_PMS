from flask import Flask, render_template, request, redirect
from database import db
from models import FuelInventory, Employee, Supplier, Billing

app = Flask(__name__)

# ---------------- DATABASE ----------------

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///petrolpump.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")

# ---------------- FUEL INVENTORY ----------------

@app.route("/fuel", methods=["GET", "POST"])
def fuel():

    if request.method == "POST":

        fuel = FuelInventory(
            fuel_id=int(request.form["fuel_id"]),
            fuel_type=request.form["fuel_type"],
            quantity=float(request.form["quantity"]),
            price=float(request.form["price"]),
            supplier=request.form["supplier"],
            date=request.form["date"]
        )

        db.session.add(fuel)
        db.session.commit()

        return redirect("/fuel")

    fuels = FuelInventory.query.all()

    return render_template(
        "fuel_inventory.html",
        fuels=fuels
    )

# ---------------- EMPLOYEE ----------------

@app.route("/employee", methods=["GET", "POST"])
def employee():

    if request.method == "POST":

        emp = Employee(
            employee_id=int(request.form["employee_id"]),
            employee_name=request.form["employee_name"],
            gender=request.form["gender"],
            phone=request.form["phone"],
            designation=request.form["designation"],
            shift=request.form["shift"],
            salary=float(request.form["salary"])
        )

        db.session.add(emp)
        db.session.commit()

        return redirect("/employee")

    employees = Employee.query.all()

    return render_template(
        "employee.html",
        employees=employees
    )

# ---------------- SUPPLIER ----------------

@app.route("/supplier", methods=["GET", "POST"])
def supplier():

    if request.method == "POST":

        sup = Supplier(
            supplier_id=int(request.form["supplier_id"]),
            supplier_name=request.form["supplier_name"],
            company_name=request.form["company_name"],
            fuel_type=request.form["fuel_type"],
            contact=request.form["contact"],
            address=request.form["address"]
        )

        db.session.add(sup)
        db.session.commit()

        return redirect("/supplier")

    suppliers = Supplier.query.all()

    return render_template(
        "supplier.html",
        suppliers=suppliers
    )

# ---------------- BILLING ----------------

@app.route("/billing", methods=["GET", "POST"])
def billing():

    if request.method == "POST":

        bill = Billing(
            bill_no=int(request.form["bill_no"]),
            customer_name=request.form["customer_name"],
            fuel_type=request.form["fuel_type"],
            quantity=float(request.form["quantity"]),
            price=float(request.form["price"]),
            total=float(request.form["total"]),
            billing_date=request.form["billing_date"]
        )

        db.session.add(bill)
        db.session.commit()

        return redirect("/billing")

    bills = Billing.query.all()

    return render_template(
        "billing.html",
        bills=bills
    )

# ---------------- REPORTS ----------------

@app.route("/reports")
def reports():

    fuel_count = FuelInventory.query.count()
    employee_count = Employee.query.count()
    supplier_count = Supplier.query.count()
    billing_count = Billing.query.count()

    return render_template(
        "reports.html",
        fuel_count=fuel_count,
        employee_count=employee_count,
        supplier_count=supplier_count,
        billing_count=billing_count
    )

# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True, port=503)
