#Biblioteca necessária pra fazer a request na API
#Baixe ela com o comando pip install requests
import requests 

#Aqui fazemos a requisição pra API e já passamos para JSON
games = requests.get("http://worldcup.sfg.io/matches").json()

#Nesse loop pegamos cada jogo da requisição acima e guardamos na variável "game"
for game in games:
    #Se o "status" desse jogo for "completed".
    #Mude pra "in progress" senão só vai ver os jogos já terminados!
    #if(game['status'] == "completed"):
    #if(game['stage_name'] == "First stage"):
   
    
       # ht = game['home_team_country']
       # at = game['away_team_country']
       # hg = game['home_team']['goals']
        #ag = game['away_team']['goals']
        #venue = game['venue']
        
        
        #Salvando as informações em variáveis para ficar mais facil de entender
       # home_team  = game['home_team']['code']
       # home_score = game['home_team']['penalties']
       # away_team  = game['away_team']['code']
        #away_score = game['away_team']['penalties']
        #celsius    = game['weather']['temp_celsius']
        
        #Print do resultado dos jogos
        
        #print("{} {} X {} {}".format(home_team, home_score, away_team, away_score))

    # print("Temperatura = {} Estadio = {} TIMES : {} {} X {} {}".format(celsius, venue, home_team, home_score, away_team, away_score))
        # print("{} : {} X {} : {} IN  {}".format(ht, hg, at, ag, venue))

input("Pressione qualquer tecla para sair...")
