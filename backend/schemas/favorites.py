from pydantic import BaseModel, Field

class FavoriteCreate(BaseModel):
    city_id: int
    name: str = Field(min_length=2, max_length=100)
    longitude: float = Field(ge=-180, le=180)
    latitude: float = Field(ge=-90, le=90)
    user_name: str = Field(min_length=2, max_length=15)

class UserNameSearchParams(BaseModel):
    user_name: str = Field(min_length=2, max_length=15)    