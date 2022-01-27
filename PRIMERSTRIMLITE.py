# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:24:11 2022

@author: gianella.martinez
"""

import streamlit as st
import joblib #cargar en el entorno el .pk
import numpy as np #cargar la libreria

st.title ('Compra de Arneses y Botas para perros')

st.header("Tienda RED")

st.subheader("Ingrese los datos de su perro")


model_filename = 'perros.pkl'
# Cargamos el modelo desde el archivo
loaded_model = joblib.load(model_filename)
 # Preparar los datos de entrada para el modelo
inputs = np.array(40).reshape(-1, 1)

# Usamos el modelo para hacer predicciones
predicted_boot_size = loaded_model.predict(inputs)[0]

arnes=0

#arnes = st.slider('Tamaño del Arnés', 0, 100, 0)



arnes = int(arnes)

# Compute the plot
c1, c2, c3 = st.columns([1, 4, 5])

arnes = c2.slider(
    label="Tamaño del Arnés",
    min_value=0,
    max_value=100,
    value=39,
    step=1)

if c2.button("Calcular"):


    inputs = np.array(arnes).reshape(-1, 1)
    
    # Usamos el modelo para hacer predicciones
    predicted_boot_size = loaded_model.predict(inputs)[0]
    
    
    mensaje = "El modelo estima un tamaño de bota: " + str(round(predicted_boot_size))
    c3.success(mensaje)















