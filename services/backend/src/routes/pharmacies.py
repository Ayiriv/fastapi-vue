from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.pharmacies as crud
from src.auth.jwthandler import get_current_user
from src.schemas.pharmacies import PharmacyOutSchema, PharmacyInSchema, UpdatePharmacy
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/pharmacies",
    response_model=List[PharmacyOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_pharmacies():
    return await crud.get_pharmacies()


@router.get(
    "/pharmacy/{pharmacy_id}",
    response_model=PharmacyOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_pharmacy(pharmacy_id: int) -> PharmacyOutSchema:
    try:
        return await crud.get_pharmacy(pharmacy_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )


@router.post(
    "/pharmacies", response_model=PharmacyOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_pharmacy(
    pharmacy: PharmacyInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> PharmacyOutSchema:
    return await crud.create_pharmacy(pharmacy, current_user)


@router.patch(
    "/pharmacy/{pharmacy_id}",
    dependencies=[Depends(get_current_user)],
    response_model=PharmacyOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_pharmacy(
    pharmacy_id: int,
    pharmacy: UpdatePharmacy,
    current_user: UserOutSchema = Depends(get_current_user),
) -> PharmacyOutSchema:
    return await crud.update_pharmacy(pharmacy_id, pharmacy, current_user)


@router.delete(
    "/pharmacy/{pharmacy_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_pharmacy(
    pharmacy_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_pharmacy(pharmacy_id, current_user)
