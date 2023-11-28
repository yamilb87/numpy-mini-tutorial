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
            Estas funcionalidades incluyen el [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html),
            el [indexado](https://numpy.org/doc/stable/user/basics.indexing.html#) booleano
             y el manejo de datos faltantes (NaN).

            #### Broadcasting
            El broadcasting es una característica poderosa en NumPy que permite realizar operaciones entre arreglos de diferentes tamaños de una manera inteligente
            (cumpliendo con ciertas reglas). NumPy ajusta automáticamente las dimensiones de los arreglos para que las operaciones sean compatibles.

            ###### Broadcasting de Escalar a Array:
            """)
st.code("""
        import numpy as np

        # Broadcasting de un escalar a un array
        escalar = 5
        array = np.array([1, 2, 3])

        resultado = escalar * array
        # El escalar se expande automáticamente para coincidir con la forma del array
        print(resultado)  # Salida: [5, 10, 15]
        """)

st.markdown("""
            ###### Broadcasting de Arrays Unidimensionales:
            """)

st.code("""
        import numpy as np

        # Broadcasting de dos arrays unidimensionales
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])

        resultado = array1 + array2
        # Ambos arrays se expanden automáticamente para coincidir con la forma del otro
        print(resultado)  # Salida: [5, 7, 9]
        """)

st.markdown("""
            ###### Broadcasting de Arrays Multidimensionales:
            """)

st.code("""
        import numpy as np

        # Broadcasting de dos arrays multidimensionales
        matriz = np.array([[1, 2, 3], [4, 5, 6]])
        vector = np.array([10, 20, 30])

        resultado = matriz + vector
        # El vector se expande automáticamente para coincidir con la forma de la matriz
        print(resultado)
        # Salida:
        # [[11, 22, 33],
        #  [14, 25, 36]]
        """)

st.markdown("""
            ###### Broadcasting de Arrays con Formas Diferentes:
            """)

st.code("""
        import numpy as np

        # Broadcasting de un array 1D y un array 2D
        array1D = np.array([1, 2, 3])
        array2D = np.array([[10], [20], [30]])

        resultado = array1D + array2D
        # El array 1D se expande automáticamente para coincidir con la forma del array 2D
        print(resultado)
        # Salida:
        # [[11, 12, 13],
        #  [21, 22, 23],
        #  [31, 32, 33]]
        """)

st.markdown("""
            Estos son solo ejemplos básicos, y NumPy realiza broadcasting de manera más general para operaciones más complejas.
            Es importante tener en cuenta las reglas de [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
             y cómo NumPy expande automáticamente las dimensiones para que las operaciones sean válidas.
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
