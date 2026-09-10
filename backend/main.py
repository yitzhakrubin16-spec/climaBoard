from fastapi import FastAPI
from routers import weather, cities
from middleware.request_timer import request_timer

app = FastAPI()

app.middleware("http")(request_timer)
app.include_router(weather.router)
app.include_router(cities.router)

@app.get("/health")
def health_test():
    return {"Health": "Server is running"}