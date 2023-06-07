from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import MedicineOnsale


OnsaleInSchema = pydantic_model_creator(
    MedicineOnsale, name="OnsaleIn", exclude=["Pid_id","Mid_id"], exclude_readonly=True)
OnsaleOutSchema = pydantic_model_creator(
    MedicineOnsale, name="Onsale", exclude =[
      "modified_at", "created_at"
    ]
)

class UpdateOnsale(BaseModel):
    name: Optional[str]
    contact: Optional[str]
    addr: Optional[str]
