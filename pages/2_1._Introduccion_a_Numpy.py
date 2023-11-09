import streamlit as st
import numpy as np
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG -------------------------- #
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Capítulo 1: Introducción a NumPy')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En este primer capítulo, nos introduciremos a [NumPy](https://numpy.org/), una biblioteca esencial en Python para el manejo eficiente de arreglos numéricos.
             Exploraremos qué es NumPy, cómo instalarlo y cómo crear arreglos numéricos básicos. Empecemos.
            """)

# Qué es Numpy?
st.markdown("""
            #### ¿Qué es NumPy?
            NumPy, que significa "Numerical Python", es una biblioteca de Python que proporciona estructuras de datos para trabajar con
             arreglos multidimensionales y funciones para operaciones matemáticas y estadísticas en estos arreglos.
             NumPy es ampliamente utilizado en el ámbito de la ciencia de datos, el procesamiento de señales,
             la investigación en física y muchas otras disciplinas científicas y técnicas debido a su eficiencia y versatilidad.
            
            #### Instalación de NumPy
            Si aún no tienes NumPy instalado en tu entorno de Python, puedes hacerlo utilizando pip:
            """)

st.code("""
        pip install numpy
        """,
        language='bash')

# SQL
st.write("Asegúrate de tener Python instalado en tu sistema antes de ejecutar esta instrucción.")

st.markdown("""
            #### Creación de Arreglos Numéricos
            Comencemos creando arreglos NumPy básicos:
            """)
st.code("""                
        import numpy as np  # Importamos NumPy con el alias 'np' para abreviar

        # Creación de un arreglo NumPy a partir de una lista
        arr_lista = np.array([1, 2, 3, 4, 5])
        print("Arreglo desde una lista:")
        print(arr_lista)

        # Creación de un arreglo NumPy con valores predeterminados
        arr_zeros = np.zeros(5)  # Un arreglo de 5 elementos lleno de ceros
        print("Arreglo de ceros:")
        print(arr_zeros)

        arr_ones = np.ones(5)  # Un arreglo de 5 elementos lleno de unos
        print("Arreglo de unos:")
        print(arr_ones)

        # Creación de un arreglo NumPy con valores secuenciales
        arr_secuencia = np.arange(0, 10, 2)  # Valores desde 0 hasta 10 (sin incluirlo) con paso 2
        print("Arreglo de valores secuenciales:")
        print(arr_secuencia)

        # Creación de un arreglo NumPy con valores espaciados uniformemente
        arr_espaciado = np.linspace(0, 1, 5)  # 5 valores espaciados uniformemente entre 0 y 1
        print("Arreglo de valores espaciados:")
        print(arr_espaciado)
        """)

st.markdown("""
            ---
            En este capítulo, hemos aprendido qué es NumPy, cómo instalarlo y cómo crear arreglos NumPy utilizando varias técnicas.
             Estos arreglos son la base para realizar cálculos numéricos y realizar análisis de datos más avanzados en Python.
             En el próximo capítulo, profundizaremos en las operaciones que podemos realizar en estos arreglos NumPy.
            """)