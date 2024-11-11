from extranjeria import *

def test_lee_extranjeria(datos):
    print("TEST DE LA FUNCIÓN lee_datos_extranjeria:")
    print(f"Leídos {len(datos)} registros.")
    print("Mostrando los 3 primeros:", datos[0:3], sep='\n')
    print("Mostrando los 3 últimos:", datos[-4:-1], sep='\n')
    
def test_numero_nacionalidades_distintas(datos):
    print("TEST DE LA FUNCIÓN numero_nacionalidades_distintas:")
    print(f"Hay {numero_nacionalidades_distintas(datos)} nacionalidades distintas en los datos.")
    
def test_secciones_distritos_con_extranjeros_nacionalidades(datos):
    print("TEST DE LA FUNCIÓN secciones_distritos_con_extranjeros_nacionalidades:")
    print(f"Hay {len(secciones_distritos_con_extranjeros_nacionalidades(datos, {"ALEMANIA", "ITALIA"}))} secciones de distritos con residentes cuya procedencia es ALEMANIA o ITALIA.")
    print("Mostrando 3 secciones:")
    print(secciones_distritos_con_extranjeros_nacionalidades(datos, {"ALEMANIA", "ITALIA"})[:3])

def test_total_extranjeros_por_pais(datos):
    print("TEST DE LA FUNCIÓN total_extranjeros_por_pais:")
    print("Mostrando el número de residentes para algunos países de procedencia:")
    print("ALEMANIA:", total_extranjeros_por_pais(datos)["ALEMANIA"])
    print("ITALIA:", total_extranjeros_por_pais(datos)["ITALIA"])
    print("MARRUECOS:", total_extranjeros_por_pais(datos)["MARRUECOS"])

def test_top_n_extranjeria(datos):
    print("TEST DE LA FUNCIÓN top_n_extranjeria:")
    print("Mostrando los 5 países de los que proceden más residentes:")
    print(top_n_extranjeria(datos, 5))

if __name__=='__main__':
    datos = lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    test_lee_extranjeria(datos)
    test_numero_nacionalidades_distintas(datos)
    test_secciones_distritos_con_extranjeros_nacionalidades(datos)
    test_total_extranjeros_por_pais(datos)
    test_top_n_extranjeria(datos)