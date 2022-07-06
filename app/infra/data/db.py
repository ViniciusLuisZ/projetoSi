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
    print(contribuinte)
    return {
        'id': contribuinte["_id"],
        "evtInfoContri": contribuinte["evtInfoContri"],
    }


def ResponseModel(data, message):
    return {
        "quantity_find": len(data),
        "data": [data],
        "code": 200,
        "message": message,
    }

def DeleteResponseModel(data, message):
    return {
        "quantity_find": data.matched_count,
        "data": None,
        "code": 200,
        "message": message,
    }

def PostResponseModel(id_contribuente, message):
    return {
        "quantity_inserted": 1,
        "id_inserted": id_contribuente,
        "code": 200,
        "message": message
    }

def PostSofthouseResponseModel(cnpj, message):
    return {
        "quantity_inserted": 1,
        "cnpj_softhouse": cnpj,
        "code": 200,
        "message": message
    }