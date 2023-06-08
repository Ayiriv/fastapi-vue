from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Medicine
from src.schemas.medicines import MedicineOutSchema
from src.schemas.token import Status
from tortoise.queryset import QuerySet


async def get_medicines():
    return await MedicineOutSchema.from_queryset(Medicine.all())


async def get_medicine(medicine_id) -> MedicineOutSchema:
    return await MedicineOutSchema.from_queryset_single(Medicine.get(id=medicine_id))


async def search_medicine_by_name(medicine_name: str):
    medicines = await Medicine.filter(name__icontains=medicine_name)
    return [await MedicineOutSchema.from_queryset_single(Medicine.get(id=medicine.id)) for medicine in medicines]
