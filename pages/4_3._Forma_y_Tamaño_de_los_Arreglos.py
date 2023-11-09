import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Capítulo 3: Forma y Tamaño de los Arreglos')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En este tercer capítulo, profundizaremos en la manipulación de la forma y el tamaño de los arreglos NumPy.
             Aprenderás cómo cambiar la forma de un arreglo, agregar o eliminar elementos y cómo apilar arreglos.
             Vamos a explorar estas operaciones fundamentales.
            
            #### Cambio de Forma de los Arreglos

            ##### [reshape()](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)

            La función [reshape()](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
             te permite cambiar la forma de un arreglo NumPy sin cambiar sus elementos.
             Esto es útil cuando deseas trabajar con arreglos de diferentes dimensiones.
            """)
st.code("""
        import numpy as np

        # Creación de un arreglo NumPy de 1D
        arr = np.array([1, 2, 3, 4, 5, 6])

        # Cambio de forma a un arreglo 2D de 2x3
        arr_2d = arr.reshape(2, 3)
        print("Arreglo 2D:")
        print(arr_2d)
        """
        )

st.markdown("""
            ##### [flatten()](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html)
            La función [flatten()](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html)
             convierte un arreglo multidimensional en un arreglo unidimensional.
            """)

st.code("""
        import numpy as np

        # Creación de un arreglo NumPy 2D
        arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

        # Convertir a un arreglo unidimensional
        arr_1d = arr_2d.flatten()
        print("Arreglo unidimensional:")
        print(arr_1d)
        """
        )

st.markdown("""
            #### Manipulación de Tamaño de los Arreglos
            
            ##### [resize()](https://numpy.org/doc/stable/reference/generated/numpy.resize.html)

            La función [resize()](https://numpy.org/doc/stable/reference/generated/numpy.resize.html)
             cambia el tamaño de un arreglo NumPy, agregando o eliminando elementos según sea necesario.
            """)

st.code("""
        import numpy as np

        # Creación de un arreglo NumPy 1D
        arr = np.array([1, 2, 3, 4, 5])

        # Cambio de tamaño a un arreglo más grande (rellena con ceros)
        arr_resize = np.resize(arr, (8,))
        print("Arreglo redimensionado (relleno con ceros):")
        print(arr_resize)

        # Cambio de tamaño a un arreglo más pequeño (recorta elementos)
        arr_resize = np.resize(arr, (3,))
        print("Arreglo redimensionado (recorte de elementos):")
        print(arr_resize)
        """
        )

st.markdown("""
            #### Apilamiento de Arreglos

            ##### [concatenate()](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)

            La función [concatenate()](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)
             te permite combinar varios arreglos en uno solo. Puedes especificar el eje a lo largo del cual se realizará la concatenación.
            """)

st.code("""
        import numpy as np

        # Creación de dos arreglos NumPy
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])

        # Concatenar a lo largo del eje 0 (por defecto)
        concatenado_eje0 = np.concatenate((arr1, arr2))
        print("Concatenación a lo largo del eje 0:")
        print(concatenado_eje0)

        # Creación de dos arreglos NumPy 2D
        arr1_2d = np.array([[1, 2], [3, 4]])
        arr2_2d = np.array([[5, 6]])

        # Concatenar a lo largo del eje 0
        concatenado_eje0_2d = np.concatenate((arr1_2d, arr2_2d), axis=0)
        print("\nConcatenación a lo largo del eje 0 (arreglos 2D):")
        print(concatenado_eje0_2d)        
        """)

st.markdown("""
            En este capítulo, hemos explorado cómo cambiar la forma y el tamaño de los arreglos NumPy,
             así como cómo realizar operaciones de apilamiento para combinar varios arreglos en uno solo.
             Estas habilidades son esenciales para la manipulación eficiente de datos en NumPy y
             serán útiles en aplicaciones de análisis de datos más avanzadas.
             En el próximo capítulo, nos sumergiremos en operaciones estadísticas y de álgebra lineal con arreglos NumPy.
            """)