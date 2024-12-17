# Use Python slim image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for UI backend
EXPOSE 5000

# Start the UI backend service
CMD ["python", "app.py"]
