def validar_entero(num_min: int, num_max: int) -> int:
    numero = input("Ingrese un numero: ")
    if  not numero.isdigit() or int(numero) < num_min or int(numero) > num_max:
        return validar_entero(num_min, num_max)
    return numero


print(validar_entero(2,9))