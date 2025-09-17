# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the port Code Engine will use
EXPOSE 8080

# Set environment variables (optional defaults)
ENV PORT=8080

# Start FastAPI using Uvicorn
CMD ["uvicorn", "github_insights_app:app", "--host", "0.0.0.0", "--port", "8080"]
