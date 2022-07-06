from app.services.validator import *


def contribuente_validator(infos):
    validate_classTrib(infos)
    validate_email(infos['infoContri']['inclusao']['infoCadastro']['contato']['email'])
    validate_cpf(infos['infoContri']['inclusao']['infoCadastro']['contato']['cpfCtt'])
    foneFixoOuCel(infos)
    validate_nrInsc(infos)

def softhouse_validator(infos):
    validate_cnpj(infos['cnpjSoftHouse'])
    validate_foneFixo(infos['telefone'])
    validate_email(infos['email'])

