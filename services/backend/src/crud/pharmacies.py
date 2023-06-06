from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Pharmacies
from src.schemas.pharmacies import PharmacyOutSchema
from src.schemas.token import Status


async def get_pharmacies():
    return await PharmacyOutSchema.from_queryset(Pharmacies.all())


async def get_pharmacy(pharmacy_id) -> PharmacyOutSchema:
    return await PharmacyOutSchema.from_queryset_single(Pharmacies.get(id=pharmacy_id))

async def search_pharmacy_by_name(pharmacy_name: str):
    pharmacy = await Pharmacies.filter(name__icontains=pharmacy_name)
    print(pharmacy)
    return await PharmacyOutSchema.from_queryset(pharmacy)


async def create_pharmacy(pharmacy, current_user) -> PharmacyOutSchema:
    pharmacy_dict = pharmacy.dict(exclude_unset=True)
    pharmacy_dict["owner_id"] = current_user.id
    pharmacy_obj = await Pharmacies.create(**pharmacy_dict)
    return await PharmacyOutSchema.from_tortoise_orm(pharmacy_obj)


async def update_pharmacy(pharmacy_id, pharmacy, current_user) -> PharmacyOutSchema:
    try:
        db_pharmacy = await PharmacyOutSchema.from_queryset_single(Pharmacies.get(id=pharmacy_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Pharmacy {pharmacy_id} not found")

    if db_pharmacy.owner.id == current_user.id:
        await Pharmacies.filter(id=pharmacy_id).update(**pharmacy.dict(exclude_unset=True))
        return await PharmacyOutSchema.from_queryset_single(Pharmacies.get(id=pharmacy_id))

    raise HTTPException(status_code=403, detail=f"Not ownerized to update")


async def delete_pharmacy(pharmacy_id, current_user) -> Status:
    try:
        db_pharmacy = await PharmacyOutSchema.from_queryset_single(Pharmacies.get(id=pharmacy_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Pharmacy {pharmacy_id} not found")

    if db_pharmacy.owner.id == current_user.id:
        deleted_count = await Pharmacies.filter(id=pharmacy_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Pharmacy {pharmacy_id} not found")
        return Status(message=f"Deleted pharmacy {pharmacy_id}")

    raise HTTPException(status_code=403, detail=f"Not ownerized to delete")
