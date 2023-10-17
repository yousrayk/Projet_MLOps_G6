# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to the current directory
WORKDIR .

# Install any necessary dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
COPY . . 
# Define environment variable

# Run app.py when the container launches
CMD ["python", "/app.py"]
