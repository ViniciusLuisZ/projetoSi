from app.api import api_router
from fastapi import APIRouter, Depends
# from app.domain.models.contribuente import ContribuinteQuerry

router = APIRouter()


@router.get("/")
def hello_world_root():
    return {"Hello": "World"}


# @router.post('/', response_model="teste")
# def contribuente(param: ContribuinteQuerry = Depends()):
#     return
