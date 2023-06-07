from typing import Optional
from src.database.models import Ingredients
from src.database.models import Brand
from src.database.models import Medicine
from tortoise import Tortoise

async def init_data():
    # insert ingredients
    initial_ingredients = [
        {"name": "布洛芬", "symptom": "退烧镇痛"},
        {"name": "对乙酰氨基酚", "symptom": "退烧镇痛"},
        {"name": "中药药材", "symptom": "-"},
        {"name": "阿司匹林", "symptom": "退烧镇痛"},
    ]
    ingredients = []
    brands = []
    for ingredient in initial_ingredients:
        ing, _ = await Ingredients.get_or_create(**ingredient)
        ingredients.append(ing)
    
    # insert brands
    initial_brands = [
        {"name": "芬必得"}, {"name": "泰诺林"},
        {"name": "以岭"}, {"name": "拜耳"},
    ]
    for brand in initial_brands:
        br, _ = await Brand.get_or_create(**brand)
        brands.append(br)

    # insert medicines
    initial_medicines = [
        {"name": "布洛芬缓释胶囊", "type": "胶囊", "ingredients": ingredients[0], "prescription": "N", "brand": brands[0]},
        {"name": "对乙酰氨基酚混悬滴剂", "type": "滴剂", "ingredients": ingredients[1], "prescription": "N", "brand": brands[1]},
        {"name": "连花清瘟胶囊", "type": "胶囊", "ingredients": ingredients[2], "prescription": "N", "brand": brands[2]},
        {"name": "拜阿司匹灵肠溶片", "type": "片剂", "ingredients": ingredients[3], "prescription": "N", "brand": brands[3]},
    ]
    for medicine in initial_medicines:
        await Medicine.get_or_create(**medicine)


def register_tortoise(
    app,
    config: Optional[dict] = None,
    generate_schemas: bool = False,
) -> None:
    @app.on_event("startup")
    async def init_orm():
        await Tortoise.init(config=config)
        if generate_schemas:
            await Tortoise.generate_schemas()
        
        await init_data()

    @app.on_event("shutdown")
    async def close_orm():
        await Tortoise.close_connections()
