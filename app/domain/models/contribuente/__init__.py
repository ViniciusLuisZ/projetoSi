import string
from fastapi import Query


class contatoScheme:
    def __init__(
        self,
        nmCtt: string = Query(...),
        cpfCtt: string = Query(...),
        foneFixo: string = Query(...),
        foneCel: string = Query(...),
        email: string = Query(...),
    ):
        self.nmCtt = nmCtt
        self.cpfCtt = cpfCtt
        self.foneFixo = foneFixo
        self.foneCel = foneCel
        self.email = email


class softHouseScheme:
    def __init__(
        self,
        cnpjSoftHouse: string = Query(...),
        nmRazao: string = Query(...),
        nmCont: string = Query(...),
        telefone: string = Query(...),
        email: string = Query(...),
    ):
        self.cnpjSoftHouse = cnpjSoftHouse
        self.nmRazao = nmRazao
        self.nmCont = nmCont
        self.telefone = telefone
        self.email = email


class infoEFRScheme:
    def __init__(
        self,
        ideEFR: string = Query(...),
        cnpjEFR: string = Query(...),
    ):
        self.ideEFR = ideEFR
        self.cnpjEFR = cnpjEFR


class novaValidadecheme:
    def __init__(
        self,
        iniValid: string = Query(...),
        fimValid: string = Query(...),
    ):
        self.iniValid = iniValid
        self.fimValid = fimValid


class infoCadastroScheme:
    def __init__(
        self,
        contato: contatoScheme = Query(...),
        softHouse: softHouseScheme = Query(...),
        infoEFR: infoEFRScheme = Query(...),
        novaValidade: novaValidadecheme = Query(None),
    ):
        self.contato = contato
        self.softHouse = softHouse
        self.infoEFR = infoEFR
        self.novaValidade = novaValidade


class idePeriodoScheme:
    def __init__(
        self,
        iniValid: string = Query(...),
        fimValid: string = Query(...),
    ):
        self.iniValid = iniValid
        self.fimValid = fimValid


class InclusaoScheme:
    def __init__(
        self,
        idePeriodo: idePeriodoScheme = Query(...),
        infoCadastro: infoCadastroScheme = Query(...),
    ):
        self.idePeriodo = idePeriodo
        self.infoCadastro = infoCadastro


class alteracaoScheme:
    def __init__(
        self,
        idePeriodo: idePeriodoScheme = Query(...),
        infoCadastro: infoCadastroScheme = Query(...),
    ):
        self.idePeriodo = idePeriodo
        self.infoCadastro = infoCadastro


class exclusaoScheme:
    def __init__(
        self,
        idePeriodo: idePeriodoScheme = Query(...),
        infoCadastro: infoCadastroScheme = Query(...),
    ):
        self.idePeriodo = idePeriodo
        self.infoCadastro = infoCadastro


class ideEventoScheme:
    def __init__(
        self,
        tpAmb: int = Query(...),
        procEmi: int = Query(None),
        verProc: string = Query(...)
    ):
        self.tpAmb = tpAmb
        self.procEmi = procEmi
        self.verProc = verProc


class ideContriScheme:
    def __init__(
        self,
        tpInsc: int = Query(...),
        nrInsc: string = Query(None)
    ):
        self.tpInsc = tpInsc
        self.nrInsc = nrInsc


class infoContriScheme:
    def __init__(
        self,
        inclusao: InclusaoScheme = Query(None),
        alteracao: alteracaoScheme = Query(None),
        exclusao: exclusaoScheme = Query(None),
    ):
        self.inclusao = inclusao
        self.alteracao = alteracao
        self.exclusao = exclusao


class contribuinteQuery:
    def __init__(
        self,
        id: int = Query(),
        ideEvento: ideEventoScheme = Query(...),
        ideContri: ideContriScheme = Query(...),
        infoContri: infoContriScheme = Query(...),
    ):
        self.id = id
        self.ideEvento = ideEvento
        self.ideContri = ideContri
        self.infoContri = infoContri
