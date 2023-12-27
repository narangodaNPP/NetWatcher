from flask import Flask
import yaml

app = Flask(__name__)


def import_devices():
    with open("NetWatcher/data/devices.yaml") as device_files:
        devices = yaml.safe_load(device_files.read())
    return devices


@app.route("/devices/")
def devices():

    devices = import_devices()
    return {"devices": devices}
