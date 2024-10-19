# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Run migrations
CMD ["python", "manage.py", "migrate"]

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
