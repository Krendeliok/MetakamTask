from sqlalchemy.orm import configure_mappers

from models.base import Base

from models.brand import Brand
from models.manufacturer import Manufacturer
from models.manufacturers_brands import ManufacturersBrands

configure_mappers()
