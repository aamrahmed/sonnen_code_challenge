# Use official Python image as the base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your application code into the container
COPY main.py .
COPY measurements_coding_challenge.csv .

# Install dependencies (we only need pandas)
RUN pip install --no-cache-dir pandas

# Set the command to run the script
ENTRYPOINT ["python", "main.py"]
