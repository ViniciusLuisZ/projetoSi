# esse script será usado para adicionar as regras de validação dos campos do reinf
from itertools import cycle
from app.enums import indSitPJ, tpInsc
import app.exceptions as app_exceptions
import re


def validate_classTrib(data):
    if data['ideContri']['tpInsc'] == 2:
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] not in [21, 22]:
            raise app_exceptions.InvalidInput("clasTrib inválido")
    if data['ideContri']['tpInsc'] == 1:
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] in [21, 22]:
            raise app_exceptions.InvalidInput("clasTrib inválido")


def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not(re.search(regex, email)):
        raise app_exceptions.InvalidInput("Email inválido")


def validate_cpf(cpf):
    if len(cpf) != 11:
        raise app_exceptions.InvalidInput(
            "CPF com tamanho inválido")
    try:
        for i in range(9, 11):
            value = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if str(digit) != cpf[i]:
                raise app_exceptions.InvalidInput("CPF inválido")
    except Exception:
        raise app_exceptions.InvalidInput("CPF inválido")


# método que verifica somente o que foi preenchido (*deve ser chamado primeiro para validação de telefones)
def foneFixoOuCel(data):
    foneFixo = data['infoCadastro']['contato']['foneFixo']
    foneCel = data['infoCadastro']['contato']['foneCel']

    if foneCel:
        validate_foneCel(foneCel)
    if foneFixo:
        validate_foneFixo(foneFixo['infoCadastro']['contato']['foneFixo'])
    if ((not foneCel) and (not foneFixo)):
        raise app_exceptions.InvalidInput(
            "É necessário informar pelo menos um telefone")


# método que valida celular (se o campo tiver sido preenchido)
def validate_foneCel(data):

    # regex para celulares com apenas números e mínimo de 11 dígitos (ddd + 9 + número)
    exp = '^[1-9]{2}? ?(?:[2-8]|9[1-9])[0-9]{3}?[0-9]{4}$'

    foneCel = re.findall(exp, data)
    if not foneCel:
        raise app_exceptions.InvalidInput("Celular não aceito!")


# valida telefone fixo (se o campo tiver sido preenchido)
def validate_foneFixo(foneFixo):
    # regex para telefone fixo com apenas números e mínimo de 10 dígitos (ddd  + número)
    exp = '^[1-9]{2}([2-8]{4})([0-9]{4})$'

    foneFixo = re.findall(exp, foneFixo)
    if not foneFixo:
        raise app_exceptions.InvalidInput("Telefone Fixo não aceito!")


def validate_nrInsc(data):
    tpInscricao = data['ideContri']['tpInsc']
    nrInsc = data['ideContri']['nrInsc']
    indSitPessoaJuridica = data['infoContri']['inclusao']['infoCadastro']['indSitPJ']

    if(tpInscricao == tpInsc.cnpjTp):
        if(indSitPessoaJuridica == indSitPJ.incorporacao):
            raise app_exceptions.InvalidInput(
                "CNPJ não poderá pertencer a pessoa jurídica inapta")
        else:
            validate_cnpj(nrInsc)
    else:
        validate_cpf(nrInsc)


def validate_cnpj(cnpj):
    cnpj = ''.join(re.findall('\d', str(cnpj)))
    if (not cnpj) or (len(cnpj) < 14) or (len(cnpj) > 14):
        raise app_exceptions.InvalidInput("CNPJ com tamanho inválido")

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False

# esse método valida as datas conferindo se estão no formato correto (YYYY-MM)
# também verifica as datas para garantir que a data_fim seja maior que a data_inicio


def iniValid_fimValid(data):
    iniValid = data['idePeriodo']['iniValid']
    fimValid = data['idePeriodo']['fimValid']

    # regex para datas no formato (YYYY-MM)
    exp = '^\d{4}\-(0?[1-9]|1[012])$'

    iniValid = re.findall(exp, iniValid)
    if not iniValid:
        raise app_exceptions.Invalidinput("Data de início inválida")
    fimValid = re.findall(exp, fimValid)
    if not fimValid:
        raise app_exceptions.Invalidinput("Data de fim inválida")

    refIniValid = str(iniValid.split('-'))
    refFimValid = str(fimValid.split('-'))

    if refFimValid[0] < refIniValid[0]:
        raise app_exceptions.Invalidinput('Ano de Data Fim não pode ser menor')
    elif refFimValid[0] == refIniValid[0]:
        if refFimValid[1] < refIniValid[1]:
            raise app_exceptions.Invalidinput(
                'Mês de Data Fim não pode ser menor')
