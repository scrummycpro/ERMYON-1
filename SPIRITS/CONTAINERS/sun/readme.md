Certainly! Here's a documentation guide for your Docker image that displays the Hebrew date and sunset time using `hdate -t` and an external API. This guide will cover the Dockerfile, the `sunset.sh` script, and how to build and run the Docker container.

---

## Docker Image Documentation: Hebrew Date and Sunset Time Display

### Overview

This Docker image demonstrates how to display the current Hebrew date and sunset time using `hdate -t` and an external API (`Hebcal API`). It includes a Dockerfile for building the image and a script (`sunset.sh`) that fetches and displays this information.

### Components

- **Dockerfile**: Defines the environment and dependencies required for the Docker image.

- **sunset.sh**: A shell script that uses `hdate -t` to get the Hebrew date and fetches sunset time from the Hebcal API.

### Prerequisites

- Docker installed on your local machine or server ([Docker Installation Guide](https://docs.docker.com/get-docker/)).

### Dockerfile

```dockerfile
# Use a base image that has a Linux distribution (e.g., Ubuntu)
FROM ubuntu:latest

# Update packages and install necessary tools
RUN apt-get update && \
    apt-get install -y hdate jq curl

# Copy the sunset script into the container
COPY sunset.sh /sunset.sh

# Make the script executable
RUN chmod +x /sunset.sh

# Set the default command to run when the container starts
CMD ["/sunset.sh"]
```

#### Dockerfile Explanation:

- `FROM ubuntu:latest`: Specifies Ubuntu as the base image.
- `RUN apt-get update && apt-get install -y hdate jq curl`: Updates package lists and installs `hdate` (for Hebrew date), `jq` (for JSON parsing), and `curl` (for making HTTP requests).
- `COPY sunset.sh /sunset.sh`: Copies the `sunset.sh` script from the local directory into the Docker image.
- `RUN chmod +x /sunset.sh`: Makes the `sunset.sh` script executable within the Docker image.
- `CMD ["/sunset.sh"]`: Defines the default command to run when a container is started from this image, which executes the `sunset.sh` script.

### sunset.sh

```bash
#!/bin/bash

# Get the Hebrew date using hdate -t
hebrew_date=$(hdate -t)

# Extract the sunset time using Hebcal API
sunset_time=$(curl -s "https://www.hebcal.com/shabbat/?cfg=json&geonameid=3448439&m=50")

# Parse the JSON response to get the sunset time
sunset_time=$(echo "$sunset_time" | jq -r '.items[0].candles | .[] | select(.title=="Sunset").date')

# Display the Hebrew date and sunset time
echo "Hebrew Date: $hebrew_date"
echo "Sunset Time: $sunset_time"
```

#### sunset.sh Explanation:

- Retrieves the current Hebrew date using `hdate -t`.
- Fetches sunset time data from the Hebcal API (`https://www.hebcal.com/shabbat/?cfg=json&geonameid=3448439&m=50`).
- Parses the JSON response using `jq` to extract the sunset time.
- Displays the Hebrew date and sunset time in the terminal.

### Build and Run Instructions

1. **Build the Docker Image**:

   Navigate to the directory containing your `Dockerfile` and `sunset.sh`, then run:

   ```bash
   docker build -t my-sunset-app .
   ```

   - `-t my-sunset-app`: Tags the built image with the name `my-sunset-app`.

2. **Run the Docker Container**:

   After successfully building the Docker image, you can run the container:

   ```bash
   docker run my-sunset-app
   ```

   This command starts a container from your `my-sunset-app` Docker image, which will execute the `sunset.sh` script and display the Hebrew date and sunset time.

### Additional Notes

- Ensure `jq` and `curl` are installed within the Docker image (`RUN apt-get install -y jq curl` in the Dockerfile).
- Adjust the `geonameid` parameter in the Hebcal API URL (`https://www.hebcal.com/shabbat/?cfg=json&geonameid=3448439&m=50`) to match your desired location.
- Modify the script (`sunset.sh`) or Dockerfile as needed for specific requirements or customizations.

---

This documentation provides a comprehensive guide for creating and using a Docker image that displays the Hebrew date and sunset time. Adjust parameters and scripts according to your specific use case or location requirements.
