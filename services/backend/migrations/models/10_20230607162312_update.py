from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "medicineonsale" RENAME COLUMN "Amount" TO "amount";
        ALTER TABLE "medicineonsale" ADD "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "medicineonsale" ADD "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "medicineonsale" ADD "price" INT NOT NULL;
        ALTER TABLE "medicinepresale" RENAME COLUMN "Arrive" TO "arrive";
        ALTER TABLE "medicinepresale" ADD "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "medicinepresale" RENAME COLUMN "Amount" TO "amount";
        ALTER TABLE "medicinepresale" ADD "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "medicinepresale" ADD "price" INT NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "medicineonsale" RENAME COLUMN "amount" TO "Amount";
        ALTER TABLE "medicineonsale" ADD "Amount" INT NOT NULL;
        ALTER TABLE "medicineonsale" DROP COLUMN "modified_at";
        ALTER TABLE "medicineonsale" DROP COLUMN "created_at";
        ALTER TABLE "medicineonsale" DROP COLUMN "price";
        ALTER TABLE "medicinepresale" RENAME COLUMN "arrive" TO "Arrive";
        ALTER TABLE "medicinepresale" RENAME COLUMN "amount" TO "Amount";
        ALTER TABLE "medicinepresale" ADD "Amount" INT NOT NULL;
        ALTER TABLE "medicinepresale" DROP COLUMN "modified_at";
        ALTER TABLE "medicinepresale" DROP COLUMN "created_at";
        ALTER TABLE "medicinepresale" DROP COLUMN "price";"""
