#!/usr/bin/env bash
cd /opt/siliconprawn
(echo; echo; echo; echo starting; sudo -u www-data python3 -u sipager.py "$@") |tee -a /var/www/lib/sipager.txt

