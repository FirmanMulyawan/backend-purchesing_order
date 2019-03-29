import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ==================================== EMPLOYEE ==================================================


class Employee(db.Model):
    __tablename__ = 'employee'

    employee_id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())
    position = db.Column(db.String())

    def __init__(self, fullname, password, email, position):
        self.fullname = fullname
        self.password = password
        self. email = email
        self.position = position

    def __repr__(self):
        return '<employee id {}>'.format(self.employee_id)

    def serialize(self):
        return{
            'employee_id': self.employee_id,
            'fullname': self.fullname,
            'password': self.password,
            'email': self.email,
            'position': self.position
        }

# =============================== CONTRACT ==================================================

class Contract(db.Model):
    __tablename__ = 'contract'

    contract_id = db.Column(db.Integer, primary_key=True)
    vendor_name = db.Column(db.String())
    contract_start_date = db.Column(db.DateTime())
    contract_end_date = db.Column(db.DateTime())
    currency = db.Column(db.String())
    plant = db.Column(db.String())

    def __init__(self, vendor_name, contract_start_date, contract_end_date, currency, plant):
        self.vendor_name = vendor_name
        self.contract_start_date = contract_start_date
        self.contract_end_date = contract_end_date
        self.currency = currency
        self.plant = plant

    def __repr__(self):
        return '<contract id {}>'.format(self.contract_id)

    def serialize(self):
        return{
            'contract_id': self.contract_id,
            'vendor_name': self.vendor_name,
            'contract_start_date': self.contract_start_date,
            'contract_end_date': self.contract_end_date,
            'currency': self.currency,
            'plant': self.plant
        }


# ================================== ITEM ==================================================

class Item(db.Model):
    __tablename__ = 'item'

    item_id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String())
    material = db.Column(db.String())
    description = db.Column(db.String())
    storage_location = db.Column(db.String())
    quantity = db.Column(db.Integer())
    price_each = db.Column(db.Integer())
    budget_source = db.Column(db.String())
    note = db.Column(db.String())

    def __init__(self, item_type, material, description, storage_location, quantity, price_each, budget_source, note):
        self.item_type = item_type
        self.material = material
        self.description = description
        self.storage_location = storage_location
        self.quantity = quantity
        self.price_each = price_each
        self.budget_source = budget_source
        self.note = note

    def __repr__(self):
        return '<item id {}>'.format(self.item_id)

    def serialize(self):
        return{
            'item_id': self.item_id,
            'item_type': self.item_type,
            'material': self.material,
            'description': self.description,
            'storage_location': self.storage_location,
            'quantity': self.quantity,
            'price_each': self.price_each,
            'budget_source': self.budget_source,
            'note': self.note
        }

# =========================== COMMENT ==================================================


class Comment(db.Model):
    __tablename__ = 'comment'

    comment_id = db.Column(db.Integer, primary_key=True)
    comment_detail = db.Column(db.String())

    def __init__(self, comment_detail):
        self.comment_detail = comment_detail

    def __repr__(self):
        return '<comment detail {}>'.format(self.comment_detail)

    def serialize(self):
        return{
            'comment_id': self.comment_id,
            'comment_detail': self.comment_detail
        }


# ================================ PURCHASE_ORDER =====================================================
class Purchase_order(db.Model):
    __tablename__ = 'purchase_order'

    po_id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.contract_id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'), nullable=False)
    medco_representative = db.Column(db.String())
    medco_to_provide = db.Column(db.String())
    location = db.Column(db.String())
    note = db.Column(db.String())
    budget_source = db.Column(db.String())
    price_total = db.Column(db.Integer())
    comment = db.Column(db.String())

    def __init__(self, contract_id, employee_id, item_id, medco_representative, medco_to_provide, location, note, budget_source, price_total, comment):
        self.contract_id = contract_id
        self.employee_id = employee_id
        self.item_id = item_id
        self.medco_representative = medco_representative
        self.medco_to_provide = medco_to_provide
        self.location = location
        self.note = note
        self.budget_source = budget_source
        self.price_total = price_total
        self.comment = comment

    def __repr__(self):
        return'<game pin {}>'.format(self.po_id)

    def serialize(self):
        return {
            'po_id': self.po_id,
            'contract_id': self.contract_id,
            'employee_id': self.employee_id,
            'item_id': self.item_id,
            'medco_representative': self.medco_representative,
            'medco_to_provide': self.medco_to_provide,
            'location': self.location,
            'note': self.note,
            'budget_source': self.budget_source,
            'price_total': self.price_total,
            'comment': self.comment
        }
