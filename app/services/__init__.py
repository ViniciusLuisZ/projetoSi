from app.services.validator import *


def contribuente_validator(infos):
    validate_classTrib(infos['ideContri']['tpInsc'],
                       infos['infoContri']['inclusao']['infoCadastro']['clasTrib'])
    validate_email(infos['infoContri']['inclusao']
                   ['infoCadastro']['contato']['email'])
    validate_cpf(infos['infoContri']['inclusao']
                 ['infoCadastro']['contato']['cpfCtt'])
    foneFixoOuCel(infos['infoContri']['inclusao'])
    validate_nrInsc(infos['ideContri']['tpInsc'], infos['ideContri']['nrInsc'],
                    infos['infoContri']['inclusao']['infoCadastro']['indSitPJ'])


def put_contribuente_validator(infos):
    validate_classTrib(infos['ideContri']['tpInsc'],
                       infos['infoContri']['alteracao']['infoCadastro']['clasTrib'])
    validate_email(infos['infoContri']['alteracao']
                   ['infoCadastro']['contato']['email'])
    validate_cpf(infos['infoContri']['alteracao']
                 ['infoCadastro']['contato']['cpfCtt'])
    foneFixoOuCel(infos['infoContri']['alteracao'])
    validate_nrInsc(infos['ideContri']['tpInsc'], infos['ideContri']['nrInsc'],
                    infos['infoContri']['alteracao']['infoCadastro']['indSitPJ'])


def softhouse_validator(infos):
    validate_cnpj(infos['cnpjSoftHouse'])
    validate_foneCel(infos['telefone'])
    validate_email(infos['email'])
