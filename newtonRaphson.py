import sympy as sp
import os

def newtonRaphson(expr_str, x0, a, b, err_relativo):
    # Definiciones básicas
    x = sp.Symbol('x')
    f = sp.sympify(expr_str)
    f_num = sp.lambdify(x, f)

    # Derivadas
    f_primerDeriv = sp.diff(f, x)
    f_segundaDeriv = sp.diff(f_primerDeriv, x)

    # Evaluaciones iniciales
    f_x0 = f_num(x0)
    v_primerDeriv = f_primerDeriv.subs(x, x0)
    v_segundaDeriv = f_segundaDeriv.subs(x, x0)

    # Comprobación del teorema
    teorema = abs((f_x0 * v_segundaDeriv) / (v_primerDeriv)**2)

    os.system("cls")
    if teorema < 1:
        print("El teorema se cumple. Es seguro que converge.")
    else:
        print(" Puede que converja o puede que no...")
    input("\nPresiona Enter para continuar...")

    os.system("cls")
    print("Método de Newton-Raphson")
    print(f"Función: f(x) = {expr_str}")
    print(f"Intervalo: [{a}, {b}]")
    print(f"Valor inicial: x₀ = {x0}\n")
    print("{:<6} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        "Iter", "Xi", "f(Xi)", "f'(Xi)", "Xi+1", "Error"))
    print("-" * 70)

    # Variables iniciales
    i = 0
    Xi = x0
    err = None

    # Iteraciones
    while True:
        fXi = f_num(Xi)
        fDerivXi = f_primerDeriv.subs(x, Xi)
        Xi1 = Xi - (fXi / fDerivXi)  # Fórmula principal

        if i > -1:
            err = abs((Xi1 - Xi) / Xi1)
        else:
            err = None

         # Mostrar resultados en tabla 
        err_str = f"{err:.6f}" if err is not None else "-"
        print("{:<6} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12}".format(
            i, Xi, fXi, fDerivXi, Xi1, err_str))

        # Condición de parada
        if err is not None and err < err_relativo:
            break

        Xi = Xi1
        i += 1
