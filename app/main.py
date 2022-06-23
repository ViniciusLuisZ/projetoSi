import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.api_router import router
from app.core.config import settings
from app import enums

# Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, docs_url="/docs", redoc_url='/re-docs',
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        description="Reinf Api desenvolvida com fastapi."
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)
    application.include_router(router, prefix=settings.API_PREFIX)
    # application.add_exception_handler(CustomException, http_exception_handler)

    return application


app = get_application()
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get('/situpj/{lang}')
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