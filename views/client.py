from flask import Blueprint, render_template, request, Response
from PIL import Image
import json

from forms.create_brand import CreateBrandForm
from controllers.brands import get_all_brands, create_brand, hashed_file_name, get_brand
from controllers.manufacturers import get_all_manufacturers, create_manufacturer, get_manufacturer
from forms.create_manufacturer import CreateManufacturerForm

client_blueprint = Blueprint('client', __name__, url_prefix='/client')


@client_blueprint.route('/', methods=['GET'])
def index():
    return render_template('client/admin_base.html')


@client_blueprint.route('/brands', methods=['GET'])
def get_brands():
    form = CreateBrandForm(request.form)
    brands = get_all_brands()
    return render_template('client/brands.html', brands=brands, form=form)


@client_blueprint.route('/manufacturers', methods=['GET'])
def get_manufacturers():
    form = CreateManufacturerForm(request.form)
    manufacturers = get_all_manufacturers()
    return render_template('client/manufacturers.html', manufacturers=manufacturers, form=form)
