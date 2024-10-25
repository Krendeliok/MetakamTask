from sqlalchemy import String
from sqlalchemy.orm import mapped_column, relationship

from models import Base


class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    name = mapped_column(String(255), nullable=False, unique=True)
    description = mapped_column(String, nullable=False)
    country = mapped_column(String(255), nullable=False)
    certificates = mapped_column(String, nullable=False)

    brands = relationship('Brand', secondary='manufacturers_brands', back_populates='manufacturers')

    def __repr__(self):
        return f'<Manufacturer {self.name}>'

    def __str__(self):
        return self.name
