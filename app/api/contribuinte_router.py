from fastapi import APIRouter, Depends
from app import enums

import sys
from app.infra.data.db import ResponseModel

from app.infra.data.repositories.contribuinte_repository import get_contribuintes
# from app.domain.models.contribuente import ContribuinteQuerry

router = APIRouter()


@router.get("/")
async def get_contribuints():
    contribuintes = await get_contribuintes()
    if contribuintes:
        return ResponseModel(contribuintes, "Deu boa!")
    return ResponseModel(contribuintes, "Deu ruim")

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
