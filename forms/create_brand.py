from wtforms import Form, FileField, StringField, validators

from models import Manufacturer

from forms.custom_fields import SelectMultipleModelsField


class CreateBrandForm(Form):
    logo = FileField('Логотип')
    name = StringField('Название', [validators.Length(min=4, max=255), validators.DataRequired()])
    description = StringField('Описание', [validators.Length(min=4, max=255), validators.DataRequired()])
    manufacturers = SelectMultipleModelsField(Manufacturer, 'Производители')
