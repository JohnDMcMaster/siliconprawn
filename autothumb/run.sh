#!/usr/bin/env bash
cd /opt/siliconprawn/autothumb
(echo; echo; echo; echo starting; sudo -u www-data ./refresh-loop.sh) |tee -a /opt/siliconprawn/autothumb/log.txt

