from fastapi import FastAPI
import os

# Create a FastAPI instance
app = FastAPI()

@app.get("/")
def read_root():
    """
    Returns a simple JSON response.
    """
    return {"message": "Hello from FastAPI on IBM Code Engine!"}

@app.get("/healthz")
def health_check():
    """
    A simple health check endpoint to confirm the application is running.
    """
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    # Use the PORT environment variable provided by Code Engine
    port = int(os.environ.get("PORT", 8080))
    # Bind to 0.0.0.0 to be accessible from outside the container
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
