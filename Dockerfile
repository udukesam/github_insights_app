FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy requirements if you have it
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the port Code Engine will use
EXPOSE 8080

# Start Flask app
CMD ["python", "github_insights_app.py"]
