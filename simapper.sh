#!/usr/bin/env bash
cd /opt/siprawn
(echo; echo; echo; echo starting; sudo -u www-data python3 -u simapper.py "$@") |tee -a /var/www/lib/simapper.txt

