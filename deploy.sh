#!/bin/bash
echo "Running Pelican"
pelican content -t ~/caelestia.space/themes/caelestia.space
echo "removing old files"
rm -r /var/www/caelestia.space/*
echo "copying new files"
cp -r output/* /var/www/caelestia.space/
echo "restarting nginx"
service nginx restart
