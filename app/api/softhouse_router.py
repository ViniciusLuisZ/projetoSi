from http import HTTPStatus
from fastapi import APIRouter, Request, HTTPException

import app.exceptions as app_exceptions
from app.services import softhouse_validator
from app.infra.data.repositories.contribuinte_repository import (
    delete_softhouse,
    get_softhouse_details,
    insert_softhouse
)
from app.infra.data.db import (
    DeleteSofthouseResponseModel,
    ErrorDeleteSofthouseResponseModel,
    ErrorResponseModel,
    PostSofthouseResponseModel,
    ResponseModel
)

router = APIRouter()


@router.post('/')
async def contribuente(info: Request):
    info_request = await info.json()
    try:
        softhouse_validator(info_request)
        insert_softhouse(info_request)
        return PostSofthouseResponseModel(info_request['cnpjsofthouse'], "Deu boa!")
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


@router.get("/details/{id}")
async def get_contribuents_details(id):
    softhouse = await get_softhouse_details(id)
    if softhouse:
        return ResponseModel(softhouse, "Deu boa!")
    return ErrorResponseModel("Deu ruim")


@router.delete('/{id}')
async def delete_softhouse_by_id(id):
    deleted_softhouse = await delete_softhouse(id)
    if (deleted_softhouse):
        return DeleteSofthouseResponseModel(id, "Deu boa!")
    return ErrorDeleteSofthouseResponseModel("Ocorreu um erro ao tentar deletar o id: {0}".format(id))
