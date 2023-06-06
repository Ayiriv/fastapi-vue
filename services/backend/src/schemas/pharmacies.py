from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Pharmacies


PharmacyInSchema = pydantic_model_creator(
    Pharmacies, name="PharmacyIn", exclude=["owner_id"], exclude_readonly=True)
PharmacyOutSchema = pydantic_model_creator(
    Pharmacies, name="Pharmacy", exclude =[
      "modified_at", "owner.password", "owner.created_at", "owner.modified_at"
    ]
)


class UpdatePharmacy(BaseModel):
    name: Optional[str]
    contact: Optional[str]
    addr: Optional[str]
