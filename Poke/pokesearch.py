#Biblioteca necessária para requests HTTP
import requests as req

#Pede o nome de um Pokemon ao usuário
pokeName = input("Digite o nome de um Pokémon: ")

#Cria o link da request, por questões de legibilidade
requestLink = "https://pokeapi.co/api/v2/pokemon/{}".format(pokeName.lower())

#Busca informações na API e guarda como JSON
pokeInfo = req.get(requestLink).json()

#Printa as informações trazidas pela API
print("================================================")
print("Pokémon Pesquisado: {}".format(pokeName.title()))
print("ID do Pokémon: {}".format(pokeInfo['id']))
print("Peso do Pokémon: {}".format(pokeInfo['weight']))
print("Habilidades: ")
for ability in pokeInfo['abilities']:
    print(" |-> {}".format(ability['ability']['name'].title()))
    

