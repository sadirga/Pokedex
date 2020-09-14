######## TUGAS POKEMON ##########
import requests
from bs4 import BeautifulSoup
link = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name'
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
pokemons = soup.find_all('a')
x = pokemons[43:]
y = [i.text for i in x]
pokemon_list = []
for j in y:
    if len(j) > 1 :
        if j == 'gender symbol':
            break
        pokemon_list.append(j.lower())

print('==================== POKEDEX ====================')

pokemon = input('Input Pokemon Name: ').lower()
while pokemon[-3:] == 'mon':
    print('Please deh, itu nama Digimon, kamu salah lapak')
    pokemon = input('Input Pokemon Name: ').lower()
while pokemon not in pokemon_list:
    print(f'{pokemon} bukan nama Pokemon')
    pokemon = input('Input Pokemon Name: ').lower()
else:
    try:
        from bs4 import BeautifulSoup
        url2 = f'https://bulbapedia.bulbagarden.net/wiki/{pokemon}_(Pok%C3%A9mon)'
        web = requests.get(url2)
        dl = BeautifulSoup(web.content, 'html.parser')
        imgLinks = dl.findAll("a", {"class":"image"})
        imglink= [i.img['src'] for i in imgLinks]
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        data =  requests.get(url)
        pokedex = data.json()
        print(f'Nama Pokemon    : {pokemon.upper()}')
        print(f"HP              : {pokedex['stats'][0]['base_stat']}")
        print(f"Attack          : {pokedex['stats'][1]['base_stat']}")
        print(f"Defense         : {pokedex['stats'][2]['base_stat']}")
        print(f"Speed           : {pokedex['stats'][5]['base_stat']}")
        print(f"Type            : {pokedex['types'][0]['type']['name']}")
        print(f'URL Image       : https:{imglink[0]}')
        abilities = pokedex['abilities']
        x = 1
        print('Abilities       : ')
        for i in range(len(abilities)):
            print(x,".  ",abilities[i]['ability']['name'])
            x += 1
    except:
        print(f'Oops, Terjadi kesalahan, sepertinya kamu memasukkan jenis pokemonnya, \natau {pokemon} belum masuk sistem kami\nSilakan coba lagi dengan nama pokemon yang lain')