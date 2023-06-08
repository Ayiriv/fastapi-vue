from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.medicines as crud
from src.auth.jwthandler import get_current_user
from src.schemas.medicines import MedicineOutSchema
from src.schemas.token import Status


router = APIRouter()


@router.get(
    "/medicines",
    response_model=List[MedicineOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_medicines():
    return await crud.get_medicines()


@router.get(
    "/medicine/{medicine_id}",
    response_model=MedicineOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_medicine(medicine_id: int) -> MedicineOutSchema:
    try:
        return await crud.get_medicine(medicine_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )
    

@router.get(
    "/medicine/search/{name}",
    response_model=List[MedicineOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def search_medicine_by_name(name: str) -> List[MedicineOutSchema]:
    try:
        print(name)
        return await crud.search_medicine_by_name(name)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )
    
