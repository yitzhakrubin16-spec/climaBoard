from fastapi import APIRouter, Query
from services.city_service import search_city_service
from schemas.cities import CitySearchParams
from typing import Annotated

router = APIRouter(prefix="/cities")

@router.get("/search")
def search_city(params: Annotated[CitySearchParams,Query()]):
    return search_city_service(name=params.name)