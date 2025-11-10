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
            err = float(input("Ingrese el error relativo: "))
            #Funcion de biseccion a crear
            break
        elif op == '2':
            x0 = float(input("Ingresa el valor incial de x0: "))
            err = float(input("Ingrese el error relativo: "))
            #Funcion de newton-raphson a crear
            break

if __name__ == "__main__":
    main()