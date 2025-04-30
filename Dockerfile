# Use official Python image as base
FROM python:3.11-slim

# Set environment variables
#ENV PYTHONDONTWRITEBYTECODE=1 \
#    PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port that Flask app will run on
EXPOSE 8000

# Command to run the Flask app
CMD ["python", "myFlask.py"]

