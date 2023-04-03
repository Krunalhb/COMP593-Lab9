import requests

POKE_API_URL = "https://pokeapi.co/api/v2/pokemon/"

def main():
    pokemon_name = input("Enter the name of a Pokémon to fetch its information: ")
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info:
        print("Here is the information for " + pokemon_name.title() + ":")
        print(pokemon_info)
    else:
        print("Failed to retrieve information for " + pokemon_name.title() + ". Please try again.")

def get_pokemon_info(pokemon_name):
    """
    Gets information about a specified Pokémon from the PokéAPI.
    
    Args:
        pokemon_name (str): The name of the Pokémon to fetch.
    
    Returns:
        dict: A dictionary containing all the Pokémon information fetched from the PokéAPI, if retrieved
        successfully. Returns None if the Pokémon information is not fetched successfully.
    """
    pokemon_name = str(pokemon_name).strip().lower()

    # Construct the API URL for the specified Pokémon
    url = POKE_API_URL + pokemon_name

    # Send Get request for pokemon info
    print(f'Getting information for {pokemon_name}...', end='')
    resp_msg = requests.get(url)

    # Check if the request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        #Return dictionary of pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.content})')
        return

if __name__=='__main__':
    main()
