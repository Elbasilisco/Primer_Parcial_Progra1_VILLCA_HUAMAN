from validaciones.validaciones import validar_entero

menu = """
    1_Obtener existencias: para ello deberá crear una función que cargue la existencia de cada vehículo en todos los garajes y mostrarlos.
    2_Calcular por cada garaje la cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria.
    3_Datos completos del garaje que almacena menos unidades de vehículos.
    4_Máxima cantidad de unidades almacenadas entre todos los garajes.
    5_Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje, teniendo en cuenta su precio           unitario y cantidad de unidades almacenadas en cada garaje.
    6_Cantidad de garajes que hayan almacenado 6 o más unidades de vehículos.
    7_Porcentaje de unidades de cada marca de vehículo sobre el total de vehículos almacenados entre todos los garajes de la sede matriz. 
      Además mostrar todos los datos del garaje con el máximo porcentaje de vehículos almacenados.
    8_Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor.
    9_Salir
"""
def menu():
    print(menu)
    while True:
        eleccion = validar_entero(1, 9)
        match (eleccion):
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                break