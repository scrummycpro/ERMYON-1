# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Install ffmpeg and other dependencies
RUN apk update && \
    apk add --no-cache ffmpeg

# Install Python dependencies
RUN pip3 install gtts pydub

# Copy the current directory contents into the container at /app
COPY . .

# Run the speak2.py script when the container launches
CMD ["python3", "speak2.py"]

