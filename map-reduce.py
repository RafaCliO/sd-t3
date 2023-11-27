import os
from collections import defaultdict

def generar_indice_invertido(directorio):
    indice_invertido = defaultdict(list)

    archivos = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.txt')]

    for archivo in archivos:
        ruta_archivo = os.path.join(directorio, archivo)
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
            palabras = contenido.split()

            for indice, palabra in enumerate(palabras):
                indice_invertido[palabra].append((archivo, indice + 1))

    return indice_invertido

def guardar_indice_en_archivo(indice, nombre_archivo_salida):
    with open(nombre_archivo_salida, 'w', encoding='utf-8') as file:
        for palabra, apariciones in indice.items():
            line = f'{palabra}: {apariciones}\n'
            file.write(line)

directorio = './carpeta1/'
nombre_archivo_salida = 'indice_invertido.txt'

indice = generar_indice_invertido(directorio)
guardar_indice_en_archivo(indice, nombre_archivo_salida)
