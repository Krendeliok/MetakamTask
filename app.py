import os

from flask import Flask, g
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy.event import listens_for
from sqlalchemy_file.storage import StorageManager

from models import Base, Brand
from routes import route

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app, metadata=Base.metadata)
api = Api(app)

os.makedirs("./static/images", 0o777, exist_ok=True)
container = LocalStorageDriver("./static").get_container("images")
StorageManager.add_storage("default", container)


@listens_for(Brand, "after_delete")
def del_image(mapper, connection, target):
    if target.logo:
        try:
            os.remove(os.path.join("./static/images", target.logo))
        except OSError:
            pass


@app.before_request
def before_request():
    g.db = db.session


route(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
