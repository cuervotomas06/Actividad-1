# Actividad 1 - Organizando Información con Estructuras de Datos

Nombre:Tomas Amaya 
Legajo: 17813/7

Taller de Lenguajes - Redictado, Segundo Semestre 2026

## Qué hace este programa
Guarda información de columnas de la Encuesta Permanente de Hogares (nombre, tipo, % de completitud) y genera un informe según el rol que se pida ('docente', 'investigador', 'analista'): muestra solo las columnas de interés de ese rol, filtradas por un porcentaje mínimo de completitud (si el rol lo tiene configurado) y ordenadas por nombre o por completitud. Si no se pide ningún rol, muestra todas las columnas ordenadas por completitud, de mayor a menor.

## Estructura de este repositorio
- `src/informe.py`: todo el código (los diccionarios `columnas` y `roles`, y las funciones `generar_informe` e `informar`).
- `notebook/Actividad_1.ipynb`: notebook para ejecutar y probar el código.
- `BITACORA.md`: decisiones tomadas y respuestas a las preguntas de la consigna.

## Cómo probarlo
Desde una terminal, parado en esta carpeta, ejecutar:

python3 src/informe.py

O abriendo el notebook con Jupyter (ver `notebook/Actividad_1.ipynb`).