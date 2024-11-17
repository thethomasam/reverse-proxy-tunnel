# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy backend files
COPY backend.py /app/

# Install Flask
RUN pip install flask

# Expose the backend port
EXPOSE 3000

# Run the Flask app
ENTRYPOINT ["python", "backend.py"]
