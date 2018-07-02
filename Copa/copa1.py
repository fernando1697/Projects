#Biblioteca necessária pra fazer a request na API
#Baixe ela com o comando pip install requests
import requests 

#Aqui fazemos a requisição pra API e já passamos para JSON
games = requests.get("http://worldcup.sfg.io/matches").json()

#Nesse loop pegamos cada jogo da requisição acima e guardamos na variável "game"
for game in games:
    #Se o "status" desse jogo for "completed".
    #Mude pra "in progress" senão só vai ver os jogos já terminados!
    if(game['status'] == "completed"):
        #Salvando as informações em variáveis para ficar mais facil de entender
        home_team  = game['home_team']['country']
        home_score = game['home_team']['goals']
        away_team  = game['away_team']['country']
        away_score = game['away_team']['goals']

        #Print do resultado dos jogos
        print("{} {} X {} {}".format(home_team, home_score, away_team, away_score))
