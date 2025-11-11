from biseccion import biseccion
from newtonRaphson import newtonRaphson
import os

def main():
    #Estructura del menu
    print(".:APROXIMACION DE RAICES:.:\n")
    expr_str = input("Ingrese la funcion f(x) = ")

    os.system("cls") #Limpia pantalla

    #Seleccion de metodo
    print("Seleccione el metodo a utilizar:")
    op = input("1. Biseccion\n2. Newton-Raphson\nOpcion: ")

    while True:
        os.system("cls") #Limpia pantalla
        if op == '1':
            a = float(input("Ingresa el intervalo a: "))
            b = float(input("Ingresa el intervalo b: "))
            err_relativo = float(input("Ingrese el error relativo: "))
            biseccion(expr_str, a, b, err_relativo)
            break
        elif op == '2':
            os.system("cls") #Limpia pantalla
            x0 = float(input("Ingresa el valor incial de x0: "))
            a = float(input("Ingresa el intervalo a: "))
            b = float(input("Ingresa el intervalo b: "))
            err_relativo = float(input("Ingrese el error relativo: "))
            newtonRaphson(expr_str, x0, a, b, err_relativo)
            break

if __name__ == "__main__":
    main()