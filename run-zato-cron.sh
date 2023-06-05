#!/bin/bash

# Stop and remove the zato-cron container if it exists
docker container stop zato-cron
docker container rm zato-cron

# Remove the plydot/zato-cron:latest image if it exists
docker image rm plydot/zato-cron:latest

# Run the zato-cron container with the specified environment variables
docker run -d --name zato-cron -e NIRA_URL=https://mobilevrs.nira.go.ug/ThirdPartyApi/deaths.php -e NIRA_USERNAME=api.dhis2 -e NIRA_PASSWORD=9b095ac8449c7fd2cb7adc45 plydot/zato-cron:latest
