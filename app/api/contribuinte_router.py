from http import HTTPStatus
from fastapi import APIRouter, Request, HTTPException
from app.services import contribuente_validator
from app.infra.data.db import ResponseModel, DeleteResponseModel
from app.infra.data.repositories.contribuinte_repository import get_classContribuinte, get_contribuintes, get_contribuentes_details, delete_contribuente, get_situacoesPj
import app.exceptions as app_exceptions

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


@router.get('/situacaopj')
async def get_situacaopj():
    situacoesPj = get_situacoesPj()
    return ResponseModel(situacoesPj, "Deu boa!")


@router.get('/classificacaoContribuinte')
async def get_classContrib():
    classificacoes = await get_classContribuinte()
    return ResponseModel(classificacoes, "Deu boa!")

@router.post('/')
async def contribuente(info: Request):
    info_request = await info.json()
    try:
        contribuente_validator(info_request['evtInfoContri'])
        return ResponseModel(info_request, "Deu boa!")
    except app_exceptions.InvalidInput as err:
        raise HTTPException(HTTPStatus.UNPROCESSABLE_ENTITY, detail={
            'type': app_exceptions.ErrorType.INVALID_INPUT.name,
            'reason': str(err)
        })
