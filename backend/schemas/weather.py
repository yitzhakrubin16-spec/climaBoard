from pydantic import BaseModel, Field

class ForecastParams(BaseModel):
    longitude: float = Field(ge=-180, le=180)
    latitude: float = Field(ge=-90, le=90)
    days: int = Field(ge=1, le=16)

class CurrentWeatherParams(BaseModel):
    longitude: float = Field(ge=-180, le=180)
    latitude: float = Field(ge=-90, le=90)