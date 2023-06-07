from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import MedicinePresale
from src.schemas.presale import PresaleOutSchema
from src.schemas.token import Status
from tortoise.queryset import QuerySet


async def get_presales():
    return await PresaleOutSchema.from_queryset(MedicinePresale.all())


async def get_presale(presale_id) -> PresaleOutSchema:
    return await PresaleOutSchema.from_queryset_single(MedicinePresale.get(id=presale_id))


async def search_presale_by_name(presale_name: str):
    presales = await MedicinePresale.filter(Mid_name__icontains=presale_name)
    return [await PresaleOutSchema.from_queryset_single(MedicinePresale.get(id=presale.id)) for presale in presales]


async def get_presale_by_pharmacy(pharmacy_id: int):
    presales = await MedicinePresale.filter(Pid_id=pharmacy_id).all()
    return [await PresaleOutSchema.from_queryset_single(MedicinePresale.get(id=presale.id)) for presale in presales]


async def create_presale(presale) -> PresaleOutSchema: # new: delete current_user
    presale_dict = presale.dict(exclude_unset=True)
    presale_obj = await MedicinePresale.create(**presale_dict)
    return await PresaleOutSchema.from_tortoise_orm(presale_obj)


async def update_presale(presale_id, presale, current_user) -> PresaleOutSchema:
    try:
        db_presale = await PresaleOutSchema.from_queryset_single(MedicinePresale.get(id=presale_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Medicine {presale_id} not found")

    if db_presale.Pid.owner.id == current_user.id:
        await MedicinePresale.filter(id=presale_id).update(**presale.dict(exclude_unset=True))
        return await PresaleOutSchema.from_queryset_single(MedicinePresale.get(id=presale_id))

    raise HTTPException(status_code=403, detail=f"Not ownerized to update")


async def delete_presale(presale_id, current_user) -> Status:
    try:
        db_presale = await PresaleOutSchema.from_queryset_single(MedicinePresale.get(id=presale_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Medicine {presale_id} not found")

    if db_presale.Pid.owner.id == current_user.id:
        deleted_count = await MedicinePresale.filter(id=presale_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Medicine {presale_id} not found")
        return Status(message=f"Deleted presale {presale_id}")

    raise HTTPException(status_code=403, detail=f"Not ownerized to delete")


async def delete_presales_by_pharmacy(pharmacy_id) -> Status:
    try:
        presales = await MedicinePresale.filter(Pid_id=pharmacy_id).all()
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"pharmacy id {pharmacy_id} not found")
    
    for presale in presales:
        await presale.delete()
    return Status(message="MedicinePresale deleted successfully.")
        
    