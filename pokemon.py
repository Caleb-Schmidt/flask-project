import requests, json

def get_poke_info(poke_char):
    poke_char = {
    f"{poke_char}_name": response.json()["forms"][0]["name"],
    f"{poke_char}_ability": response.json()["abilities"][0]["ability"]["name"],
    f"{poke_char}_exp": response.json()["base_experience"],
    f"{poke_char}_sprite": response.json()["sprites"]["front_shiny"]
    }

class PokemonAPI():

    def get_poke_info(self, poke_char):
        poke_char = {
        "pokemon_name": response.json()["forms"][0]["name"],
        "pokemon_ability": response.json()["abilities"][0]["ability"]["name"],
        "pokemon_exp": response.json()["base_experience"],
        "pokemon_sprite": response.json()["sprites"]["front_shiny"]
        }
        return poke_char

pokemon = input("What pokemon would you like to see?: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
response = requests.get(url)

poke_call = PokemonAPI()
print(poke_call.get_poke_info(pokemon))