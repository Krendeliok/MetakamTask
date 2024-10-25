from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    confirm_deleted_rows = False
    id = mapped_column(Integer, primary_key=True, autoincrement=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
