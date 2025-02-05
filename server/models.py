from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bakery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    baked_goods = db.relationship('BakedGood', backref='bakery', lazy=True)

class BakedGood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakery.id'), nullable=False)
