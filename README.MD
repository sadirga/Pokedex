<p align="center"> <img width="300" height ='200' src="https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/378462_335525306545013_1403366754_n.jpg?_nc_cat=102&_nc_sid=d2e176&_nc_ohc=GR1XOg5kpBUAX8lwy0z&_nc_ht=scontent-sin6-2.xx&oh=a391ffd87e7a69114aee5f0e41cc7ee4&oe=5F841100"> </p>  

# Pokedex Exercise  
<hr>

First of all I took the resource from these 2 sites:
> 1. 
<img src="pokeapi.png" width="170" height ='100' />  

[Poke API Website](https://pokeapi.co/)  
They provide everything about pokemon!  

<br>

> 2. 
<img src="BULBA.png" width="100" height ='100' />  

[Bulbapedia Website](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name)  
I use this website for scraping pokemon images, they have bigger image then Poke API so yeah thats the reason.

<hr>

The first step that I took is to scrap the pokemon list from bulbapedia,
I need their name format to get the images.
```python
import requests
from bs4 import BeautifulSoup
link = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name'
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
pokemons = soup.find_all('a')                       # the pokemon names found in 'a' tag
y = [i.text for i in pokemons]                      # store the names into a list in variable y
pokemon_list = []                                   # empty list for store a clean result of the pokemon names
for j in y:                                         # this loop is to get the clean result of the pokemon names
    if len(j) > 1 :                                 
        if j == 'gender symbol':
            break
        pokemon_list.append(j.lower())

print('==================== POKEDEX ====================')  # Aesthetics use only

pokemon = input('Input Pokemon Name: ').lower()             # Input command
while pokemon[-3:] == 'mon':                                # While Loop condition
    print('Please deh, itu nama Digimon, kamu salah lapak') # if the input has mon as digimon name have
    pokemon = input('Input Pokemon Name: ').lower()         # then we have to input the name again.

while pokemon not in pokemon_list:                          # Condition while the name is not in the list of pokemon names
    print(f'{pokemon} bukan nama Pokemon')                  # it'll print this
    pokemon = input('Input Pokemon Name: ').lower()         # And ask to input the pokemon name again

else:
    try:
        url2 = f'https://bulbapedia.bulbagarden.net/wiki/{pokemon}_(Pok%C3%A9mon)' # for scrapping imageof the pokemon
        web = requests.get(url2)    
        dl = BeautifulSoup(web.content, 'html.parser')          
        imgLinks = dl.findAll("a", {"class":"image"})
        imglink= [i.img['src'] for i in imgLinks]

        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'                # finding essentials Pokemon Information
        data =  requests.get(url)
        pokedex = data.json()

        print(f'Nama Pokemon    : {pokemon.upper()}')                       # Name of Pokemon
        print(f"HP              : {pokedex['stats'][0]['base_stat']}")      # HP Stats
        print(f"Attack          : {pokedex['stats'][1]['base_stat']}")      # Attack Stats
        print(f"Defense         : {pokedex['stats'][2]['base_stat']}")      # Defense Stats
        print(f"Speed           : {pokedex['stats'][5]['base_stat']}")      # Speed Stats
        print(f"Type            : {pokedex['types'][0]['type']['name']}")   # Type Stats
        print(f'URL Image       : https:{imglink[0]}')                      # The URL image of the pokemon
        abilities = pokedex['abilities']                                    # Pokemon available Abilities
        x = 1
        print('Abilities       : ')
        for i in range(len(abilities)):
            print(x,".  ",abilities[i]['ability']['name'])
            x += 1
    except:                                                                 # Handling unexpedted error
        print(f'Oops, Terjadi kesalahan, sepertinya kamu memasukkan jenis pokemonnya, \natau {pokemon} belum masuk sistem kami\nSilakan coba lagi dengan nama pokemon yang lain')
```

### That's it, a simple apps of POKEDEX