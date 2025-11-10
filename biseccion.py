import sympy as sp
import os

def biseccion(expr_str, a, b, err_relativo):
    #Definiciones basicas
    x = sp.Symbol('x')  #Definicion de variable x
    f = sp.sympify(expr_str)  #Transforma la expresion a una evaluable
    f_num = sp.lambdify(x, f)  #Funcion para evaluar valores reemplazando x

    #RESTRICCIONES
    #1. Que la funcion sea continua
    p = (a + b)/2 #Punto de partida para evaluar continuidad

    #Calculamos los limites laterales y el valor en el punto
    lim_izq = sp.limit(f, x, p, dir='-')
    lim_der = sp.limit(f, x, p, dir='+')
    valor = f.subs(x, p)    
    
    # Verificación de continuidad
    if lim_izq == lim_der == valor:
        os.system("cls") #Limpia pantalla
        print(f"La función es continua en x = {p}")
    else:
        print(f"La función NO es continua en x = {p}")

    #2. Que tengan signos diferentes
    if f_num(a) * f_num(b) > 0:
        print("El intervalo no es valido. Deben tener signos opuestos.")
    else:
        print("El intervalo tiene signos opuestos.")
    iteraciones = 0
    input("\nPresiona Enter para continuar...") #Congela consola

    os.system("cls") #Limpia pantalla

    # Encabezado de tabla
    print("Método de Bisección")
    print(f"Función: f(x) = {expr_str}")
    print(f"Intervalo inicial: [{a}, {b}]\n")
    print("{:<10} {:<10} {:<10} {:<10} {:<12} {:<12} {:<12} {:<10}".format(
        "Iter", "a", "b", "m", "f(a)", "f(b)", "f(m)", "Error"))
    print("-"*85)

    #ITERACIONES
    err = None
    
    while True:

        #Calculo del punto medio
        puntoMedio = (a + b)/2

        # Mostrar datos en tabla
        print("{:<10} {:<10.5f} {:<10.5f} {:<10.5f} {:<12.5f} {:<12.5f} {:<12.5f} {:<10}".format(
            iteraciones, a, b, puntoMedio, f_num(a), f_num(b), f_num(puntoMedio), f"{err:.5f}" if err else "-"))


        #Calcular los nuevos intervalos 
        if f_num(a) * f_num(puntoMedio) < 0:
            b = puntoMedio
        elif f_num(puntoMedio) * f_num(b):
            a = puntoMedio

        #Verificamos si lleva mas de una iteracion para calcular el error
        if iteraciones > 0:
            err = abs((puntoMedio - puntoMedioAnt)/puntoMedio)
            print(puntoMedio, puntoMedioAnt)
            if err < err_relativo:
                break

        #Fin del ciclo
        #Contador de ciclos
        iteraciones += 1

        #Punto medio actual se guarda para cuando se reinicie el ciclo
        puntoMedioAnt = puntoMedio 