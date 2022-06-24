from app.infra.data.db import database_r1000


async def get_contribuintes():
    data = []
    for doc in database_r1000.Reinf.find({'evtInfoContri.infoContri.inclusao': {'$ne': None}}):
        doc['_id'] = str(doc['_id'])  # Convertendo _id para iterar cursor
        data.append(doc)
    return data

async def get_contribuentes_details(id):
    return [x['evtInfoContri'] for x in database_r1000.Reinf.find({'evtInfoContri.id': {'$eq': id}})]