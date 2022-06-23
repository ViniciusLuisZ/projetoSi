from enum import Enum

''' Preencher com o código correspondente ao tipo de inscrição do contribuinte:
1 CNPJ;
2 CPF.
Valores válidos: 1, 2. '''
class tpInsc (str, Enum):
    cnpjTp = 1
    cpfTp = 2


''' Identificação do ambiente:
1 Produção;
2 Produção restrita.
Valores válidos: 1, 2. '''
class tpAmb (str, Enum):
    producao = 1
    producaoRestrita = 2 


''' Processo de emissão do evento:
1 Aplicativo do contribuinte;
2 Aplicativo governamental.
Valores válidos: 1, 2. '''
class procEmi (str, Enum):
    aplicaContri = 1
    aplicGover = 2

''' Informar se o órgão público é o Ente Federativo
Responsável EFR ou se é
uma unidade administrativa autônoma vinculada a um EFR:
S É EFR;
N Não é EFR.
Validação: Essa informação é validada no cadastro do CNPJ na RFB.
Valores válidos: S, N. '''
class ideEFR (str, Enum):
    enteFeder = "S"
    unidAdmAuto = "N"

'''Indicativo da obrigatoriedade do contribuinte em fazer a sua escrituração
contábil através da ECD Escrituração Contábil Digital:
0 Empresa NÃO obrigada à ECD;
1 Empresa obrigada à ECD.
Valores válidos: 0, 1. '''
class indEscrituracao (str, Enum):
    naoObri = 0
    obri = 1


''' Indicativo de desoneração da folha de pagamento:
0 Não Aplicável;
1 Empresa enquadrada nos a rtigos 7° a 9° da Lei 12.546/2011.
Validação: Pode ser igual a [1] apenas se a classificação tributária for igual a
[02, 03,
Nos demais casos deve ser igual a [0].
Valores válidos: 0, 1. '''
class indDesoneracao (str, Enum):
    aplica = 0
    naoAplic = 1

''' Indicativo da
situação da pessoa jurídica
0 Situação Normal;
1 Extinção;
2 Fusão;
3 Cisão;
4 Incorporação.
Validação: Informação obrigatória e exclusiva para pessoa jurídica.
Valores válidos: 0, 1, 2, 3, 4. ''' 
class indSitPJ (str, Enum):
    situaNormal = 0
    extinto = 1
    fusao = 2
    cisao = 3
    incorporacao = 4

'''Indicativo da existê
ncia de acordo internacional para isenção de multa:
0 Sem acordo;
1 Com acordo.
Validação: Só pode ser igual a [1] se {classTrib} for igual a [60].
Valores válidos: 0, 1.'''
class indAcordoIsenMulta (str, Enum):
    semAcordo = 0
    comAcordo = 1
