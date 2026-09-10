from typing import Annotated
from fastapi import APIRouter, Query
from schemas.favorites import FavoriteCreate, UserNameSearchParams
from services.favorite_service import add_favorite_service, get_favorites_service

router = APIRouter(prefix="/favorites")

@router.post("/")
def add_favorite(favorite: FavoriteCreate):
    return add_favorite_service(favorite=favorite)

@router.get("/")
def get_favorites(params: Annotated[UserNameSearchParams, Query()]):
    return get_favorites_service(user_name=params.user_name)