### esse script será usado para adicionar as regras de validação dos campos do reinf
import app.exceptions as app_exceptions
import re

def validate_classTrib(data):
    if data['ideContri']['tpInsc'] == 2:
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] not in [21, 22]:
            raise app_exceptions.Invalidinput("clasTrib inválido")
    if data['ideContri']['tpInsc'] == 1:
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] in [21, 22]:
            raise app_exceptions.Invalidinput("clasTrib inválido")

def validate_email(data):
    email = data['infoContri']['inclusao']['infoCadastro']['contato']['email']
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not(re.search(regex,email)):
        raise app_exceptions.Invalidinput("Email inválido")

def validate_cpf(data):
    cpf = data['infoContri']['inclusao']['infoCadastro']['contato']['cpfCtt']
    if len(cpf) != 11:
        raise app_exceptions.Invalidinput("CPF com tamanho inválido")
    for i in range(9,11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            raise app_exceptions.Invalidinput("CPF inválido")


def validate_foneCel(data):
    foneCel = data['infoContri']['inclusao']['infoCadastro']['contato']['foneCel']

    # regex para celulares com apenas números e mínimo de 11 dígitos (ddd + 9 + número)
    exp = '^[1-9]{2}? ?(?:[2-8]|9[1-9])[0-9]{3}?[0-9]{4}$'

    foneCel = re.findall(exp, foneCel)
    if not foneCel:
        raise app_exceptions.Invalidinput("Celular não aceito!")
        
    

def validate_foneFixo(data):
    foneFixo = data['infoContri']['inclusao']['infoCadastro']['contato']['foneFixo']

    # regex para telefone fixo com apenas números e mínimo de 10 dígitos (ddd  + número)
    exp = '^[1-9]{2}([2-8]{4})([0-9]{4})$'

    foneFixo = re.findall(exp, foneFixo)
    if not foneFixo:
        raise app_exceptions.Invalidinput("Telefone Fixo não aceito!")