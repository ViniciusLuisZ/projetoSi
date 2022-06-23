from pymongo import MongoClient
from app.core.config import settings
client = MongoClient(settings.DATABASE_URL)
database_r1000 = client["R-1000"]

# Collections:
# Tabela8
# Reinf
# softHouse


# helpers


def contribuinte_helper(contribuinte) -> dict:
    return {
        "id": contribuinte["id"],
        "ideEvento": contribuinte["ideEvento"],
        "ideContri": contribuinte["ideContri"],
        "infoContri": contribuinte["infoContri"],
    }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
