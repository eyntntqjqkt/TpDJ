# Step 1: Build environment
FROM python:3.11-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run server
CMD ["gunicorn", "demoDjango.wsgi:application", "--bind", "0.0.0.0:8000"]