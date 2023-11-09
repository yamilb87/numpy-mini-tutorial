import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Capítulo 7: Casos de Uso Avanzados')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            En este séptimo capítulo, exploraremos algunos casos de uso avanzados de NumPy en situaciones prácticas.
            Estos ejemplos están diseñados para ser accesibles incluso si no tienes una base sólida en matemáticas o cálculos avanzados.

            #### Procesamiento de Imágenes
            El procesamiento de imágenes con NumPy puede ser emocionante y útil.
            Aquí veremos cómo trabajar con imágenes y realizar algunas operaciones simples.
        
            ##### Paso 1: Cargar una Imagen
            Para cargar una imagen en un arreglo NumPy, primero necesitas una imagen en tu computadora.
            Puede ser cualquier imagen que tengas a mano, como una foto tuya o una imagen descargada de Internet.
        
            Coloca la imagen en la misma carpeta que tu archivo Python o especifica la ruta completa de la imagen.
            Utiliza el siguiente código para cargar la imagen:
            """)

st.code("""
        import numpy as np
        import matplotlib.pyplot as plt

        # Reemplaza "imagen.jpg" con el nombre de tu imagen y su extensión
        imagen = plt.imread("imagen.jpg")
        """)

st.markdown("""
            ##### Paso 2: Manipular la Imagen
            Una vez que tengas la imagen en un arreglo NumPy, puedes realizar algunas operaciones sencillas.

            Por ejemplo, puedes cambiar el tamaño de la imagen, suavizarla o incluso rotarla. Vamos a ver cómo hacerlo.
            """)

st.code("""
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy import ndimage

        # Cambiar el tamaño de la imagen
        imagen_redimensionada = ndimage.zoom(imagen, (0.5, 0.5, 1))

        # Aplicar un filtro de suavizado
        imagen_suavizada = ndimage.gaussian_filter(imagen, sigma=(5, 5, 0))

        # Rotar la imagen
        imagen_rotada = ndimage.rotate(imagen, angle=45)
        """)

st.markdown("""
            Estos son solo ejemplos simples de manipulación de imágenes.
            Puedes explorar más funciones y técnicas de procesamiento de imágenes a medida que avanzas en tu aprendizaje.

            ---

            #### Cálculo Numérico
            NumPy es una herramienta poderosa en el cálculo numérico y la resolución de problemas matemáticos.
            Veamos un ejemplo de cómo usar NumPy en un contexto práctico.

            ##### Paso 1: Definir una Ecuación Diferencial
            Supongamos que quieres modelar cómo cambia una cantidad a lo largo del tiempo según una regla simple. No te preocupes si no tienes experiencia en ecuaciones diferenciales; este es un ejemplo simple.

            Digamos que tienes una cantidad `y` que cambia con el tiempo `t` según esta regla:
            """)

st.code("""
        dy/dt = -2 * t * y
        """,
        language='bash')

st.markdown("""
            Esta ecuación describe cómo y cambia con el tiempo, y NumPy puede ayudarnos a resolverla.

            ##### Paso 2: Resolver la Ecuación Diferencial
            Utilizaremos una función de SciPy llamada [solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
            para resolver esta ecuación.
            Primero, debemos definir la función que describe la ecuación y luego especificar el rango de tiempo en el que queremos observar el cambio.
            """)

st.code("""
        import numpy as np
        from scipy.integrate import solve_ivp
        import matplotlib.pyplot as plt

        # Paso 1: Definir la Ecuación Diferencial
        def ecuacion_diferencial(t, y):
            dydt = -2 * t * y
            return dydt

        # Paso 2: Definir el Rango de Tiempo
        tiempo = (0, 5)

        # Resolver la Ecuación Diferencial
        solucion = solve_ivp(ecuacion_diferencial, tiempo, [1])

        # Paso 3: Graficar la Solución
        plt.plot(solucion.t, solucion.y[0])
        plt.xlabel("Tiempo")
        plt.ylabel("y(t)")
        plt.show()
        """)

st.markdown("""
            En este ejemplo, estamos viendo cómo cambia `y` con el tiempo. No necesitas profundizar en la matemática detrás de esto,
            pero es un ejemplo de cómo NumPy puede ayudarte a modelar situaciones del mundo real.

            Esperamos que estos ejemplos te ayuden a comprender cómo NumPy se puede aplicar en casos prácticos,
            incluso si no tienes una sólida formación en matemáticas o cálculos avanzados.
            NumPy es una herramienta versátil que puede ser útil en una variedad de aplicaciones.
            """)