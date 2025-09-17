# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port 8080 (required by Code Engine)
EXPOSE 8080

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "github_insights_app:app", "--host", "0.0.0.0", "--port", "8080"]
