import os
import requests
import json

def get_wikipedia_text(entrada):
    params = {
        'format': 'json',
        'action': 'query',
        'prop': 'extracts',
        'exintro': '',
        'explaintext': '',
        'redirects': 1,
        'titles': entrada
    }

    req = requests.get(url, params=params).json()
    
    # Verificar si la página existe
    if 'query' in req and 'pages' in req['query']:
        n_page = list(req['query']['pages'].keys())[0]
        return req['query']['pages'][n_page]['extract']

    return None

def save_to_file(texto, entrada, output_folder):
    filename = f'{entrada}.txt'
    filepath = os.path.join(output_folder, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(texto)

# Lista de nombres de empresas
entradas = [
    "ExxonMobil", 
    "Apple", 
    "Bank of America",
    "Berkshire Hathaway",
    "Alphabet", 
    "Amazon", 
    "UnitedHealth Group", 
    "Lamborghini",
    "Johnson & Johnson", 
    "Walmart",
    "Home Depot",
    "Visa",
    "Mastercard",
    "Procter & Gamble",
    "Coca-Cola",
    "Wells Fargo",
    "Chevron",
    "AT&T",
    "PepsiCo",
    "IBM",
    "Goldman Sachs",
    "General Electric",
    "Ford Motor Company",
    "United Technologies Corporation",
    "Intel Corporation",
    "Pfizer",
    "Merck & Co.",
    "Microsoft",
    "DuPont",
    "Cisco"
]

# Obtener la ruta del directorio actual
script_directory = os.path.dirname(os.path.abspath(__file__))

# Crear las carpetas si no existen
carpeta1_path = os.path.join(script_directory, 'carpeta1')
carpeta2_path = os.path.join(script_directory, 'carpeta2')

os.makedirs(carpeta1_path, exist_ok=True)
os.makedirs(carpeta2_path, exist_ok=True)

url = "https://en.wikipedia.org/w/api.php"
i = 1

for entrada in entradas:
    texto = get_wikipedia_text(entrada)

    if texto is not None:
        texto = '{}<splittername>{}'.format(i, json.dumps(texto))

        output_folder = carpeta1_path if i <= 15 else carpeta2_path
        save_to_file(texto, entrada, output_folder)

        i += 1