from wtforms import Form, StringField, validators

from models import Brand

from forms.custom_fields import SelectMultipleModelsField


class CreateManufacturerForm(Form):
    name = StringField('Название', [validators.Length(max=255), validators.DataRequired()])
    description = StringField('Описание', [validators.Length(min=4), validators.DataRequired()])
    country = StringField('Страна', [validators.Length(max=255), validators.DataRequired()])
    certificates = StringField('Сертификаты', [validators.Length(max=255), validators.DataRequired()])
    brands = SelectMultipleModelsField(Brand, 'Бренды')
