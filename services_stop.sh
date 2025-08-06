#!/usr/bin/env bash

echo "Stopping"
sudo systemctl stop autothumb.service
sudo systemctl stop sipager.service
sudo systemctl stop simapper.service
