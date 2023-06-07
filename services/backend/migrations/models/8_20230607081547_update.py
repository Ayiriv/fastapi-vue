from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "medicine" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL,
    "type" VARCHAR(32) NOT NULL,
    "prescription" VARCHAR(1) NOT NULL,
    "brand_id" INT NOT NULL REFERENCES "brand" ("id") ON DELETE CASCADE,
    "ingredients_id" INT NOT NULL REFERENCES "ingredients" ("id") ON DELETE CASCADE
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "medicine";"""
