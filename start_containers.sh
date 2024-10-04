#!/bin/bash

# Build containers
docker compose down
docker compose up --build -d

# Start the cron job
docker exec swapi_cron /scripts/run_update.sh

echo "Hello World"