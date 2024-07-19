# Use a suitable base image (e.g., Python 3.9)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "core.wsgi:application", "-b", "0.0.0.0:8000"]