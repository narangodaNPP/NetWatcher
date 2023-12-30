from NetWatcher.controller.util import import_devices
from NetWatcher import app


@app.route("/devices/")
def devices():
    devices = import_devices()
    return {"devices": devices}