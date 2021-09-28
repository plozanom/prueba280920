import operator

def lista_numeros():
#Función para tomar las lineas de texto del archivo keylog.txt y agregarlos a una lista
    
    lista = []

    with open('keylog.txt','r') as file:#Abriendo el archivo en modo lectura
        for num in file:
            lista.append(num)#Agregando las lineas de texto del archivo a una lista 
    
    return lista

def armador_psw(lista):
#Función para obtener los numeros que conforman la contraseña y retornarlos ordenados en una lista

    pos0 = []
    pos1 = []
    pos2 = []
    dct_pos0 = {}
    dct_pos1 = {}
    dct_pos2 = {}
    
    for num in lista:#Recorriendo la lista dada por la función lista_numeros
        if num[0] not in pos0:
            pos0.append(num[0])#Agregando a pos0 los valores (sin repetirlos) que se encuentran en la primera posición de cada numero en la lista dada por lista_numeros

        if num[1] not in pos1:
            pos1.append(num[1])#Agregando a pos1 los valores (sin repetirlos) que se encuentran en la segunda posición de cada numero en la lista dada por lista_numeros
        
        if num[2] not in pos2:
            pos2.append(num[2])#Agregando a pos2 los valores (sin repetirlos) que se encuentran en la tercera posición de cada numero en la lista dada por lista_numeros
        
        if num[0] in dct_pos0:#Creando un diccionario con los valores que están en la posición 1 de cada numero en la lista dada por lista_numeros y la cantidad de veces que se repiten
            dct_pos0[num[0]] += 1
        else:
            dct_pos0[num[0]] = 1

        if num[1] in dct_pos1:#Creando un diccionario con los valores que están en la posición 2 de cada numero en la lista dada por lista_numeros y la cantidad de veces que se repiten
            dct_pos1[num[1]] += 1
        else:
            dct_pos1[num[1]] = 1

        if num[2] in dct_pos2:#Creando un diccionario con los valores que están en la posición 3 de cada numero en la lista dada por lista_numeros y la cantidad de veces que se repiten
            dct_pos2[num[2]] += 1
        else:
            dct_pos2[num[2]] = 1
    
    first_value = list(set(pos0)-set(pos1)-set(pos2))#Hallando el primer numero de la contraseña
    second_value = list(set(pos0)&set(pos1)-set(pos2))#Hallando el segundo numero de la contraseña
    penultimate_value = list(set(pos2)&set(pos1)-set(pos0))#Hallando el penúltimo numero de la contraseña
    ultimate_value = list(set(pos2)-set(pos1)-set(pos0))#Hallando el último numero de la contraseña

    dct_mdm_vals = {j: dct_pos2[j] for j in dct_pos2 if j in dct_pos1 and j in dct_pos0}#Creando un diccionario con los numeros que se encuentran repetidos tanto en dct_pos0, dct_pos1 y dct_pos2 y cuantas veces se repiten en dct_pos2
    dct_mdm_vals_std = sorted(dct_mdm_vals.items(), key=operator.itemgetter(1))#Ordenando los pares key:value con respecto al value ya que entre menor sea el value, la posición del key en la contraseña será menor
    medium_values = [i for i,j in dct_mdm_vals_std]#Creando una lista con los keys ordenados

    return first_value+second_value+medium_values+penultimate_value+ultimate_value

def psw(lista):

    print('La contraseña más corta para la cual todas las secuencias son correctas es: ', end="")
    for i in lista:
        print(int(i),end="")

psw(armador_psw(lista_numeros()))