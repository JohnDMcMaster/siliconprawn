#!/usr/bin/env bash
# /opt/siprawn/user_add.sh --user mcmaster --copyright "John McMaster, CC BY 4.0" --dry
sudo -u www-data python3 -u /opt/siprawn/user_add.py "$@"
