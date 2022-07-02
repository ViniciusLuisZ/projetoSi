from app.services.validator import *


def contribuente_validator(infos):
    validate_classTrib(infos)
    validate_emailCtt(infos)
    validate_cpfCtt(infos)
    validate_nrInsc(infos)
    validate_cnpjEFR(infos)
