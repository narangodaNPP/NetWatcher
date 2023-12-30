from flask import Flask

app = Flask(__name__)

import server.views.ui_views
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

app.app_context().push()


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.Text)
    name = db.Column(db.Text, unique=True, nullable=False)
    os = db.Column(db.Text)
    hostname = db.Column(db.Text)
    vendor = db.Column(db.Text)


db.create_all()

from server.controller.util import import_devices

for device in import_devices():
    device_object = Device(**device)
    db.session.add(device_object)

db.session.commit()
