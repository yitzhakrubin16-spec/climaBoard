from typing import Annotated
from fastapi import APIRouter, Query, HTTPException
from schemas.favorites import FavoriteCreate, UserNameSearchParams
from services.favorite_service import add_favorite_service, get_favorites_service, delete_favorite_service

router = APIRouter(prefix="/favorites")

@router.post("/")
def add_favorite(favorite: FavoriteCreate):
    return add_favorite_service(favorite=favorite)

@router.get("/")
def get_favorites(params: Annotated[UserNameSearchParams, Query()]):
    return get_favorites_service(user_name=params.user_name)

@router.delete("/{city_id}")
def delete_favorite(params: Annotated[UserNameSearchParams, Query()], city_id: int):
    res = delete_favorite_service(user_name=params.user_name, city_id=city_id)

    if res is None:
        raise HTTPException(status_code=404, detail="favorite not found")
    else:
        return res