# esse script será usado para adicionar as regras de validação dos campos do reinf
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



# método que verifica somente o que foi preenchido (*deve ser chamado primeiro para validação de telefones)
def foneFixoOuCel(data):
    foneFixo = data['evtInfoContri']['infoContri']['inclusao']['infoCadastro']['contato']['foneFixo']
    foneCel = data['evtInfoContri']['infoContri']['inclusao']['infoCadastro']['contato']['foneCel']

    if foneCel:
        validate_foneCel(foneCel)
    if foneFixo:
        validate_foneFixo(foneFixo)
    if ((not foneCel) and (not foneFixo)):
        raise app_exceptions.InvalidInput("É necessário informar pelo menos um telefone")



#método que valida celular (se o campo tiver sido preenchido)
def validate_foneCel(data):
    foneCel = data['evtInfoContri']['infoContri']['inclusao']['infoCadastro']['contato']['foneCel']

    # regex para celulares com apenas números e mínimo de 11 dígitos (ddd + 9 + número)
    exp = '^[1-9]{2}? ?(?:[2-8]|9[1-9])[0-9]{3}?[0-9]{4}$'

    foneCel = re.findall(exp, foneCel)
    if not foneCel:
        raise app_exceptions.Invalidinput("Celular não aceito!")
        
    
#valida telefone fixo (se o campo tiver sido preenchido)
def validate_foneFixo(data):
    foneFixo = data['evtInfoContri']['infoContri']['inclusao']['infoCadastro']['contato']['foneFixo']

    # regex para telefone fixo com apenas números e mínimo de 10 dígitos (ddd  + número)
    exp = '^[1-9]{2}([2-8]{4})([0-9]{4})$'

    foneFixo = re.findall(exp, foneFixo)
    if not foneFixo:
        raise app_exceptions.Invalidinput("Telefone Fixo não aceito!")







    

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
