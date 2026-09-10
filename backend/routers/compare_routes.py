from typing import Annotated
from fastapi import APIRouter, Query
from schemas.compare import CompareCities
from services.compare_service import compare_cities_service


router = APIRouter(prefix="/compare")


@router.get("/")
def compare(params: Annotated[CompareCities, Query()]):
    return compare_cities_service(data=params)