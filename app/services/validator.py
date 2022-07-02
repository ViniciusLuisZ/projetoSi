# esse script será usado para adicionar as regras de validação dos campos do reinf
from app.enums import tpInsc
import app.exceptions as app_exceptions
import re


def validate_contribuinte(data):
    validate_classTrib(data)
    validate_emailCtt(data)
    validate_cpfCtt(data)
    validate_nrInsc(data)
    validate_cnpjEFR(data)


def validate_classTrib(data):
    if data['ideContri']['tpInsc'] == 2:
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] not in [21, 22]:
            raise app_exceptions.InvalidInput("clasTrib inválido")
    if data['ideContri']['tpInsc'] == 1:
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] in [21, 22]:
            raise app_exceptions.InvalidInput("clasTrib inválido")


def validate_emailCtt(data):
    email = data['infoContri']['inclusao']['infoCadastro']['contato']['email']
    validate_email(email)


def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not(re.search(regex, email)):
        raise app_exceptions.InvalidInput("Email inválido")


def validate_cpfCtt(data):
    cpf = data['infoContri']['inclusao']['infoCadastro']['contato']['cpfCtt']
    validate_cpf(cpf)


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


def validate_nrInsc(data):
    tpInscricao = data['ideContri']['tpInsc']
    nrInsc = data['ideContri']['nrInsc']
    if(tpInscricao == tpInsc.cnpjTp):
        validate_cnpj(nrInsc)
    else:
        validate_cpf(nrInsc)


def validate_cnpjEFR(data):
    cnpj = data['infoContri']['inclusao']['infoCadastro']['infoEFR']['cnpjEFR']
    if(cnpj):
        validate_cnpj(cnpj)


def validate_cnpj(cnpj):
    cnpj = ''.join(re.findall('\d', str(cnpj)))
    if (not cnpj) or (len(cnpj) < 14):
        raise app_exceptions.InvalidInput("CNPJ com tamanho inválido")

    # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
    inteiros = map(int, cnpj)
    novo = inteiros[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(novo) < 14:
        r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        prod.insert(0, 6)

    # Se o número gerado coincidir com o número original, é válido
    if novo != inteiros:
        raise app_exceptions.InvalidInput("CNPJ inválido")


def validate_softHouse(data):
    validate_cnpj_softHouse(data)
    validate_email_softHouse(data)
    # Adicionar validação de telefone para softHouse


def validate_email_softHouse(data):
    email = data['email']
    if(email):
        validate_email(email)


def validate_cnpj_softHouse(data):
    cnpj = data['cnpjSoftHouse']
    validate_cnpj(cnpj)
