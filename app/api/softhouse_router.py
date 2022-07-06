from http import HTTPStatus
from fastapi import APIRouter, Request, HTTPException

import app.exceptions as app_exceptions
from app.services import softhouse_validator
from app.infra.data.repositories.contribuinte_repository import (
    insert_softhouse
)
from app.infra.data.db import (
    PostSofthouseResponseModel
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