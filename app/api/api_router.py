from fastapi import APIRouter

from app.api import contribuinte_router, softhouse_router

router = APIRouter()

router.include_router(contribuinte_router.router, tags=[
                      "contribuinte"], prefix="/contribuinte")

router.include_router(softhouse_router.router, tags=[
                      "softhouse"], prefix="/softhouse")
