# Use ubuntu as the base image
FROM ubuntu:latest

# Install python3 and python requests
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install requests
# Install Supervisor
RUN apt-get install -y supervisor
RUN apt-get install -y vim

# Copy files
COPY . .

# Copy the Supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN chmod +x /loop.sh

ENV NIRA_URL=${DEFAULT_NIRA_URL:-'http://mobilevrs.nira.go.ug:8080/test/ThirdPartyApi/deaths.php'} \
    NIRA_USERNAME=${DEFAULT_NIRA_USERNAME:-'dhsi2.api'} \
    NIRA_PASSWORD=${DEFAULT_NIRA_PASSWORD:-'7162165ccebfa49657126bd8'} \
    NIRA_REALM=${DEFAULT_NIRA_REALM:-'mVRS API:deaths'} \
    DHIS_BASE_URL=${DEFAULT_DHIS_BASE_URL:-'https://hmis.health.go.ug'} \
    DHIS_DATA_URL=${DEFAULT_DHIS_DATA_URL:-'/api/29/analytics/events/query/vf8dN49jprI.json'} \
    DHIS_USERNAME=${DEFAULT_DHIS_USERNAME:-'moh-rch.dmurokora'} \
    DHIS_PASSWORD=${DEFAULT_DHIS_PASSWORD:-'Dhis@2022'} \
    DEBUG=${DEAFULT_DEBUG:-0} \
    START_COUNT=${DEFAULT_START_COUNT:-X} \
    END_COUNT=${DEFAULT_END_COUNT:-X} \
    LOGS_RECIPIENT_EMAIL=${DEFAULT_LOGS_RECIPIENT_EMAIL:-'srmugisa@gmail.com'}

# Start Supervisor when the container starts
CMD ["supervisord", "-n"]
