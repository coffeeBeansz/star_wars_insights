#!/bin/bash

mkdir -p /tmp/logs
echo "Script is running!" >> /tmp/logs/test_script.log

apt-get update
apt-get -y install cron

# # Install cron and Python dependencies
# apt-get update && apt-get install -y cron python3 python3-pip

# # Install any Python packages needed (e.g., for API requests)
# pip3 install requests

# # Make sure the scripts are executable
# chmod +x /scripts/update_db.py
# chmod +x /scripts/run_update.sh

# # Setup scheduled update of the database with cron
# crontab /scripts/cronjob
# service cron start

echo "Script finished running!" >> /tmp/logs/test_script.log