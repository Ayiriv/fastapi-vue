from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import MedicineOnsale


OnsaleInSchema = pydantic_model_creator(
    MedicineOnsale, name="OnsaleIn", exclude_readonly=True)
OnsaleOutSchema = pydantic_model_creator(
    MedicineOnsale, name="Onsale", exclude =[
      "modified_at", "created_at"
    ]
)

class UpdateOnsale(BaseModel):
    amount: Optional[int]
    price: Optional[float]
