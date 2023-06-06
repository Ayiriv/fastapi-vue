from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "pharmacies" ALTER COLUMN "addr" TYPE VARCHAR(225) USING "addr"::VARCHAR(225);
        ALTER TABLE "pharmacies" ALTER COLUMN "addr" TYPE VARCHAR(225) USING "addr"::VARCHAR(225);
        ALTER TABLE "pharmacies" ALTER COLUMN "addr" TYPE VARCHAR(225) USING "addr"::VARCHAR(225);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "pharmacies" ALTER COLUMN "addr" TYPE TEXT USING "addr"::TEXT;
        ALTER TABLE "pharmacies" ALTER COLUMN "addr" TYPE TEXT USING "addr"::TEXT;
        ALTER TABLE "pharmacies" ALTER COLUMN "addr" TYPE TEXT USING "addr"::TEXT;"""
