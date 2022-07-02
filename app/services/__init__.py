from app.services.validator import *

def contribuente_validator(infos):
    validate_classTrib(infos)
    validate_email(infos)
    validate_cpf(infos)
