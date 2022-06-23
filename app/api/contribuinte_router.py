from fastapi import APIRouter, Depends
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

# @router.post('/', response_model="teste")
# def contribuente(param: ContribuinteQuerry = Depends()):
#     return
