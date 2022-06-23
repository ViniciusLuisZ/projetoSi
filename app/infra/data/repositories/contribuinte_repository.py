from app.infra.data.db import database_r1000


async def get_contribuintes():
    # async for contribuinte in collection_reinf.find():
    #     contribuintes.append(contribuinte_helper(contribuinte))
    # return contribuintes
    return database_r1000.Reinf.find()
