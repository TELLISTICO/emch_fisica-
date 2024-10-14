import streamlit as st
import random

# Función para generar un ejercicio de cinemática
def generar_ejercicio():
    # Ejemplo simple: un objeto que cae desde una altura
    altura = random.randint(10, 100)  # Altura en metros
    tiempo = random.randint(1, 5)      # Tiempo en segundos
    return altura, tiempo

# Función para calcular la respuesta correcta
def respuesta_correcta(altura, tiempo):
    # Fórmula: d = 1/2 * g * t^2, donde g = 9.81 m/s^2
    g = 9.81
    distancia = 0.5 * g * (tiempo ** 2)
    return distancia

# Configuración de la página
st.title("Ejercicios de Cinemática")
st.write("Genera un ejercicio de cinemática y verifica tu respuesta.")

# Generar un nuevo ejercicio
if st.button("Generar ejercicio"):
    altura, tiempo = generar_ejercicio()
    st.session_state.altura = altura
    st.session_state.tiempo = tiempo
    st.write(f"Un objeto se deja caer desde una altura de {altura} metros.")
    st.write(f"¿Cuánto ha caído en {tiempo} segundos?")

# Entrada del usuario
respuesta_usuario = st.number_input("Tu respuesta (en metros):", min_value=0.0)

# Verificar la respuesta
if st.button("Verificar respuesta"):
    correcta = respuesta_correcta(st.session_state.altura, st.session_state.tiempo)
    if abs(correcta - respuesta_usuario) < 0.1:  # Tolerancia de 10 cm
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta correcta es {correcta:.2f} metros.")
