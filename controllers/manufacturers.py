from flask import g
from sqlalchemy.orm import joinedload

from models import Manufacturer


def get_all_manufacturers():
    manufacturers = g.db.query(Manufacturer).options(joinedload(Manufacturer.brands)).all()
    return manufacturers


def get_manufacturer(manufacturer_id):
    manufacturer = g.db.get(Manufacturer, manufacturer_id)
    return manufacturer


def create_manufacturer(data):
    manufacturer = Manufacturer(**data)
    g.db.add(manufacturer)
    g.db.commit()
    return manufacturer.as_dict()


def update_manufacturer(manufacturer_id, data):
    manufacturer = g.db.get(Manufacturer, manufacturer_id)
    if not manufacturer:
        return None
    manufacturer.update(data)
    g.db.commit()
    return manufacturer.as_dict()
