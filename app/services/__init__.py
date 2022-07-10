from app.services.validator import *


def contribuente_validator(infos):
    validate_classTrib(infos['ideContri']['tpInsc'],
                       infos['infoContri']['inclusao']['infoCadastro']['clasTrib'])
    validate_email(infos['infoContri']['inclusao']
                   ['infoCadastro']['contato']['email'])
    validate_cpf(infos['infoContri']['inclusao']
                 ['infoCadastro']['contato']['cpfCtt'])
    foneFixoOuCel(infos['infoContri']['inclusao']['infoCadastro']['contato']['foneCel'],
                infos['infoContri']['inclusao']['infoCadastro']['contato']['foneFixo'])
    validate_nrInsc(infos['ideContri']['tpInsc'], infos['ideContri']['nrInsc'],
                    infos['infoContri']['inclusao']['infoCadastro']['indSitPJ'])
    iniValid_fimValid(infos['infoContri']['inclusao']['idePeriodo']['iniValid'],
                      infos['infoContri']['inclusao']['idePeriodo']['fimValid'])


def put_contribuente_validator(infos):
    validate_classTrib(infos['ideContri']['tpInsc'],
                       infos['infoContri']['alteracao']['infoCadastro']['clasTrib'])
    validate_email(infos['infoContri']['alteracao']
                   ['infoCadastro']['contato']['email'])
    validate_cpf(infos['infoContri']['alteracao']
                 ['infoCadastro']['contato']['cpfCtt'])
    foneFixoOuCel(infos['infoContri']['alteracao']['infoCadastro']['contato']['foneCel'],
                infos['infoContri']['alteracao']['infoCadastro']['contato']['foneFixo'])
    validate_nrInsc(infos['ideContri']['tpInsc'], infos['ideContri']['nrInsc'],
                    infos['infoContri']['alteracao']['infoCadastro']['indSitPJ'])
    iniValid_fimValid(infos['infoContri']['alteracao']['idePeriodo']['iniValid'],
                      infos['infoContri']['alteracao']['idePeriodo']['fimValid'])
    iniValid_fimValid(infos['infoContri']['alteracao']['infoCadastro']['novaValidade']['iniValid'],
                      infos['infoContri']['alteracao']['infoCadastro']['novaValidade']['fimValid'])


def softhouse_validator(infos):
    validate_cnpj(infos['cnpjSoftHouse'])
    validate_foneCel(infos['telefone'])
    validate_email(infos['email'])
