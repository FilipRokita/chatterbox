# Use Python 3.12-slim as the base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8081

# Command to run the application
CMD ["gunicorn", "-k", "eventlet", "-b", "0.0.0.0:8081", "app:app"]