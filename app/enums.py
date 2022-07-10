from enum import Enum

class tpInsc (str, Enum):
    cnpjTp = 1
    cpfTp = 2


class tpAmb (str, Enum):
    producao = 1
    producaoRestrita = 2 


class procEmi (str, Enum):
    aplicaContri = 1
    aplicGover = 2

class ideEFR (str, Enum):
    enteFeder = "S"
    unidAdmAuto = "N"

class indEscrituracao (str, Enum):
    naoObri = 0
    obri = 1


class indDesoneracao (str, Enum):
    aplica = 0
    naoAplic = 1

class indSitPJ (str, Enum):
    situaNormal = 0
    extinto = 1
    fusao = 2
    cisao = 3
    incorporacao = 4

class indAcordoIsenMulta (str, Enum):
    semAcordo = 0
    comAcordo = 1
