import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Capítulo 4: Operaciones Estadísticas y de Álgebra Lineal')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En este cuarto capítulo, exploraremos operaciones estadísticas y de álgebra lineal que puedes realizar en arreglos NumPy.
             Aprenderás cómo calcular estadísticas descriptivas y realizar operaciones de álgebra lineal en tus datos.

            #### Operaciones Estadísticas
            [mean()](https://numpy.org/doc/stable/reference/generated/numpy.mean.html),
            [median()](https://numpy.org/doc/stable/reference/generated/numpy.median.html),
            [std()](https://numpy.org/doc/stable/reference/generated/numpy.std.html),
            [var()](https://numpy.org/doc/stable/reference/generated/numpy.var.html).

            Puedes calcular estadísticas descriptivas básicas utilizando las funciones _**mean() (media), median() (mediana), std() (desviación estándar) y var() (varianza)**_.
            """)

st.code("""
        import numpy as np

        # Creación de un arreglo NumPy
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        # Calcular la media
        media = np.mean(arr)
        print("Media:", media)

        # Calcular la mediana
        mediana = np.median(arr)
        print("Mediana:", mediana)

        # Calcular la desviación estándar
        desviacion_estandar = np.std(arr)
        print("Desviación Estándar:", desviacion_estandar)

        # Calcular la varianza
        varianza = np.var(arr)
        print("Varianza:", varianza)
        """)

st.markdown("""
            #### Álgebra Lineal

            ##### Producto Interno (Producto Escalar)            
            El producto interno (o producto escalar) de dos arreglos se calcula con la función [dot()](https://numpy.org/doc/stable/reference/generated/numpy.dot.html).
            Esto es útil en álgebra lineal y cálculos vectoriales.
            """)
st.code("""
        import numpy as np

        # Creación de dos arreglos NumPy
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])

        # Calcular el producto interno
        producto_interno = np.dot(arr1, arr2)
        print("Producto Interno:")
        print(producto_interno)
        """)

st.markdown("""
            ##### Multiplicación de Matrices
            La multiplicación de matrices se realiza utilizando la función dot() o el operador @.
            """)
st.code("""
        import numpy as np

        # Creación de dos matrices NumPy
        matriz1 = np.array([[1, 2], [3, 4]])
        matriz2 = np.array([[5, 6], [7, 8]])

        # Multiplicación de matrices utilizando 'dot()'
        resultado_dot = np.dot(matriz1, matriz2)
        print("Multiplicación de Matrices (dot()):")
        print(resultado_dot)

        # Multiplicación de matrices utilizando el operador '@'
        resultado_operador = matriz1 @ matriz2
        print("Multiplicación de Matrices (operador '@'):")
        print(resultado_operador)
        """)

st.markdown("""
            #### Resolución de Sistemas de Ecuaciones Lineales
            Supongamos que tienes un sistema de ecuaciones lineales, que se puede expresar en forma matricial como:
            """) 

st.code("""
        Ax = b
        """,
        language='css')

st.markdown("""
            Donde:

            * A es la matriz de coeficientes.
            * x es el vector de incógnitas que deseas encontrar.
            * b es el vector de valores conocidos (lado derecho de las ecuaciones).

            Para resolver este sistema en NumPy, puedes utilizar la función [linalg.solve()](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)
            que resuelve sistemas de ecuaciones lineales de la forma $$Ax = b$$.
            Aquí hay un ejemplo más detallado:
            """)
                
st.code("""
        import numpy as np

        # Definición de la matriz de coeficientes 'A' y el vector 'b'
        A = np.array([[2, 1],
                [1, -3]])

        b = np.array([5, 2])

        # Resolver el sistema de ecuaciones
        solucion = np.linalg.solve(A, b)

        print("Solución del Sistema de Ecuaciones:")
        print("x =", solucion[0])
        print("y =", solucion[1])
        """)

st.markdown("""
            En este ejemplo, definimos la matriz de coeficientes A y el vector b que representan nuestro sistema de ecuaciones.
            Luego, utilizamos `np.linalg.solve(A, b)` para encontrar la solución, que se almacena en el vector solucion.
            Finalmente, imprimimos los valores de `x` e `y`, que son las soluciones del sistema.

            Es importante mencionar que `np.linalg.solve()` es la forma más eficiente y precisa de resolver sistemas de ecuaciones lineales cuando trabajas con NumPy,
            ya que aprovecha las optimizaciones numéricas subyacentes de la biblioteca.
            
            Resolver sistemas de ecuaciones lineales es fundamental en muchas áreas de las ciencias y la ingeniería, y NumPy simplifica este proceso,
            permitiéndote concentrarte en tus problemas específicos en lugar de las complejidades de las operaciones matriciales.

            ---

            En este capítulo, hemos explorado operaciones estadísticas y de álgebra lineal que puedes realizar en arreglos NumPy.
            Estas operaciones son esenciales en el análisis de datos y en aplicaciones de álgebra lineal en ciencia e ingeniería.
            En el próximo capítulo, nos enfocaremos en funcionalidades avanzadas de NumPy, como el broadcasting y el indexado booleano.
            """)