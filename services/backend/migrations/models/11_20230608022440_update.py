from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "medicineonsale" ALTER COLUMN "price" TYPE DOUBLE PRECISION USING "price"::DOUBLE PRECISION;
        ALTER TABLE "medicineonsale" ALTER COLUMN "price" TYPE DOUBLE PRECISION USING "price"::DOUBLE PRECISION;
        ALTER TABLE "medicineonsale" ALTER COLUMN "price" TYPE DOUBLE PRECISION USING "price"::DOUBLE PRECISION;
        ALTER TABLE "medicineonsale" ALTER COLUMN "price" TYPE DOUBLE PRECISION USING "price"::DOUBLE PRECISION;
        ALTER TABLE "medicinepresale" ALTER COLUMN "price" TYPE DOUBLE PRECISION USING "price"::DOUBLE PRECISION;
        ALTER TABLE "medicinepresale" ALTER COLUMN "price" TYPE DOUBLE PRECISION USING "price"::DOUBLE PRECISION;
        ALTER TABLE "medicinepresale" ALTER COLUMN "price" TYPE DOUBLE PRECISION USING "price"::DOUBLE PRECISION;
        ALTER TABLE "medicinepresale" ALTER COLUMN "price" TYPE DOUBLE PRECISION USING "price"::DOUBLE PRECISION;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "medicineonsale" ALTER COLUMN "price" TYPE INT USING "price"::INT;
        ALTER TABLE "medicineonsale" ALTER COLUMN "price" TYPE INT USING "price"::INT;
        ALTER TABLE "medicineonsale" ALTER COLUMN "price" TYPE INT USING "price"::INT;
        ALTER TABLE "medicineonsale" ALTER COLUMN "price" TYPE INT USING "price"::INT;
        ALTER TABLE "medicinepresale" ALTER COLUMN "price" TYPE INT USING "price"::INT;
        ALTER TABLE "medicinepresale" ALTER COLUMN "price" TYPE INT USING "price"::INT;
        ALTER TABLE "medicinepresale" ALTER COLUMN "price" TYPE INT USING "price"::INT;
        ALTER TABLE "medicinepresale" ALTER COLUMN "price" TYPE INT USING "price"::INT;"""
