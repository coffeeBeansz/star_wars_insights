#!/bin/bash

touch /scripts/cronjob
echo "DB_HOST=$DB_HOST" >> /scripts/cronjob
echo "DB_PORT=$DB_PORT" >> /scripts/cronjob
echo "DB_USER=$DB_USER" >> /scripts/cronjob
echo "DB_PASSWORD=$DB_PASSWORD" >> /scripts/cronjob
echo "DB_NAME=$DB_NAME" >> /scripts/cronjob
echo "* * * * * /usr/bin/python3 /scripts/update_database.py" >> /scripts/cronjob

# Gjorde denna fil för att cron inte har tillgång till miljövariablerna annars.
# Eller detta var ett sätt att lösa det på iaf.