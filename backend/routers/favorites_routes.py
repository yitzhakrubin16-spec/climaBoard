from fastapi import APIRouter
from schemas.favorites import FavoriteCreate
from services.favorite_service import add_favorite_service

router = APIRouter(prefix="/favorites")

@router.post("/")
def add_favorite(favorite: FavoriteCreate):
    return add_favorite_service(favorite=favorite)