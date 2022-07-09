from app import enums
from app.infra.data.db import database_r1000
import app.exceptions as app_exceptions
from bson.objectid import ObjectId


async def get_contribuintes():
    return [x['evtInfoContri'] for x in database_r1000.Reinf.find({'evtInfoContri.infoContri.inclusao': {'$ne': None}})]


async def get_contribuentes_details(id):
    return [x['evtInfoContri'] for x in database_r1000.Reinf.find({'evtInfoContri.id': {'$eq': id}})]


async def delete_contribuente(id):
    data = database_r1000.Reinf.update_one({'evtInfoContri.id': {'$eq': id}}, {'$set': {
        'evtInfoContri.infoContri.exclusao.idePeriodo': {'iniValid': 'algo', 'fimValid': 'outroalgo'}}})
    return data


def get_situacoesPj():
    data = []
    for item in enums.indSitPJ:
        data.append({item: item.name})
    return data


async def get_classContribuinte():
    data = []
    dataFinal = []
    cursor = database_r1000.Tabela8.find()
    for item in cursor:
        item['_id'] = str(item['_id'])  # Convertendo _id para iterar cursor
        data.append(item)
    for i in data[0]:
        if(i != "_id"):
            dataFinal.append({int(i): data[0][i]})
    return dataFinal


def insert_contribuente(evtInfoContri):
    try:
        resultado = database_r1000.Reinf.insert_one(evtInfoContri)
    except Exception as err:
        raise app_exceptions.DatabaseError(f'Database query error: {err}')


def insert_softhouse(infoSofthouse):
    try:
        resultado = database_r1000.softHouse.insert_one(infoSofthouse)
        return str(resultado.inserted_id)
    except Exception as err:
        raise app_exceptions.DatabaseError(f'Database query error: {err}')


async def delete_softhouse(id):
    softhouse = database_r1000.softHouse.find_one({"_id": ObjectId(id)})
    if softhouse:
        database_r1000.softHouse.delete_one({'_id': ObjectId(id)})
        return True
    return False


async def get_softhouse_details(id):
    data = []
    cursor = database_r1000.softHouse.find({"_id": ObjectId(id)})
    for item in cursor:
        item['_id'] = str(item['_id'])  # Convertendo _id para iterar cursor
        data.append(item)
    return data


def update_softhouse(id, infoSofthouse):
    try:
        del(infoSofthouse['id'])
        resultado = database_r1000.softHouse.update_one(
            {"_id": ObjectId(id)}, {"$set": infoSofthouse})
    except Exception as err:
        raise app_exceptions.DatabaseError(f'Database query error: {err}')
