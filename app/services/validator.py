### esse script será usado para adicionar as regras de validação dos campos do reinf
import app.exceptions as app_exceptions

def validate_classTrib(data):
    if data['ideContri']['tpInsc'] == '2':
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] not in ['21', '22']:
            raise app_exceptions.Invalidinput("Valor não aceito")
    if data['ideContri']['tpInsc'] == '1':
        if data['infoContri']['inclusao']['infoCadastro']['clasTrib'] in ['21', '22']:
            raise app_exceptions.Invalidinput("Valor não aceito")
