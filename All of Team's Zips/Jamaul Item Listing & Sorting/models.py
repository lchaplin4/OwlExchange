from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, nullable=False)
    description = db.Column(db.Text)
    price_cents = db.Column(db.Integer, index=True, nullable=False)
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), index=True)
    category = db.relationship('Category', backref='products')
