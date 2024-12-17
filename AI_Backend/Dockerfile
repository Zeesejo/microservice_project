# Use Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5001 for the AI backend
EXPOSE 5001

# Run the backend service
CMD ["python", "app.py"]
