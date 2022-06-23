from app.api import api_router
from fastapi import APIRouter, Depends
from app import enums

# from app.domain.models.contribuente import ContribuinteQuerry

router = APIRouter()


@router.get("/")
def hello_world_root():
    return {"Hello": "World"}


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
