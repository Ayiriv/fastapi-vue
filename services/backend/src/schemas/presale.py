from typing import Optional
from datetime import datetime

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import MedicinePresale


PresaleInSchema = pydantic_model_creator(
    MedicinePresale, name="PresaleIn", exclude_readonly=True)
PresaleOutSchema = pydantic_model_creator(
    MedicinePresale, name="Presale", exclude =[
      "modified_at", "created_at"
    ]
)

class UpdatePresale(BaseModel):
    amount: Optional[int]
    price: Optional[float]
    arrive: Optional[datetime]
