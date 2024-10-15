from UTN_Heroes_Dataset.utn_pp import (
                                        get_original_matrix, mostrar_matriz_texto_tabla,
                                        clear_console, color_text
                                        )

matriz_concesionaria = get_original_matrix()
columnas = ["IND", "MARCA", "MODELO", "CANTIDAD", "PRECIO", "GANANCIA"]
garages = []
def obtener_existencias():
    for i in range(20):
        garages.append([i])
        garages[i].append(matriz_concesionaria[0][i])
        garages[i].append(matriz_concesionaria[1][i])
        garages[i].append(matriz_concesionaria[2][i])
        garages[i].append(matriz_concesionaria[3][i])
        garages[i].append(matriz_concesionaria[4][i])
    print(mostrar_matriz_texto_tabla(garages, columnas))

def total_autos():
    acumulador = 0
    for i in range (len(garages)):
        acumulador += int(garages[i][3])
    return acumulador
    
def garage_mas_vacio():
    bandera = True
    for i in range (len(garages)):
        if bandera == True or garages[i][3] < minimo:
            minimo =  garages[i][3]
            matriz = [garages[i]]
            bandera = False
    mostrar_matriz_texto_tabla(matriz, columnas)

def mayor_cantidad():
    bandera = True
    for i in range (len(garages)):
        if bandera == True or garages[i][3] > maximo:
            maximo =  garages[i][3]
            bandera = False
    return maximo

obtener_existencias()
#print(mostrar_matriz_texto_tabla(garages, columnas))
#print(garages)
#print(f"La cantidad total de autos es: {total_autos()}")
print(f"La mayor cantidad de autos en un garage es de: {mayor_cantidad()}")
