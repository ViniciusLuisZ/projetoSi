from app.services.validator import *


def contribuente_validator(infos):
    validate_classTrib(infos)
    validate_email(infos)
    validate_cpf(infos)
    foneFixoOuCel(infos)
    validate_foneCel(infos)
    validate_foneFixo(infos)
    validate_emailCtt(infos)
    validate_cpfCtt(infos)
    validate_nrInsc(infos)
    validate_cnpjEFR(infos)
