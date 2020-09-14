# Pokedex Exercise  
<hr>

First of all I took the resource from these 2 sites:
> 1. 
<img src="pokeapi.png" width="130" height ='70' />  

[Poke API Website](https://pokeapi.co/)  
They provide everything about pokemon!  

<br>

> 2. 
<img src="BULBA.png" width="130" height ='70' />  

[Bulbapedia Website](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name)  
I use this website for scraping pokemon images, they have bigger image then Poke API so yeah thats the reason.

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
```

