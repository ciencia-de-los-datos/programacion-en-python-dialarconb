"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_segunda_columna = 0
    with open("data.csv","r") as data:
        for linea in data:
            
            col = linea.strip().split('\t')
            if len(col) >= 2:
            
                valor_segunda_columna = int(col[1])
                suma_segunda_columna += valor_segunda_columna
 

    return suma_segunda_columna


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    from operator import itemgetter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data=[x[0] for x in data[:]]
    contador={}
    for x in data:
        if x in contador.keys():
            contador[x]+=1
        else:
            contador[x]=1
    tuplas=[]
    for key, value in contador.items():
        tuplas.append((key,value))
    tuplas=sorted(tuplas,key=itemgetter(0))
    return tuplas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df]

    ListA = [z for z in df if z[0] == "A"]
    ListB = [z for z in df if z[0] == "B"]
    ListC = [z for z in df if z[0] == "C"]
    ListD = [z for z in df if z[0] == "D"]
    ListE = [z for z in df if z[0] == "E"]

    Col2A = [z[1] for z in ListA[0:]]
    Col2B = [z[1] for z in ListB[0:]]
    Col2C = [z[1] for z in ListC[0:]]
    Col2D = [z[1] for z in ListD[0:]]
    Col2E = [z[1] for z in ListE[0:]]

    sumaA = 0
    sumaB = 0
    sumaC = 0
    sumaD = 0
    sumaE = 0

    for i in Col2A:
        sumaA = sumaA + int(i)
        
    for i in Col2B:
        sumaB = sumaB + int(i)

    for i in Col2C:
        sumaC = sumaC + int(i)

    for i in Col2D:
        sumaD = sumaD + int(i)
        
    for i in Col2E:
        sumaE = sumaE + int(i)

    List_ordenada = [('A', sumaA), ('B', sumaB), ('C', sumaC), ('D', sumaD), ('E', sumaE)]

    return List_ordenada


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df] #Separamos
    Col3_mes = [z[2].split("-")[1] for z in df[0:]]
    from collections import Counter

    tuples_list = Counter(Col3_mes)
    tuples_list = dict(tuples_list)
    pregunta4 = sorted(tuples_list.items())

    return pregunta4


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import csv

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])
    

    max_values = {}
    min_values = {}

    rows = data.strip().split('\n')

    for row in rows:
        columns = row.split('\t')
        letra = columns[0]
        valor_columna_2 = int(columns[1])

        if letra in max_values:
            max_values[letra] = max(max_values[letra], valor_columna_2)
        else:
            max_values[letra] = valor_columna_2

        if letra in min_values:
            min_values[letra] = min(min_values[letra], valor_columna_2)
        else:
            min_values[letra] = valor_columna_2

    resultado = [(letra, max_values[letra], min_values[letra]) for letra in sorted(max_values)]

    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv
    from operator import itemgetter
    with open ("data.csv","r") as file:
        data = file.readlines()
    datatemp = list()
    data1= [row[:-1] for row in data]
    data2 = [str(row).split("\t")[-1] for row in data1]
    data4 = []
    data5=[]
    for row in data2:
        a= row.split(",")
        data4.extend(a)
    for row in data4:
        b= row.split(":")
        data5.extend(b)
    x= data5[0::2]
    y = data5[1::2]
    xy = zip(x,y)
    dicc= {}
    for row in xy:
        clave = row[0]
        valor = []
        val = int(row[1])
        if clave in dicc:
            dicc[clave].append(val)
        else:
            dicc[clave]=valor
            dicc[clave].append(val)
    dicc = [(clave,min(valor),max(valor)) for clave,valor in dicc.items()]
    dicc = sorted(dicc,key = itemgetter(0), reverse = False)
    
    return dicc


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])

    values_dict = {}

    rows = data.strip().split('\n')

    for row in rows:
        columns = row.split('\t')
        valor_columna_2 = int(columns[1])
        letra_columna_1 = columns[0]

        if valor_columna_2 in values_dict:
            values_dict[valor_columna_2].append(letra_columna_1)
        else:
            values_dict[valor_columna_2] = [letra_columna_1]

    respuesta_07 = [(valor, letras) for valor, letras in values_dict.items()]

    respuesta_07.sort()

    return respuesta_07


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t')[:2] for row in data ]
    data = [[row[0], int(row[1])] for row in data]
    dic = {key[1] : [] for key in data}
    for i in data:
        if i[0] not in dic[i[1]]:
            dic[i[1]].append(i[0])

    list_data = [(key, sorted(value)) for key, value in dic.items()]
    list_data.sort(key=lambda x: x[0])
    return list_data


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv", "r") as file:
        data = file.readlines()        
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        data = [row[3:] for row in data]
        
        col5 = []
        for index, element in enumerate (data):
            list5 = []
            for indice, fila in enumerate (element):
                if len(fila) > 1:
                    list5.append(fila)
            col5.append(list5)
        
            lista = []
            for index, element in enumerate (col5):
                lista.extend(element)
            
            #lista = [(row[:3], int(row[4:])) for row in lista]
            lista = [row.replace(":", ",") for row in lista]    
            lista = [row.split(',') for row in lista]  
            lista = [(row[0], (int(row[1]))) for row in lista] 

            counter = {}
            for key, value in lista:
                    if key in counter:       
                        counter[key] += 1
                    else:
                        counter[key] = 1

            rta = list(counter.items())
            rta.sort(reverse = False)
            rta_9 = dict (rta)
    return rta_9
    


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    respuesta_10 = []
    import csv
    with open('data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        
        for row in csvreader:
            letra_columna_1 = row[0]
            column_4 = row[3].split(',')
            column_5 = row[4].split(',')

            cantidad_columna_4 = len(column_4)
            cantidad_columna_5 = len(column_5)

            respuesta_10.append((letra_columna_1, cantidad_columna_4, cantidad_columna_5))

    return respuesta_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df] #Separamos

    list_11 = []

    Cols = [row[1:4:2] for row in df[0:]]
    for i in Cols:
        Columna4 = i[1].split(",")
        for x in Columna4:
            tupla = (i[0],x)
            list_11.append(tupla) 

    valA = []
    letA = []
    valB = []
    letB = []
    valC = []
    letC = []
    valD = []
    letD = []
    valE = []
    letE = []
    valF = []
    letF = []
    valG = []
    letG = []

    for j in list_11:
        if j[1] == 'a':
            valA.append(j[0])
            letA.append(j[1])
        elif j[1] == 'b':
            valB.append(j[0])
            letB.append(j[1])
        elif j[1] == 'c':
            valC.append(j[0])
            letC.append(j[1])
        elif j[1] == 'd':
            valD.append(j[0])
            letD.append(j[1])
        elif j[1] == 'e':
            valE.append(j[0])
            letE.append(j[1])
        elif j[1] == 'f':
            valF.append(j[0])
            letF.append(j[1])
        else:
            valG.append(j[0])
            letG.append(j[1])

    sumaA = 0
    for i in valA:
        sumaA = sumaA + int(i)

    sumaB = 0
    for i in valB:
        sumaB = sumaB + int(i)

    sumaC = 0
    for i in valC:
        sumaC = sumaC + int(i)

    sumaD = 0
    for i in valD:
        sumaD = sumaD + int(i)

    sumaE = 0
    for i in valE:
        sumaE = sumaE + int(i)

    sumaF = 0
    for i in valF:
        sumaF = sumaF + int(i)

    sumaG = 0
    for i in valG:
        sumaG = sumaG + int(i)
    List_ordenada = [(letA[1], sumaA), (letB[1], sumaB), (letC[1], sumaC), (letD[1], sumaD), (letE[1], sumaE), (letF[1], sumaF), 
                    (letG[1], sumaG)]

    result = {}
    for letra, suma in List_ordenada:
        if letra in result.keys():
            result[letra].append(suma)
        else:
            result[letra] = suma
    return result


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    archivo = open('data.csv')                                                                #Lectura

    archivo = archivo.readlines()

    elementos = [str(archivo[i]).split("\n")[0:-1] for i in range(len(archivo))][:-1]   #Partición por saltos de línea y limpieza
    elementos.append([str(archivo[-1]),''])
    elementos = list(map(lambda x: x[0], elementos))                                    #En cada posición de la lista grande queda el texto y no la lista
    elementos = list(map(lambda x: [x.split("\t")[0],x.split("\t")[4]],elementos))      #Extrae únicamente elementos del diccionario
    elementos = list(map(lambda x: [x[0],x[1].split(",")],elementos))

    for i in range(len(elementos)):
        fila = [elementos[i][0]]
        for j in range(len(elementos[i][1])):
            fila.append(int(elementos[i][1][j][elementos[i][1][j].find(":")+1:]))
        elementos[i] = fila

    elementosSD = [elementos[i][0] for i in range(len(elementos))]
    elementosSD = sorted(list(set(elementosSD)))

    for i in range(len(elementosSD)):
        sumatoria = 0
        for j in range(len(elementos)):
            if(elementosSD[i] in elementos[j]):
                sumatoria += sum(elementos[j][1:])
        elementosSD[i] = (elementosSD[i],sumatoria)
    elementosSD = dict(elementosSD)
    return elementosSD
