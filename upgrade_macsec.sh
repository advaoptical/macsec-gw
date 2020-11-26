#!/bin/bash
set -x #echo on
git pull
systemctl stop macsec-gw
cp macsec-gw /opt/adva/extra
systemctl restart macsec-gw