from fastapi import APIRouter

from app.api import contribuinte_router

router = APIRouter()

router.include_router(contribuinte_router.router, tags=[
                      "contribuinte"], prefix="/contribuinte")
