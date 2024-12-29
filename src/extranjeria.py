from collections import Counter, defaultdict
from typing import NamedTuple
import csv


RegistroExtranjeria = NamedTuple('RegistroExtranjeria',
            [('distrito', str),
            ('seccion', str),
            ('barrio', str),
            ('pais', str),
            ('hombres', int),
            ('mujeres', int)]
            )

def lee_datos_extranjeria(ruta: str) -> list[RegistroExtranjeria]:
    '''
    recibe la ruta del fichero CSV, devolviendo una lista de tuplas
    de tipo RegistroExtranjeria con toda la información contenida en
    el fichero.
    '''

    with open(ruta, encoding = "utf-8") as f:
        lector = csv.reader(f)
        next(lector)

        res = []

        for distrito, seccion, barrio, pais, hombres, mujeres in lector:
            hombres = int(hombres)
            mujeres = int(mujeres)
            tupla = RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres)
            res.append(tupla)
        return res


def numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> int:
    '''
    recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve
    el número de nacionalidades distintas presentes en los registros de
    la lista recibida como parámetro
    '''
    res = set()
    for r in registros:
        res.add(r.pais)
    return len(res)


def  secciones_distritos_con_extranjeros_nacionalidades(registros: list[RegistroExtranjeria], paises: set[str]) -> list[tuple[str, str]]:
    '''
    recibe una lista de tuplas de tipo RegistroExtranjeria y un conjunto
    de cadenas con nombres de países, y devuelve una lista de
    tuplas (distrito, seccion) con los distritos y secciones en los que hay
    extranjeros del conjunto de paises dado como parámetro. La lista de tuplas
    devuelta estará ordenada por distrito.
    '''
    res = set()
    for r in registros:
        if r.pais in paises:
            tupla = (r.distrito, r.seccion)
            res.add(tupla)
    return sorted(res)


def total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> dict[str:int]:
    '''
    recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve
    un diccionario de tipo {str:int} en el que las claves son los países
    y los valores son el número total de extranjeros (tanto hombres como
    mujeres) de cada país.
    '''
    res = {}
    for r in registros:
        if r.pais in res:
            res[r.pais] += r.hombres + r.mujeres
        else:
            res[r.pais] = r.hombres + r.mujeres
    return res

def top_n_extranjeria(registros: list[RegistroExtranjeria], n: int =3) -> list[tuple[str, int]]:
    '''
    recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve una
    lista de tuplas (pais, numero_extranjeros) con los n países de los que
    hay más población extranjera en los registros pasados como parámetros.
    '''
    #convierte el diccionario en una lista de tuplas con la que puedo trabajar
    #tengo que trabajar con los items del diccionario( pais, num_extranjeros_por_pais)
    #1.- ordenar de mayor a menor número
    #lista_ordenada = sorted(num_extranjeros_por_pais.items(), key= lambda t reverse = False)
    #return lista_ordenada[:n]
    #2.- Devolver los n primeros

    num_extranjeros_por_pais = total_extranjeros_por_pais(registros)
    return num_extranjeros_por_pais.items()



def barrio_mas_multicultural(registros:list[RegistroExtranjeria]) -> str:
    '''
    recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el
    nombre del barrio en el que hay un mayor número de países de procedencia
    distintos
    '''
    #hace falta construir un diccionario que agrupe por barrios
    #dict[str, list[RegistroExtranjeria]]
    #lo implementamos en una funcion auxliar

    #construir un diccionario en el que para cada barrio tengamos el conjunto de paisis que pertenecen a ese barrio
    paises_por_barrio= {}
    for r in registros:
        if r.barrio in paises_por_barrio:
            paises_por_barrio[r.barrio].add(r.pais)
        else:
            paises_por_barrio[r.barrio] = {r.pais}
    maximo = max(paises_por_barrio.items(), key = lambda t:len(t[1]))
    return maximo[0]

def barrio_con_mas_extranjeros(registros:list[RegistroExtranjeria], tipo:str =None) -> str:
    '''
    recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el
    nombre del barrio en el que hay un mayor número de extranjeros, bien
    sea en total (tanto hombres como mujeres) si tipo tiene el valor None,
    bien sea de hombres si tipo es 'Hombres', o de mujeres si tipo es 'Mujeres'.
    '''
    extranjeros_por_barrio= defaultdict(list)
    for r in registros:
        if tipo == None:
            extranjeros_por_barrio[r.barrio].append(r)
        elif tipo == 'Hombres':
            extranjeros_por_barrio[r.barrio].append(r)
        else:
            extranjeros_por_barrio[r.barrio].append(r)
    barrio_mas_extranjeros = max(extranjeros_por_barrio.items(), key= lambda t:t[1])
    return barrio_mas_extranjeros[0]

    # extranjeros_por_barrio = Counter( r.barrio for r in registros if tipo == None elif tipo == 'Hombres' else tipo == 'Mujeres')
    # barrio_mas_extranjeros = max(extranjeros_por_barrio.items(), key= lambda t:t[1])
    # return barrio_mas_extranjeros[0]

    #https://pastebin.com/wuh5pvYP


def pais_mas_representado_por_distrito(registros:list[RegistroExtranjeria]) -> dict[ str:str]:
    '''
     recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve un
     diccionario de tipo {str:str} en el que las claves son los distritos
     y los valores los países de los que hay más extranjeros residentes
     en cada distrito.
    '''
    pass