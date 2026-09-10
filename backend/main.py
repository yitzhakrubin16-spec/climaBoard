from fastapi import FastAPI
from routers import cities_routes
from routers import weather_routes
from routers import favorites_routes
from routers import compare_routes
from middleware.request_timer import request_timer

app = FastAPI()

app.middleware("http")(request_timer)
app.include_router(weather_routes.router)
app.include_router(cities_routes.router)
app.include_router(favorites_routes.router)
app.include_router(compare_routes.router)

@app.get("/health")
def health_test():
    return {"Health": "Server is running"}