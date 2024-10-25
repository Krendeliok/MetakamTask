from wtforms import SelectMultipleField
from flask import g


class SelectMultipleModelsField(SelectMultipleField):
    def __init__(self, model, *args, **kwargs):
        self.model = model
        super().__init__(choices=[(obj.id, str(obj)) for obj in g.db.query(model).all()], *args, **kwargs)
