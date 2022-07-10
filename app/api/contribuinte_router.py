import copy
from http import HTTPStatus
import uuid
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
    get_contribuintes_details,
    delete_contribuinte,
    get_situacoesPj,
    insert_contribuinte,
    update_contribuinte
)
import app.exceptions as app_exceptions
from app.services import contribuinte_validator, put_contribuinte_validator
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
    detalhes = await get_contribuintes_details(id)
    if detalhes:
        return ResponseModel(detalhes, "Deu boa!")
    return ResponseModel(detalhes, "Deu ruim")


@router.delete('/{id}')
async def delete_contribuinte_by_id(id):
    resposta = await delete_contribuinte(id)
    if resposta.matched_count > 0:
        contribuinte = await get_contribuintes_details(id)
        await push_to_queue(contribuinte[0])
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
async def contribuinte(info: Request):
    info_request = await info.json()
    try:
        contribuinte_validator(info_request['evtInfoContri'])
        info_request['evtInfoContri']['id'] = str(uuid.uuid4())
        insert_contribuinte(info_request)
        await push_to_queue(info_request['evtInfoContri'])
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
        contribuinte = await get_contribuintes_details(id)
        if(contribuinte):
            put_contribuinte_validator(info_request['evtInfoContri'])
            update_contribuinte(id, info_request)
            await push_to_queue(info_request['evtInfoContri'])
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
