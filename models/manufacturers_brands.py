from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column

from models import Base


class ManufacturersBrands(Base):
    __tablename__ = 'manufacturers_brands'
    manufacturer_id = mapped_column(Integer, ForeignKey('manufacturer.id', ondelete='CASCADE', onupdate='CASCADE'))
    brand_id = mapped_column(Integer, ForeignKey('brand.id', ondelete='CASCADE', onupdate='CASCADE'))
