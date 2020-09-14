<p align="center"> <img width="300" height ='200' src="https://scontent-sin6-2.xx.fbcdn.net/v/t1.0-9/378462_335525306545013_1403366754_n.jpg?_nc_cat=102&_nc_sid=d2e176&_nc_ohc=GR1XOg5kpBUAX8lwy0z&_nc_ht=scontent-sin6-2.xx&oh=a391ffd87e7a69114aee5f0e41cc7ee4&oe=5F841100"> </p>  

# Pokedex Exercise  
<hr>

First of all I took the resource from these 2 sites:
> 1. 
<img src="pokeapi.png" width="150" height ='100' />  

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
```

