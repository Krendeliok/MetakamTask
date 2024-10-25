from sqlalchemy import String
from sqlalchemy.orm import mapped_column, relationship

from models import Base


class Brand(Base):
    __tablename__ = 'brand'
    logo = mapped_column(String(255), nullable=False)
    name = mapped_column(String(255), nullable=False, unique=True)
    description = mapped_column(String, nullable=False)

    manufacturers = relationship('Manufacturer', secondary='manufacturers_brands', back_populates='brands')

    def __repr__(self):
        return f'<Brand {self.name}>'

    def __str__(self):
        return self.name
