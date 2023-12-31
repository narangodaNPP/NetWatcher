name=${1:-localhost}
broker=${2:-localhost}
sudo python3 worker.py --name $name --broker $broker