### esse script será usado para adicionar as regras de validação dos campos do reinf
import app.exceptions as app_exceptions
import re

def validate_classTrib(data):
    if data['ideContri']['tpInsc'] == 2:
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] not in [21, 22]:
            raise app_exceptions.InvalidInput("clasTrib inválido")
    if data['ideContri']['tpInsc'] == 1:
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] in [21, 22]:
            raise app_exceptions.InvalidInput("clasTrib inválido")

def validate_email(data):
    email = data['infoContri']['inclusao']['infoCadastro']['contato']['email']
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not(re.search(regex,email)):
        raise app_exceptions.InvalidInput("Email inválido")

def validate_cpf(data):
    cpf = data['infoContri']['inclusao']['infoCadastro']['contato']['cpfCtt']
    if len(cpf) != 11:
        raise app_exceptions.InvalidInput("CPF com tamanho inválido")
    try:
        for i in range(9,11):
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







    

