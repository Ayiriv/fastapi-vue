from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Pharmacies
from src.schemas.pharmacies import PharmacyOutSchema
from src.schemas.token import Status
from tortoise.queryset import QuerySet


async def get_pharmacies():
    return await PharmacyOutSchema.from_queryset(Pharmacies.all())


async def get_pharmacy(pharmacy_id) -> PharmacyOutSchema:
    return await PharmacyOutSchema.from_queryset_single(Pharmacies.get(id=pharmacy_id))


async def search_pharmacy_by_name(pharmacy_name: str):
    pharmacies = await Pharmacies.filter(name__icontains=pharmacy_name)
    return [await PharmacyOutSchema.from_queryset_single(Pharmacies.get(id=pharmacy.id)) for pharmacy in pharmacies]


async def get_pharmacy_by_owner(owner_id: int):# new: str->int
    pharmacies = await Pharmacies.filter(owner_id=owner_id).all()
    return [await PharmacyOutSchema.from_queryset_single(Pharmacies.get(id=pharmacy.id)) for pharmacy in pharmacies]


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


async def delete_pharmacies_by_owner(owner_id, current_user) -> Status:
    try:
        pharmacies = await Pharmacies.filter(owner_id=owner_id).all()
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"owner id {owner_id} not found")
    
    if owner_id == current_user.id:
        for pharmacy in pharmacies:
            await pharmacy.delete()
        return Status(message="Pharmacies deleted successfully.")
    
    raise HTTPException(status_code=403, detail=f"Not ownerized to delete")
