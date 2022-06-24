from fastapi import APIRouter, Depends
from app.infra.data.db import ResponseModel
from app.infra.data.repositories.contribuinte_repository import get_contribuintes, get_contribuentes_details, get_situacoesPj
router = APIRouter()


@router.get("/")
async def get_contribuints():
    contribuintes = await get_contribuintes()
    if contribuintes:
        return ResponseModel(contribuintes, "Deu boa!")
    return ResponseModel(contribuintes, "Deu ruim")


@router.get("/details/{id}")
async def get_contribuents_details(id):
    detalhes = await get_contribuentes_details(id)
    if detalhes:
        return ResponseModel(detalhes, "Deu boa!")
    return ResponseModel(detalhes, "Deu ruim")


@router.get('/situacaopj')
async def get_situacaopj():
    situacoesPj = get_situacoesPj()
    return situacoesPj

# @router.post('/', response_model="teste")
# def contribuente(param: ContribuinteQuerry = Depends()):
#     return
