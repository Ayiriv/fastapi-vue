from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.presale as crud
from src.auth.jwthandler import get_current_user
from src.schemas.presale import PresaleOutSchema, PresaleInSchema, UpdatePresale
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/presales",
    response_model=List[PresaleOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_presales():
    return await crud.get_presales()


@router.get(
    "/presale/{presale_id}",
    response_model=PresaleOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_presale(presale_id: int) -> PresaleOutSchema:
    try:
        return await crud.get_presale(presale_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )
    

@router.get(
    "/presale/search/{name}",
    response_model=List[PresaleOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def search_presale_by_name(name: str) -> List[PresaleOutSchema]:
    try:
        print(name)
        return await crud.search_presale_by_name(name)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )
    

@router.get(
    "/presale/by-pharmacy/{pharmacy_id}",
    response_model=List[PresaleOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_presale_by_pharmacy(pharmacy_id: int) -> List[PresaleOutSchema]:
    try:
        print(pharmacy_id)
        return await crud.get_presale_by_pharmacy(pharmacy_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pharmacy does not exist",
        )
    

@router.get(
    "/presale/exist/{medicine_id}",
    response_model=bool,
    dependencies=[Depends(get_current_user)],
)
async def check_presale_exists(medicine_id: int) -> bool:
    try:
        return await crud.check_presale_exists(medicine_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Medicine does not exist",
        )


@router.post(
    "/presales", response_model=PresaleOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_presale(
    presale: PresaleInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> PresaleOutSchema:
    return await crud.create_presale(presale)


@router.patch(
    "/presale/{presale_id}",
    dependencies=[Depends(get_current_user)],
    response_model=PresaleOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_presale(
    presale_id: int,
    presale: UpdatePresale,
    current_user: UserOutSchema = Depends(get_current_user),
) -> PresaleOutSchema:
    return await crud.update_presale(presale_id, presale, current_user)


@router.delete(
    "/presale/{presale_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_presale(
    presale_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_presale(presale_id, current_user)


@router.delete(
    "/presale/by-pharmacy/{pharmacy_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_presales_by_pharmacy(
    pharmacy_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_presales_by_pharmacy(pharmacy_id)

