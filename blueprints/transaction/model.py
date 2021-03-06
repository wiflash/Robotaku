from blueprints import db
from flask_restful import fields
from datetime import datetime


class ShipmentMethods(db.Model):
    __tablename__ = "shipment_methods"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kurir = db.Column(db.String(20), unique=True, nullable=False, default="")
    tarif = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    
    response_fields = {
        "created_at": fields.DateTime,
        "updated_at": fields.DateTime,
        "id": fields.Integer,
        "kurir": fields.String,
        "tarif": fields.Integer
    }
    
    def __init__(self, kurir, tarif):
        self.kurir = kurir
        self.tarif = tarif

    def __repr__(self):
        return "<Shipment Methods %r>" % self.id


class PaymentMethods(db.Model):
    __tablename__ = "payment_methods"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(20), nullable=False, default="")
    norek = db.Column(db.String(20), unique=True, nullable=False)
    pemilik = db.Column(db.String(30), nullable=False, default="PT. Robotaku")
    tarif = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    
    response_fields = {
        "created_at": fields.DateTime,
        "updated_at": fields.DateTime,
        "id": fields.Integer,
        "nama": fields.String,
        "norek": fields.String,
        "pemilik": fields.String,
        "tarif": fields.Integer
    }
    
    def __init__(self, nama, norek, tarif):
        self.nama = nama
        self.norek = norek
        self.tarif = tarif

    def __repr__(self):
        return "<Payment Methods %r>" % self.id


class Transactions(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    shipment_method_id = db.Column(db.Integer, db.ForeignKey('shipment_methods.id'), nullable=False, default=1)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_methods.id'), nullable=False, default=1)
    total_harga = db.Column(db.Integer, nullable=False, default=0)
    total_tagihan = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.String(10), default="staging", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    
    response_fields = {
        "created_at": fields.DateTime,
        "updated_at": fields.DateTime,
        "id": fields.Integer,
        "user_id": fields.Integer,
        "shipment_method_id": fields.Integer,
        "payment_method_id": fields.Integer,
        "total_harga": fields.Integer,
        "total_tagihan": fields.Integer,
        "status": fields.String
    }
    
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "<Transactions %r>" % self.id


class Carts(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), nullable=False)
    jumlah = db.Column(db.Integer, nullable=False, default=0)
    subtotal = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    
    response_fields = {
        "created_at": fields.DateTime,
        "updated_at": fields.DateTime,
        "id": fields.Integer,
        "product_id": fields.Integer,
        "transaction_id": fields.Integer,
        "jumlah": fields.Integer,
        "subtotal": fields.Integer
    }
    
    def __init__(self, product_id, transaction_id, jumlah, subtotal):
        self.product_id = product_id
        self.transaction_id = transaction_id
        self.jumlah = jumlah
        self.subtotal = subtotal

    def __repr__(self):
        return "<Carts %r>" % self.id