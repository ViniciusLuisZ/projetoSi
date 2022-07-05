
iniValid = '2001-02'
fimValid = '2004-02'

refIniValid = (iniValid.split('-'))
refFimValid = (fimValid.split('-'))


if refFimValid[0] < refIniValid[0]:
    raise ValueError('ano fim menor')
elif refFimValid[0] == refIniValid[0]:
    if refFimValid[1] < refIniValid[1]:
        raise ValueError('mes fim menor')
    elif refFimValid[1] == refIniValid[1]:
        raise ValueError('datas nao podem ser iguais')
    

