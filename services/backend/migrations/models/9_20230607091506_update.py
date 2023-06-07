from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "medicineonsale" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "Amount" INT NOT NULL,
    "Mid_id" INT NOT NULL REFERENCES "medicine" ("id") ON DELETE CASCADE,
    "Pid_id" INT NOT NULL REFERENCES "pharmacies" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_medicineons_Pid_id_a41ffd" UNIQUE ("Pid_id", "Mid_id")
);;
        CREATE TABLE IF NOT EXISTS "medicinepresale" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "Amount" INT NOT NULL,
    "Arrive" TIMESTAMPTZ NOT NULL,
    "Mid_id" INT NOT NULL REFERENCES "medicine" ("id") ON DELETE CASCADE,
    "Pid_id" INT NOT NULL REFERENCES "pharmacies" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_medicinepre_Pid_id_37d154" UNIQUE ("Pid_id", "Mid_id")
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "medicineonsale";
        DROP TABLE IF EXISTS "medicinepresale";"""
