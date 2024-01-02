#!/bin/bash

sudo mv /home/pi/ddnsUpdater/ddnsUpdater.service /etc/systemd/system/ && sudo systemctl daemon-reload
chmod +x -R /home/pi/ddnsUpdater/*