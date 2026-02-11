import sympy as sp

def integral_riemann_izquierda(f_lambda, a, b, n):
    """
    Cálculo usando Sumas de Riemann por la IZQUIERDA (como en tu clase).
    """
    dx = (b - a) / n
    suma_areas = 0.0
    
    for i in range(n):
        # Usamos el extremo izquierdo del intervalo: x_i = a + i*dx
        x_i = a + i * dx
        suma_areas += f_lambda(x_i) * dx
        
    return suma_areas

def ejecutar():
    x = sp.symbols('x')
    # Ejemplo de entrada: 3*x*(x**2 + 1)**0.5
    func_input = input("Introduce la función f(x): ")

    try:
        expresion = sp.sympify(func_input)
        f_num = sp.lambdify(x, expresion, 'math')

        a = float(input("Límite inferior (a): "))
        b = float(input("Límite superior (b): "))
        n = int(input("Número de particiones (n): "))

        # Cálculos con precisión total
        valor_real = float(sp.integrate(expresion, (x, a, b)))
        valor_aprox = integral_riemann_izquierda(f_num, a, b, n)
        
        # Error relativo: |Real - Aproximado| / |Real|
        error_relativo = abs(valor_real - valor_aprox) / abs(valor_real)

        # Salida formateada a 2 decimales para los valores
        # El error lo dejamos con más detalle o notación científica porque suele ser muy pequeño
        print("\n" + "="*35)
        print(f"Valor Real:       {valor_real:.2f}")
        print(f"Valor Aproximado: {valor_aprox:.2f}")
        print(f"Error Relativo:   {error_relativo:.4f}") 
        print("="*35)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar()