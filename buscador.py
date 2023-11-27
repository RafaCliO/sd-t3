import json
import argparse

def obtener_top_5_archivos_con_palabra(palabra, archivo_indice):
    with open(archivo_indice, 'r', encoding='utf-8') as file:
        # Leer el archivo de índice invertido
        contenido = file.readlines()
        indice = {}
        for line in contenido:
            # Separar la palabra del resto del contenido en la línea
            partes = line.strip().split(': ')
            if len(partes) == 2:
                key = partes[0]
                value = partes[1]
                indice[key] = eval(value)

    # Verificar si la palabra está en el índice
    if palabra in indice:
        apariciones = indice[palabra]
        top_5_archivos = sorted(apariciones, key=lambda x: x[1], reverse=True)[:5]
        resultado = [{"archivo": archivo, "apariciones": apariciones} for archivo, apariciones in top_5_archivos]
        return json.dumps(resultado, indent=4)
    else:
        return json.dumps({"mensaje": "La palabra no se encuentra en el índice"}, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Buscador')
    parser.add_argument('termino_a_buscar', type=str, help='Palabra a buscar')
    args = parser.parse_args()

    archivo_indice = 'indice_invertido.txt'
    palabra_buscada = args.termino_a_buscar

    resultado_busqueda = obtener_top_5_archivos_con_palabra(palabra_buscada, archivo_indice)
    print(resultado_busqueda)