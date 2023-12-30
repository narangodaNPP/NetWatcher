import yaml


def import_devices():
    with open("NetWatcher/data/devices.yaml") as device_files:
        devices = yaml.safe_load(device_files.read())
    return devices
