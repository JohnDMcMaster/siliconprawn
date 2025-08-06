#!/usr/bin/env bash

rm -f /etc/systemd/system/autothumb.service
rm -f /etc/systemd/system/sipager.service
rm -f /etc/systemd/system/simapper.service

ln -s /opt/siliconprawn/autothumb/autothumb.service /etc/systemd/system/
ln -s /opt/siliconprawn/sipager.service /etc/systemd/system/
ln -s /opt/siliconprawn/simapper.service /etc/systemd/system/

sudo systemctl daemon-reload

sudo systemctl enable autothumb.service
sudo systemctl enable sipager.service
sudo systemctl enable simapper.service

sudo systemctl start autothumb.service
sudo systemctl start sipager.service
sudo systemctl start simapper.service

echo "Checking"
sleep 1
sudo systemctl status autothumb.service
sudo systemctl status sipager.service
sudo systemctl status simapper.service
