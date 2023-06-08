from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import MedicineOnsale
from src.schemas.onsale import OnsaleOutSchema
from src.schemas.token import Status
from tortoise.queryset import QuerySet


async def get_onsales():
    return await OnsaleOutSchema.from_queryset(MedicineOnsale.all())


async def get_onsale(onsale_id) -> OnsaleOutSchema:
    return await OnsaleOutSchema.from_queryset_single(MedicineOnsale.get(id=onsale_id))


async def search_onsale_by_name(onsale_name: str):
    onsales = await MedicineOnsale.filter(Mid__name__icontains=onsale_name)
    return [await OnsaleOutSchema.from_queryset_single(MedicineOnsale.get(id=onsale.id)) for onsale in onsales]


async def get_onsale_by_pharmacy(pharmacy_id: int):
    onsales = await MedicineOnsale.filter(Pid_id=pharmacy_id).all()
    return [await OnsaleOutSchema.from_queryset_single(MedicineOnsale.get(id=onsale.id)) for onsale in onsales]


async def create_onsale(onsale) -> OnsaleOutSchema: # new: delete current_user
    onsale_dict = onsale.dict(exclude_unset=True)
    onsale_obj = await MedicineOnsale.create(**onsale_dict)
    return await OnsaleOutSchema.from_tortoise_orm(onsale_obj)


async def update_onsale(onsale_id, onsale, current_user) -> OnsaleOutSchema:
    try:
        db_onsale = await OnsaleOutSchema.from_queryset_single(MedicineOnsale.get(id=onsale_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Medicine {onsale_id} not found")

    if db_onsale.Pid.owner.id == current_user.id:
        await MedicineOnsale.filter(id=onsale_id).update(**onsale.dict(exclude_unset=True))
        return await OnsaleOutSchema.from_queryset_single(MedicineOnsale.get(id=onsale_id))

    raise HTTPException(status_code=403, detail=f"Not ownerized to update")


async def delete_onsale(onsale_id, current_user) -> Status:
    try:
        db_onsale = await OnsaleOutSchema.from_queryset_single(MedicineOnsale.get(id=onsale_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Medicine {onsale_id} not found")

    if db_onsale.Pid.owner.id == current_user.id:
        deleted_count = await MedicineOnsale.filter(id=onsale_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Medicine {onsale_id} not found")
        return Status(message=f"Deleted onsale {onsale_id}")

    raise HTTPException(status_code=403, detail=f"Not ownerized to delete")


async def delete_onsales_by_pharmacy(pharmacy_id) -> Status: # new: delete current_user
    try:
        onsales = await MedicineOnsale.filter(Pid_id=pharmacy_id).all()
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"pharmacy id {pharmacy_id} not found")
    
    for onsale in onsales:
        await onsale.delete()
    return Status(message="MedicineOnsale deleted successfully.")
        

async def check_onsale_exists(Mid: int) -> bool:
    try:
        count = await MedicineOnsale.filter(Mid_id=Mid).count()
        return count > 0
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"medicine id {Mid} not found")
    