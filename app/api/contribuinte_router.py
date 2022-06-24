from fastapi import APIRouter, Depends
from app import enums

import sys
from app.infra.data.db import ResponseModel, DeleteResponseModel

from app.infra.data.repositories.contribuinte_repository import get_contribuintes, get_contribuentes_details, delete_contribuente
# from app.domain.models.contribuente import ContribuinteQuerry

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


@router.delete('/{id}')
async def delete_contribuente_by_id(id):
    resposta = await delete_contribuente(id)
    if resposta.matched_count > 0:
        return DeleteResponseModel(resposta, "Deu boa!")
    return DeleteResponseModel(resposta, "Deu ruim")


@router.get('/situpj/{lang}')
def getenum (lang:enums.indSitPJ):
    if (lang == enums.indSitPJ.extinto):
        return {"Pessoa Extinta"}
    elif (lang == enums.indSitPJ.fusao):    
        return {"Pessoa com Fusão"}
    elif (lang == enums.indSitPJ.situaNormal):
        return {"Pessoa Em Situação Normal"}
    elif (lang == enums.indSitPJ.cisao):
        return {"Pessao Em Cisao"}
    return {"Pessoa Incorporada"}

# @router.post('/', response_model="teste")
# def contribuente(param: ContribuinteQuerry = Depends()):
#     return
