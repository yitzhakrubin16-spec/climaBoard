from fastapi import FastAPI
from routers import weather

app = FastAPI()

app.include_router(weather.router)

@app.get("/health")
def health_test():
    return {"Health": "Server is running"}