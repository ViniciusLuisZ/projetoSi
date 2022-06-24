from app import enums
from app.infra.data.db import database_r1000


async def get_contribuintes():
    return [x['evtInfoContri'] for x in database_r1000.Reinf.find({'evtInfoContri.infoContri.inclusao': {'$ne': None}})]


async def get_contribuentes_details(id):
    return [x['evtInfoContri'] for x in database_r1000.Reinf.find({'evtInfoContri.id': {'$eq': id}})]

async def delete_contribuente(id):
    data = database_r1000.Reinf.update_one({'evtInfoContri.id': {'$eq': id}}, {'$set': {'evtInfoContri.infoContri.exclusao.idePeriodo':{'iniValid': 'algo', 'fimValid': 'outroalgo'}}})
    return data

def get_situacoesPj():
    data = []
    for item in enums.indSitPJ:
        data.append({item: item.name})
    return data
