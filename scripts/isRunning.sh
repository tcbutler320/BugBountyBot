#!/bin/sh
if ps -ef | grep -v grep | grep bbbot.py ; then
        exit 0
else
        /usr/bin/python3 /home/bugbountybot/app/bbbot.py >>  ~/cron.log 2>&1
        exit 0
fi