# Use official Python runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run the web server
CMD ["gunicorn", "-b", ":8080", "app:app"]


