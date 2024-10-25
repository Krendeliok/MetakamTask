from flask import g
from sqlalchemy.orm import joinedload

from models import Brand
from hashlib import md5


def get_all_brands():
    brands = g.db.query(Brand).options(joinedload(Brand.manufacturers)).all()
    return brands


def get_brand(brand_id):
    brand = g.db.get(Brand, brand_id)
    return brand


def create_brand(data) -> dict:
    brand = Brand(**data)
    g.db.add(brand)
    g.db.commit()
    return brand.as_dict()


def update_brand(brand_id, data) -> dict | None:
    brand = g.db.get(Brand, brand_id)
    if not brand:
        return
    brand.update(data)
    g.db.commit()
    return brand.as_dict()


def hashed_file_name(file_name: str) -> str:
    return f"{md5(file_name.encode()).hexdigest()}.png"
