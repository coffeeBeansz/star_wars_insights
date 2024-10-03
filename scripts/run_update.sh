#!/bin/bash
cron_job=$(cat /scripts/cronjob)
if crontab -l | grep -q "$cron_job"; then
  echo "Cron job already exists. No changes made."
else
  (
    crontab -l
    echo "$cron_job"
  ) | crontab -
  echo "Cron job added successfully."
fi

echo "Current cron jobs:"
crontab -l