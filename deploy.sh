#!/bin/bash
echo "Running Pelican"
pelican content -t ~/space-blog/themes/nest
echo "removing old files"
rm -r /var/www/space-blog/*
echo "copying new files"
cp -r output/* /var/www/space-blog/
echo "restarting nginx"
service nginx restart
