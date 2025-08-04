#!/usr/bin/env bash
cd /opt/siprawn/autothumb
(echo; echo; echo; echo starting; sudo -u www-data ./refresh-loop.sh) |tee -a /opt/siprawn/autothumb/log.txt

