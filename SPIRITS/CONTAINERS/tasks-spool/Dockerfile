# Use a base image
FROM ubuntu:latest

# Install Task Spooler, ffmpeg, and any necessary dependencies
RUN apt-get update \
    && apt-get install -y \
        task-spooler \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Create a directory inside the container (optional)
RUN mkdir /app

# Optional: Set up a default TS_ONFINISH script
COPY ts_onfinish.sh /usr/local/bin/ts_onfinish.sh
RUN chmod +x /usr/local/bin/ts_onfinish.sh

# Set the working directory
WORKDIR /app


