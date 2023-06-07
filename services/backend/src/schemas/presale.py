from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import MedicinePresale


PresaleInSchema = pydantic_model_creator(
    MedicinePresale, name="PresaleIn", exclude=["Pid_id","Mid_id"], exclude_readonly=True)
PresaleOutSchema = pydantic_model_creator(
    MedicinePresale, name="Presale", exclude =[
      "modified_at", "created_at"
    ]
)

class UpdatePresale(BaseModel):
    name: Optional[str]
    contact: Optional[str]
    addr: Optional[str]
