import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Capítulo 5: Funcionalidades Avanzadas')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En este quinto capítulo, exploraremos funcionalidades avanzadas de NumPy que te permitirán realizar operaciones más complejas y eficientes en arreglos NumPy.
            Estas funcionalidades incluyen el broadcasting, el indexado booleano y el manejo de datos faltantes (NaN).

            #### Broadcasting
            El broadcasting es una característica poderosa en NumPy que permite realizar operaciones entre arreglos de diferentes tamaños de una manera inteligente.
            NumPy ajusta automáticamente las dimensiones de los arreglos para que las operaciones sean compatibles.
            """)
st.code("""
        import numpy as np

        # Creación de un arreglo NumPy
        arr = np.array([1, 2, 3])

        # Sumar un escalar a un arreglo
        resultado = arr + 10
        print("Broadcasting - Suma de un escalar:")
        print(resultado)

        # Sumar dos arreglos de diferentes tamaños
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([10, 20])

        resultado = arr1 + arr2
        print("Broadcasting - Suma de dos arreglos de diferentes tamaños:")
        print(resultado)
        """)

st.markdown("""
            #### Indexado Booleano
            El indexado booleano te permite seleccionar elementos de un arreglo NumPy basándote en condiciones booleanas.
            Esto es útil para filtrar datos.
            """)

st.code("""
        import numpy as np

        # Creación de un arreglo NumPy
        arr = np.array([1, 2, 3, 4, 5])

        # Crear un arreglo booleano que indica qué elementos son mayores que 3
        condicion = arr > 3

        # Seleccionar elementos que cumplen la condición
        seleccion = arr[condicion]
        print("Indexado Booleano - Elementos mayores que 3:")
        print(seleccion)
        """)

st.markdown("""
            #### Manejo de Datos Faltantes (NaN)
            En análisis de datos, es común encontrarse con datos faltantes, representados a menudo como `NaN` (Not a Number).
            NumPy permite trabajar con datos faltantes de manera eficiente utilizando la función
            [np.isnan](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html) y funciones relacionadas.
            """)
st.code("""
        import numpy as np

        # Creación de un arreglo NumPy con datos faltantes (NaN)
        arr_con_nan = np.array([1.0, 2.0, np.nan, 4.0, 5.0])

        # Verificar si hay NaN en el arreglo
        hay_nan = np.isnan(arr_con_nan)
        print("Datos faltantes (NaN):")
        print(hay_nan)

        # Calcular la suma sin considerar NaN (ignora los NaN en la suma)
        suma_sin_nan = np.nansum(arr_con_nan)
        print("Suma sin considerar NaN:")
        print(suma_sin_nan)
        """)

st.markdown("""
            En este capítulo, hemos explorado funcionalidades avanzadas de NumPy que te permitirán realizar operaciones más complejas,
            como el broadcasting y el indexado booleano, así como el manejo de datos faltantes (NaN).
            Estas capacidades son fundamentales para el análisis de datos y te brindan la flexibilidad necesaria
            para trabajar con una amplia variedad de datos en tus proyectos.
            En el próximo capítulo, exploraremos cómo leer y escribir datos utilizando NumPy.
            """)
