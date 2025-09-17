FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port CE will inject
EXPOSE 8080

# Start FastAPI with Uvicorn
CMD ["uvicorn", "github_insights_app:app", "--host", "0.0.0.0", "--port", "8080"]
