from pydantic import BaseModel, Field

class CompareCities(BaseModel):
    longitude_first: float = Field(ge=-180, le=180)
    latitude_first: float = Field(ge=-90, le=90)
    longitude_second: float = Field(ge=-180, le=180)
    latitude_second: float = Field(ge=-90, le=90)