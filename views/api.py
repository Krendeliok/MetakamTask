from PIL import Image
from flask import Blueprint, Response, request
import json
from controllers import brands, manufacturers
from controllers.brands import hashed_file_name, create_brand, get_brand
from controllers.manufacturers import get_manufacturer, create_manufacturer
from forms.create_brand import CreateBrandForm
from forms.create_manufacturer import CreateManufacturerForm

api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')


@api_blueprint.route('/brands/<brand_id>', methods=['GET'])
@api_blueprint.route('/brands', methods=['GET'])
def get_brands(brand_id=None):
    if brand_id:
        return Response(json.dumps(brands.get_brand(brand_id)), mimetype='application/json')
    return Response(json.dumps(brands.get_all_brands()), mimetype='application/json')


@api_blueprint.route('/manufacturers/<manufacturer_id>', methods=['GET'])
@api_blueprint.route('/manufacturers', methods=['GET'])
def get_manufacturers(manufacturer_id=None):
    if manufacturer_id:
        return Response(json.dumps(manufacturers.get_manufacturer(manufacturer_id)), mimetype='application/json')
    return Response(json.dumps(manufacturers.get_all_manufacturers()), mimetype='application/json')


@api_blueprint.route('/brands', methods=['POST'])
def new_brand():
    form = CreateBrandForm(request.form)

    if form.validate():
        try:
            form.logo.data = request.files['logo']
            if form.manufacturers.data:
                form.manufacturers.data = [get_manufacturer(int(manufacturer_id)) for manufacturer_id in
                                           form.manufacturers.data]
            if form.logo.data:
                hashed_name = hashed_file_name(form.logo.data.filename)
                Image.open(form.logo.data.stream).save(f"static/images/{hashed_name}")
                form.logo.data = hashed_name
            else:
                form.logo.data = ""
            create_brand(form.data)
            return Response(json.dumps({'status': "Brand created"}), status=201)
        except OSError | ValueError as e:
            return Response(json.dumps({'status': "Brand isn`t created"}), status=500)
    return Response(json.dumps({'status': "Brand isn`t created", "reason": form.errors}), status=400)


@api_blueprint.route('/manufacturers', methods=['POST'])
def new_manufacturer():
    form = CreateManufacturerForm(request.form)

    if form.validate():
        if form.brands.data:
            form.brands.data = [get_brand(int(brand_id)) for brand_id in form.brands.data]
        create_manufacturer(form.data)
        return Response(json.dumps({'status': "Manufacturer created"}), status=201)
    return Response(json.dumps({'status': "Manufacturer isn`t created", "reason": form.errors}), status=400)
