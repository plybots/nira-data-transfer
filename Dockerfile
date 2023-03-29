# Use ubuntu as the base image
FROM ubuntu:latest

# Install python3 and python requests
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install requests

# Copy the script to the container
COPY main.py /main.py

# Install cron and set up the crontab
RUN apt-get install -y cron
RUN echo "0 0 * * * python3 /main.py" > /etc/cron.d/some_script

# Start cron in the foreground
CMD ["cron", "-f"]