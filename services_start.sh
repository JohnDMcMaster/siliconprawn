#!/usr/bin/env bash

echo "Starting"
sudo systemctl start autothumb.service
sudo systemctl start sipager.service
sudo systemctl start simapper.service
