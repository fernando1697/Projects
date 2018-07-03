import requests as req
#Input nome da carta



card = input("Nome da carta : ")
#Requisição da busca
requestLink = "http://pokeprices.doeiqts.com/api/findcards?cardname={}".format(card.lower())

#print(requestLink)
#pega informações depois do filtro card
cardinfo = req.get(requestLink).json()

    
for card in cardinfo['cards']:
    #print(card['name'])
        print("{} {} {} = {}$".format(card['rarity'],card['set'],card['name'],card['price'])) 
            
input("Pressione qualquer tecla para sair...")

