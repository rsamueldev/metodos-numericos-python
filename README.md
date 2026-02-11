# Métodos Numéricos en Python 🧮

Este repositorio contiene una colección de algoritmos fundamentales de **Cálculo Numérico** implementados en Python. El objetivo principal es resolver problemas de integración y búsqueda de raíces, comparando los resultados aproximados con soluciones analíticas para medir la precisión mediante el error relativo.

## 🚀 Algoritmos Implementados

* **Integración Numérica:** Sumas de Riemann (Extremo Izquierdo).
* **Búsqueda de Raíces:** Método de Bisección (Próximamente).
* **Búsqueda de Raíces:** Método de Newton-Raphson (Próximamente).

## 🛠️ Características Principales

1.  **Evaluación Dinámica:** Permite al usuario ingresar funciones matemáticas directamente por consola (ej. `3*x*(x**2 + 1)**0.5`).
2.  **Cálculo de Error:** Utiliza la librería `SymPy` para obtener la solución exacta mediante integración simbólica y calcular el **error relativo** de la aproximación.
3.  **Optimización:** Uso de `lambdify` para convertir expresiones simbólicas en funciones numéricas de alto rendimiento.

## 📋 Requisitos

Para ejecutar estos scripts, necesitarás instalar las siguientes dependencias:

```bash
pip install sympy
