import streamlit as st


# -------------------------- CONFIG -------------------------- #
PAGE_CONFIG = {"page_title":"Numpy Mini-Tutorial", 
               "page_icon":"🧊​​", 
               "layout":"wide", 
               "initial_sidebar_state":"expanded",
               "menu_items":{
                            'Get Help': 'https://github.com/yamilb87/numpy-mini-tutorial/blob/main/README.md',
                            'Report a bug': "https://github.com/yamilb87/numpy-mini-tutorial/issues",
                            'About': "https://github.com/yamilb87/numpy-mini-tutorial"
                            }
                }
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Mini Tutorial de Numpy 🔢​', anchor='title-pg1')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            Bienvenido al mini tutorial de [NumPy](https://numpy.org/), una biblioteca fundamental en el mundo de la computación científica en Python.
             En este tutorial, exploraremos las capacidades de _NumPy_ para trabajar con arreglos numéricos eficientes y 
            realizar operaciones matemáticas y estadísticas en ellos.
             Estos son los temas principales que cubriremos en este mini tutorial:
            """)

st.markdown("""
            #### Capítulo 1: Introducción a NumPy
            * **¿Qué es NumPy?**: Una introducción a la biblioteca NumPy y por qué es esencial en el análisis de datos
             y la ciencia computacional.
            
            * **Instalación de NumPy**: Cómo instalar NumPy en tu entorno de Python.

            * **Creación de Arreglos Numéricos**: Aprenderás cómo crear arreglos NumPy y entenderás sus características básicas.
            """)

st.markdown("""
            #### Capítulo 2: Operaciones Básicas en Arreglos
            * **Indexación y Segmentación**: Cómo acceder a elementos específicos y realizar segmentaciones en arreglos NumPy.

            * **Operaciones Matemáticas**: Realizar cálculos matemáticos elementales con arreglos NumPy.

            * **Funciones Universales (Ufuncs)**: Exploración de las funciones universales de NumPy para aplicar operaciones a elementos
             de arreglos.
            """)

st.markdown("""
            #### Capítulo 3: Forma y Tamaño de los Arreglos
            * **Forma de los Arreglos**: Cómo cambiar la forma de los arreglos y realizar transposiciones.

            * **Manipulación de Tamaño**: Aprenderás a agregar o eliminar elementos en un arreglo NumPy.

            * **Apilamiento de Arreglos**: Combinar varios arreglos en uno solo.
            """)

st.markdown("""
            #### Capítulo 4: Operaciones Estadísticas y de Álgebra Lineal
            * **Operaciones Estadísticas**: Cálculos de estadísticas descriptivas como media, mediana, varianza, etc., en arreglos.

            * **Álgebra Lineal**: Introducción a las operaciones de álgebra lineal, como multiplicación de matrices y
             resolución de sistemas de ecuaciones.
            """)

st.markdown("""
            #### Capítulo 5: Funcionalidades Avanzadas
            * **Broadcasting**: Cómo NumPy maneja automáticamente las operaciones en arreglos de diferentes formas.

            * **Indexado Booleano**: Uso de expresiones booleanas para indexar y filtrar arreglos.

            * **Manejo de Datos Faltantes**: Cómo tratar los valores NaN en arreglos.
            """)

st.markdown("""
            #### Capítulo 6: Entrada y Salida de Datos
            * **Lectura y Escritura de Datos**: Aprenderás a cargar datos desde archivos y guardar resultados en archivos usando NumPy.
            """)

st.markdown("""
            #### Capítulo 7: Casos de Uso Avanzados
            * **Procesamiento de Imágenes**: Breve introducción al procesamiento de imágenes con NumPy.

            * **Cálculo Numérico**: Aplicaciones en cálculo numérico y resolución de ecuaciones diferenciales.
            """)

st.markdown("""
            Este tutorial te proporcionará una sólida base en NumPy, lo que te permitirá realizar análisis de datos,
             procesamiento de señales, simulaciones numéricas y mucho más.
             ¡Exploremos el emocionante mundo de NumPy!
            """)
