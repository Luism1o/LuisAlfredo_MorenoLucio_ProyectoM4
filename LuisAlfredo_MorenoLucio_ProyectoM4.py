import os  # Importa el módulo os para manipulación de archivos y directorios
import requests  # Importa el módulo requests para realizar solicitudes HTTP
import json  # Importa el módulo json para trabajar con datos JSON

# Función para obtener información de un Pokémon
def obtener_pokemon(nombre_pokemon):
    # URL de la API para obtener información de un Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    # Realiza una solicitud GET a la URL
    respuesta = requests.get(url)

    # Si la solicitud es exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Convierte la respuesta a formato JSON
        data = respuesta.json()
        # Extrae la URL de la imagen frontal del Pokémon
        imagen = data['sprites']['front_default']
        # Extrae el peso del Pokémon
        peso = data['weight']
        # Extrae la altura del Pokémon
        tamaño = data['height']
        # Extrae los movimientos del Pokémon
        movimientos = [move['move']['name'] for move in data['moves']]
        # Extrae las habilidades del Pokémon
        habilidades = [ability['ability']['name'] for ability in data['abilities']]
        # Extrae los tipos del Pokémon
        tipos = [tipo['type']['name'] for tipo in data['types']]

        # Crea un diccionario con la información del Pokémon
        pokemon_info = {
            "nombre": nombre_pokemon,
            "imagen": imagen,
            "peso": peso,
            "tamaño": tamaño,
            "movimientos": movimientos,
            "habilidades": habilidades,
            "tipos": tipos
        }

        # Llama a la función para guardar la información del Pokémon en un archivo JSON
        guardar_pokemon_en_json(pokemon_info)
        # Devuelve la información del Pokémon
        return pokemon_info
    else:
        # Si la solicitud no es exitosa, devuelve None
        return None

# Función para guardar la información del Pokémon en un archivo JSON
def guardar_pokemon_en_json(pokemon_info):
    # Si no existe el directorio 'pokedex', créalo
    if not os.path.exists('pokedex'):
        os.makedirs('pokedex')

    # Define el nombre del archivo usando el nombre del Pokémon
    nombre_archivo = f"pokedex/{pokemon_info['nombre']}.json"
    # Abre el archivo en modo escritura
    with open(nombre_archivo, 'w') as archivo:
        # Escribe la información del Pokémon en formato JSON en el archivo
        json.dump(pokemon_info, archivo, indent=4)

# Función principal del programa
def main():
    # Ciclo que se ejecuta indefinidamente hasta que se encuentre un Pokémon válido
    while True:
        # Solicita al usuario que ingrese el nombre de un Pokémon
        nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
        # Llama a la función para obtener la información del Pokémon
        pokemon = obtener_pokemon(nombre_pokemon)

        # Si se encuentra un Pokémon válido
        if pokemon:
            # Imprime la información del Pokémon
            print("Imagen:", pokemon['imagen'])
            print("Peso:", pokemon['peso'])
            print("Tamaño:", pokemon['tamaño'])
            print("Movimientos:", ', '.join(pokemon['movimientos']))
            print("Habilidades:", ', '.join(pokemon['habilidades']))
            print("Tipos:", ', '.join(pokemon['tipos']))
            # Sale del bucle si se encuentra un Pokémon válido
            break
        else:
            # Si el Pokémon no existe, muestra un mensaje de error y vuelve a solicitar otro nombre
            print("¡Ese Pokémon no existe! Inténtalo de nuevo.")

# Si este script es ejecutado directamente (no importado como un módulo)
if __name__ == "__main__":
    # Llama a la función principal del programa
    main()
