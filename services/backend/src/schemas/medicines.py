from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Medicine


MedicineOutSchema = pydantic_model_creator(
    Medicine, name="Medicine"
)


