# Use a base image that has a Linux distribution (e.g., Ubuntu)
FROM ubuntu:latest

# Update packages and install hdate
RUN apt-get update && \
    apt-get install -y hdate

# Set the default command to run when the container starts
CMD ["hdate", "-t"]

