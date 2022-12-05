import logging
import traceback
from store.db import db


class StoreMetadata(db.Model):
    """
    This class represents the StoreMetadata table.
    """
    __tablename__ = "store_metadata"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(length=100))
    address = db.Column(db.String(length=1000))
    manager = db.Column(db.String(length=100))
    # not considered county code , string because of E1.64 standard.
    contact = db.Column(db.String(length=10))
    is_active = db.Column(db.Boolean)
    created_on = db.Column(
        db.DateTime,
        index=True,
        server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now())

    def __repr__(self):
        return '<name: {}>'.format(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class Supplier(db.Model):
    """
    This class represents the Suppliers table.
    """
    __tablename__ = "suppliers"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(length=100))
    address = db.Column(db.String(length=1000))
    # not considered county code , string because of E1.64 standard.
    contact = db.Column(db.String(length=10))
    is_active = db.Column(db.Boolean)
    created_on = db.Column(
        db.DateTime,
        index=True,
        server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now())

    def __repr__(self):
        return '<Sup_name:{}>'.format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class Category(db.Model):
    """
    This class represents the Categories table.
    """
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100))
    discription = db.Column(db.String(length=500))
    created_on = db.Column(
        db.DateTime,
        index=True,
        server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now())

    def __repr__(self):
        return '<category_type: {}>'.format(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


ItemSupplier = db.Table(
    'item_suppliers',
    db.Column(
        'id',
        db.BigInteger,
        primary_key=True),
    db.Column(
        'item_id',
        db.BigInteger,
        db.ForeignKey('items.id')),
    db.Column(
        'supplier_id',
        db.BigInteger,
        db.ForeignKey('suppliers.id')))


class Item(db.Model):
    """
    This class represents the Items table.
    """
    __tablename__ = "items"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(length=100))
    discription = db.Column(db.String(length=1000))
    mrp = db.Column(db.Float(precision=3))
    sup_id = db.relationship('Supplier', secondary=ItemSupplier, backref='items')
    quantity = db.Column(db.Integer)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('categories.id'))  # one2many
    store_id = db.Column(
        db.BigInteger,
        db.ForeignKey('store_metadata.id'),
        nullable=False)
    created_on = db.Column(
        db.DateTime,
        index=True,
        server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now())

    def __repr__(self):
        return '<name: {}>'.format(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

