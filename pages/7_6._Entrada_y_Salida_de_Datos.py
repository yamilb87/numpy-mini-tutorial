import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Capítulo 6: Entrada y Salida de Datos')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En este sexto capítulo, aprenderemos cómo leer y escribir datos utilizando NumPy. Trabajaremos con diferentes formatos de archivo para importar y exportar datos de manera eficiente.

            #### Lectura de Datos desde Archivos
            ##### Desde Archivos de Texto
            Puedes utilizar la función [np.loadtxt()](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html)
            para cargar datos desde archivos de texto, como archivos CSV.
            Supongamos que tenemos un archivo CSV llamado `"datos.csv"` con el siguiente contenido:
            """)
st.code("""
        1,2,3
        4,5,6
        7,8,9
        """)

st.code("""
        import numpy as np

        # Cargar datos desde un archivo CSV
        datos = np.loadtxt("datos.csv", delimiter=",")
        print("Datos desde archivo CSV:")
        print(datos)
        """)

st.markdown("""
            #####Desde Archivos Binarios
            NumPy también puede cargar datos desde archivos binarios utilizando
            [np.fromfile()](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html).
            Asegúrate de que los datos estén en un formato compatible con NumPy.
            """)
st.code("""
        import numpy as np

        # Cargar datos desde un archivo binario
        datos = np.fromfile("datos.bin", dtype=np.float64)
        print("Datos desde archivo binario:")
        print(datos)
        """)

st.markdown("""
            #### Escritura de Datos en Archivos
            ##### A Archivos de Texto
            Para guardar datos en archivos de texto, puedes utilizar 
            [np.savetxt()](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html).
            Supongamos que tienes un arreglo NumPy llamado `datos` y deseas guardarlo en un archivo CSV:
            """)
st.code("""
        import numpy as np

        # Crear un arreglo de ejemplo
        datos = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        # Guardar datos en un archivo CSV
        np.savetxt("datos_guardados.csv", datos, delimiter=",")
        """)

st.markdown("""
            ##### A Archivos Binarios
            Para guardar datos en archivos binarios, puedes utilizar
            [np.ndarray.tofile()](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html).
            Asegúrate de especificar el tipo de dato adecuado.
            """)
st.code("""
        import numpy as np

        # Crear un arreglo de ejemplo
        datos = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

        # Guardar datos en un archivo binario
        datos.ndarray.tofile("datos_guardados.bin")

        """)

st.markdown("""
            NumPy ofrece flexibilidad para leer y escribir datos en una variedad de formatos,
            lo que lo convierte en una herramienta poderosa para el manejo de datos en proyectos de ciencia de datos y análisis.
            Estas capacidades te permitirán cargar datos de fuentes externas y guardar resultados para su posterior análisis y compartición.
            """)