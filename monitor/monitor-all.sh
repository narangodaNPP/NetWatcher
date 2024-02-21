#!/bin/bash
netwatcher=${1:-localhost:5001}
sudo python3 host_monitor.py --netwatcher $netwatcher &
sudo python3 host_portscan.py --netwatcher $netwatcher &
python3 device_monitor.py --netwatcher $netwatcher &
python3 service_monitor.py --netwatcher $netwatcher &