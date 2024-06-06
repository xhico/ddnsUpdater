#!/bin/bash

python3 -m venv /home/pi/ddnsUpdater/venv
source /home/pi/ddnsUpdater/venv/bin/activate
python3 -m pip install -r /home/pi/ddnsUpdater/requirements.txt --no-cache-dir
chmod +x -R /home/pi/ddnsUpdater/*
sudo mv /home/pi/ddnsUpdater/ddnsUpdater.service /etc/systemd/system/ && sudo systemctl daemon-reload

git clone https://github.com/xhico/Misc.git /home/pi/Misc
rsync -avp --progress /home/pi/Misc/Misc.py /home/pi/ddnsUpdater/venv/lib/python$(python3 -c "import sys; print('{}.{}'.format(sys.version_info.major, sys.version_info.minor))")/site-packages/
rm -rf /home/pi/Misc/