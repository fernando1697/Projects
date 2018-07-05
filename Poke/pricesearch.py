import requests as req
#Input nome da carta
print("Quantas buscas?")
qtd = int(input()) 
count =0
while(count!=qtd):
    card = input("Nome da carta : ")
    count = count +1
#Requisição da busca
    requestLink = "http://pokeprices.doeiqts.com/api/findcards?cardname={}".format(card.lower())

#print(requestLink)
#pega informações depois do filtro card
    cardinfo = req.get(requestLink).json()

    
    for card in cardinfo['cards']:
    #print(card['name'])
        print("{} {} {} = {}$".format(card['rarity'],card['set'],card['name'],card['price'])) 
             
input("Suas {} buscas foram finalizadas,pressione qualquer tecla para sair...".format(count))

