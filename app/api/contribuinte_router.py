import copy
from http import HTTPStatus
from fastapi import APIRouter, Request, HTTPException
from app.infra.data.db import (
    ErrorResponseModel,
    PutResponseModel,
    ResponseModel,
    DeleteResponseModel,
    PostResponseModel
)
from app.infra.data.repositories.contribuinte_repository import (
    get_classContribuinte,
    get_contribuintes,
    get_contribuentes_details,
    delete_contribuente,
    get_situacoesPj,
    insert_contribuente,
    update_contribuinte
)
import app.exceptions as app_exceptions
from app.services import contribuente_validator, put_contribuente_validator
from app.services.rabbitmq.producer import push_to_queue
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
        insert_contribuente(info_request)
        return PostResponseModel(info_request['evtInfoContri']['id'], "Deu boa!")
    except app_exceptions.InvalidInput as err:
        raise HTTPException(HTTPStatus.UNPROCESSABLE_ENTITY, detail={
            'type': app_exceptions.ErrorType.INVALID_INPUT.name,
            'reason': str(err)
        })
    except app_exceptions.DatabaseError as err:
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail={
            'type': app_exceptions.ErrorType.SERVER_ERROR.name,
            'reason': str(err)
        })


@router.put('/')
async def put_contribuinte_by_evtInfoContri_id(info: Request):
    info_request = await info.json()
    id = copy.deepcopy(info_request['evtInfoContri']['id'])
    try:
        contribuinte = await get_contribuentes_details(id)
        if(contribuinte):
            put_contribuente_validator(info_request['evtInfoContri'])
            update_contribuinte(id, info_request)
            return PutResponseModel(id, "Deu boa!")
        return ErrorResponseModel("Deu ruim")
    except app_exceptions.InvalidInput as err:
        raise HTTPException(HTTPStatus.UNPROCESSABLE_ENTITY, detail={
            'type': app_exceptions.ErrorType.INVALID_INPUT.name,
            'reason': str(err)
        })
    except app_exceptions.DatabaseError as err:
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, detail={
            'type': app_exceptions.ErrorType.SERVER_ERROR.name,
            'reason': str(err)
        })


# endpoint criado para teste da fila do rabbitmq
@router.post('/send-message')
async def send_message(message: object):
    await push_to_queue(
        {"message": message}
    )
    return {"status": "ok"}
