from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "notes" ADD "contact" VARCHAR(225) NOT NULL;
        DROP TABLE IF EXISTS "pharmacy";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "notes" DROP COLUMN "contact";"""
