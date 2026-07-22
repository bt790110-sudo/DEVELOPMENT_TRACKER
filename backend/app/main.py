from fastapi import FastAPI

app = FastAPI(
    title="DevelopmentTracker API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DevelopmentTracker API!"
    }