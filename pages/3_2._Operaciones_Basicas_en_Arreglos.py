import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Capítulo 2: Operaciones Básicas en Arreglos')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En este segundo capítulo, exploraremos las operaciones básicas que puedes realizar en los arreglos NumPy.
             Aprenderás a indexar, segmentar y realizar operaciones matemáticas en arreglos.
             Vamos a sumergirnos en las operaciones fundamentales.
            
            #### Indexación y Segmentación de Arreglos            
            ##### Indexación Básica            
            Puedes acceder a elementos específicos de un arreglo NumPy utilizando la notación de corchetes y el índice del elemento.
             Los índices comienzan en 0 para el primer elemento. Veamos un ejemplo:
            """)

st.code("""
        import numpy as np

        # Creación de un arreglo NumPy
        arr = np.array([1, 2, 3, 4, 5])

        # Acceder al primer elemento
        primer_elemento = arr[0]
        print("Primer elemento:", primer_elemento)

        # Acceder al tercer elemento
        tercer_elemento = arr[2]
        print("Tercer elemento:", tercer_elemento)
        """)

# Creación de un arreglo
arr = np.array([10, 4, 8, 3, 9, 6, 2, 7, 9, 5])
matriz = np.matrix(arr)



with st.expander("ejemplo interactivo 👇​"):
	
	posicion_elemento = st.select_slider("Selecciona posición del elemento: ",options=range(len(arr)),value=2)
	cmap = ListedColormap(['w'])

	fig, ax = plt.subplots()
	ax.matshow(matriz, cmap=cmap)


	for j in range(matriz.shape[1]):
			if j==posicion_elemento:
					props = dict(boxstyle='round', facecolor='red', alpha=0.7)
					ax.text(-0.65+j,1,"Selección",color='red',style='italic',fontdict=dict(size=7))					
			else:
					props = None

			ax.text(x=j, y=0,s=int(matriz[0, j]), va='center', ha='center', size='small', bbox=props)

	ax.set(yticklabels=[])
	ax.set(xticklabels=[])
	ax.tick_params(left=False, bottom=False, top=False)
	ax.tick_params(left=False)
	fig.set_facecolor("#040D12")
	ax.set_title(f"Array de {len(arr)} elementos", color='white' ,fontdict=dict(size=8,style='italic'))

	st.pyplot(fig)
	st.text(f"Sintaxis: 'arr[{posicion_elemento}]'")

st.markdown("""
            #### Segmentación (Slicing)
            La segmentación te permite extraer partes específicas de un arreglo NumPy.

            Se utiliza la notación **[start :stop: step]**, donde **'start'** es el índice de inicio (inclusive),
             **'stop'** es el índice de parada (exclusivo), y **'step'** es el paso entre elementos.
             Ejemplos:
            """)
st.code("""
        # Segmentar el arreglo desde el segundo al cuarto elemento (índices 1 a 3)
        segmento = arr[1:4]
        print("Segmento:", segmento)

        # Segmentar con un paso de 2, tomando elementos alterno
        segmento_alterno = arr[::2]
        print("Segmento de elementos alterno:", segmento_alternos)
        """)
# Mostrando los ejemplos:
with st.expander("mostrar resultados: "):
    st.text("segmento ⬇️​ ")
    st.text(arr[1:4])
    st.text("segmento_alterno ⬇️​ ")
    st.text(arr[::2])


st.markdown("""
            #### Operaciones Matemáticas
            NumPy permite realizar operaciones matemáticas en arreglos de manera eficiente.
             Estas operaciones se aplican elemento por elemento. Veamos algunos ejemplos:
            """)
st.code("""
        import numpy as np

        # Creación de dos arreglos NumPy
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = np.array([6, 7, 8, 9, 10])

        # Suma de arreglos
        suma = arr1 + arr2
        print("Suma de arreglos:")
        print(suma)

        # Resta de arreglos
        resta = arr2 - arr1
        print("Resta de arreglos:")
        print(resta)

        # Multiplicación de arreglos
        multiplicacion = arr1 * arr2
        print("Multiplicación de arreglos:")
        print(multiplicacion)

        # División de arreglos
        division = arr2 / arr1
        print("División de arreglos:")
        print(division)
        """)

st.markdown("""
            #### Funciones Universales (Ufuncs)
            NumPy proporciona una amplia gama de funciones universales (ufuncs) que son operaciones matemáticas
             y estadísticas predefinidas que se pueden aplicar a elementos individuales de un arreglo NumPy.
             Estas ufuncs son extremadamente útiles y eficientes para realizar cálculos en arreglos grandes de manera rápida.
             A continuación, se muestran algunas de las ufuncs más comunes:
            """)
st.code("""
        import numpy as np

        # Creación de un arreglo NumPy
        arr = np.array([1, 2, 3, 4, 5])

        # Función 'sqrt' para calcular la raíz cuadrada de cada elemento
        raiz_cuadrada = np.sqrt(arr)
        print("Raíz cuadrada de elementos:")
        print(raiz_cuadrada)

        # Función 'exp' para calcular la exponencial de cada elemento
        exponencial = np.exp(arr)
        print("Exponencial de elementos:")
        print(exponencial)

        # Función 'sin' para calcular el seno de cada elemento (en radianes)
        seno = np.sin(arr)
        print("Seno de elementos:")
        print(seno)

        # Función 'log' para calcular el logaritmo natural de cada elemento
        logaritmo = np.log(arr)
        print("Logaritmo de elementos:")
        print(logaritmo)
        """)

st.markdown("""
            Las funciones universales son esenciales en el análisis de datos y en cálculos numéricos en general.
             Puedes aplicar estas funciones a arreglos NumPy completos o a elementos individuales,
             lo que facilita la realización de operaciones matemáticas y estadísticas en tus datos.

            La siguiente tabla lista los operadores aritméticos comunmente implementados por Numpy:

            | Operador	    | Ufunc equivalente   | Descripción                           |
            |---------------|---------------------|---------------------------------------|
            |``+``          |``np.add``           |Suma (e.g., ``1 + 1 = 2``)             |
            |``-``          |``np.subtract``      |Resta (e.g., ``3 - 2 = 1``)            |
            |``-``          |``np.negative``      |Negativo (e.g., ``-2``)                |
            |``*``          |``np.multiply``      |Multiplicación (e.g., ``2 * 3 = 6``)   |
            |``/``          |``np.divide``        |División (e.g., ``3 / 2 = 1.5``)       |
            |``//``         |``np.floor_divide``  |Floor division (e.g., ``3 // 2 = 1``)  |
            |``**``         |``np.power``         |Potenciación (e.g., ``2 ** 3 = 8``)    |
            |``%``          |``np.mod``           |ModulO/resto div. (e.g., ``9 % 4 = 1``)|
            
            Continúa explorando estas funciones para potenciar tus habilidades de manipulación numérica con NumPy.
            """)