# connectivity-emulator


## Enable IP Forwarding

sudo vi /etc/sysctl.conf

net.ipv4.ip_forward=1

sudo sysctl -p

## Allow traffic to and from the local network interface
sudo iptables -A INPUT -i lo -j ACCEPT && sudo iptables -A OUTPUT -o lo -j ACCEPT

## Redirect HTTP traffic to the Flask app (assuming Flask runs on port 80)
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000

## Enable NAT
sudo iptables -t nat -A POSTROUTING -o wlan2 -j MASQUERADE

## Install flask and gunicorn
venv/bin/pip install flask gunicorn

## Activate venv
source venv/bin/activate

## Run
gunicorn --header-map -w 4 -b 0.0.0.0:8000 app:app
