from fastapi import FastAPI, Path, Depends
from app.contribuente.models import ContribuenteQuerry

app = FastAPI()

@app.get("/")
def hello_world_root():
    return {"Hello": "World"}


@app.post('/contribuente', response_model=ContribuenteResponse)
def contribuente(param: ContribuenteQuerry = Depends()):
    return
