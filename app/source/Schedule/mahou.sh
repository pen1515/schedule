#!/bin/bash

set -eu

LC_CTYPE=C

echo -n "SECRET_KEY = '" > Schedule/settings_local.py
tr -dc 'A-Za-z0-9!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' </dev/urandom | head -c 50 >> Schedule/settings_local.py
echo "'" >> Schedule/settings_local.py