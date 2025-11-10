import sympy as sp

def biseccion(expr_str, a, b, err):
    #Definiciones basicas
    x = sp.Symbol('x')  #Definicion de variable x
    f = sp.sympify(expr_str)  #Transforma la expresion a una evaluable
    f_num = sp.lambdify(x, f)  #Funcion para evaluar valores reemplazando x

    #Comprobacion de restricciones del metodo de biseccion
    #1. Que la funcion sea continua
    a = 0 #Punto de partida para evaluar continuidad

    #Calculamos los limites laterales y el valor en el punto
    lim_izq = sp.limit(f, x, a, dir='-')
    lim_der = sp.limit(f, x, a, dir='+')
    valor = f.subs(x, a)    
    
    # Verificación de continuidad
    if lim_izq == lim_der == valor:
        print(f"La función es continua en x = {a}")
    else:
        print(f"La función NO es continua en x = {a}")

    #2. Que tengan signos diferentes
    if f_num(a) * f_num(b) > 0:
        print("El intervalo no es valido. Deben tener signos opuestos")
