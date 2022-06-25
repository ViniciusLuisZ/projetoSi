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
 