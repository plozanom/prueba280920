psw = int(input('Coloca el numero generado por prueba.py aquí>>> '))

def lista_numeros():
    
    lista = []

    with open('keylog.txt','r') as file:
        for num in file:
            lista.append(num)
    
    return lista

def comprobador(lista, psw):

    psw = str(psw)

    if len(psw) < 8 or len(psw)> 8:
        return 'La contraseña es incorrecta'
    
    for num in lista:
        if num[0] == psw[-1] or num[0] == psw[-2]:
            return 'Failed'
        elif num[1] == psw[-1]:
            return 'Failed'
        elif psw.index(num[1]) < psw.index(num[0]):
            return 'Failed'
        elif psw.index(num[2]) < psw.index(num[1]):
            return 'Failed'
        else:
            return 'Success!!!!'

print(comprobador(lista_numeros(),psw))