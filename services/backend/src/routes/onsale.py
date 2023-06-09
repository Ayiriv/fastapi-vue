from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.onsale as crud
from src.auth.jwthandler import get_current_user
from src.schemas.onsale import OnsaleOutSchema, OnsaleInSchema, UpdateOnsale
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/onsales",
    response_model=List[OnsaleOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_onsales():
    return await crud.get_onsales()


@router.get(
    "/onsale/{onsale_id}",
    response_model=OnsaleOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_onsale(onsale_id: int) -> OnsaleOutSchema:
    try:
        return await crud.get_onsale(onsale_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )
    

@router.get(
    "/onsale/search/{name}",
    response_model=List[OnsaleOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def search_onsale_by_name(name: str) -> List[OnsaleOutSchema]:
    try:
        print(name)
        return await crud.search_onsale_by_name(name)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )
    

@router.get(
    "/onsale/search/symptom/{symptom}",
    response_model=List[OnsaleOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def search_onsale_by_symptom(symptom: str) -> List[OnsaleOutSchema]:
    try:
        return await crud.search_onsale_by_symptom(symptom)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )


@router.get(
    "/onsale/by-pharmacy/{pharmacy_id}",
    response_model=List[OnsaleOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_onsale_by_pharmacy(pharmacy_id: int) -> List[OnsaleOutSchema]:
    try:
        print(pharmacy_id)
        return await crud.get_onsale_by_pharmacy(pharmacy_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )
    

@router.get(
    "/onsale/exist/{medicine_id}",
    response_model=bool,
    dependencies=[Depends(get_current_user)],
)
async def check_onsale_exists(medicine_id: int) -> bool:
    try:
        return await crud.check_onsale_exists(medicine_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Medicine does not exist",
        )


@router.post(
    "/onsales", response_model=OnsaleOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_onsale(
    onsale: OnsaleInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> OnsaleOutSchema:
    return await crud.create_onsale(onsale)


@router.patch(
    "/onsale/{onsale_id}",
    dependencies=[Depends(get_current_user)],
    response_model=OnsaleOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_onsale(
    onsale_id: int,
    onsale: UpdateOnsale,
    current_user: UserOutSchema = Depends(get_current_user),
) -> OnsaleOutSchema:
    return await crud.update_onsale(onsale_id, onsale, current_user)


@router.delete(
    "/onsale/{onsale_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_onsale(
    onsale_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_onsale(onsale_id, current_user)


@router.delete(
    "/onsale/by-pharmacy/{pharmacy_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_onsales_by_pharmacy(
    pharmacy_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_onsales_by_pharmacy(pharmacy_id)

