def main():
    #Estructura del menu
    print(".:APROXIMACION DE RAICES:.:\n")
    expr_str = input("Ingrese la funcion f(x) = ")

    #Seleccion de metodo
    print("Seleccione el metodo a utilizar:")
    op = input("1. Biseccion\n2. Newton-Raphson: ")

    while True:
        if op == '1':
            a = float(input("Ingresa el intervalo a: "))
            b = float(input("Ingresa el intervalo b: "))
            break
        elif op == '2':
            a = float(input("Ingresa el intervalo a: "))
            b = float(input("Ingresa el intervalo b: "))
            break

if __name__ == "__main__":
    main()