import os
import requests
import json

def obtener_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        imagen = data['sprites']['front_default']
        peso = data['weight']
        tamaño = data['height']
        movimientos = [move['move']['name'] for move in data['moves']]
        habilidades = [ability['ability']['name'] for ability in data['abilities']]
        tipos = [tipo['type']['name'] for tipo in data['types']]

        pokemon_info = {
            "nombre": nombre_pokemon,
            "imagen": imagen,
            "peso": peso,
            "tamaño": tamaño,
            "movimientos": movimientos,
            "habilidades": habilidades,
            "tipos": tipos
        }

        guardar_pokemon_en_json(pokemon_info)
        return pokemon_info
    else:
        return None

def guardar_pokemon_en_json(pokemon_info):
    if not os.path.exists('pokedex'):
        os.makedirs('pokedex')

    nombre_archivo = f"pokedex/{pokemon_info['nombre']}.json"
    with open(nombre_archivo, 'w') as archivo:
        json.dump(pokemon_info, archivo, indent=4)

def main():
    while True:
        nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
        pokemon = obtener_pokemon(nombre_pokemon)

        if pokemon:
            print("Imagen:", pokemon['imagen'])
            print("Peso:", pokemon['peso'])
            print("Tamaño:", pokemon['tamaño'])
            print("Movimientos:", ', '.join(pokemon['movimientos']))
            print("Habilidades:", ', '.join(pokemon['habilidades']))
            print("Tipos:", ', '.join(pokemon['tipos']))
            break  # Sale del bucle si se encuentra un Pokémon válido
        else:
            print("¡Ese Pokémon no existe! Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
