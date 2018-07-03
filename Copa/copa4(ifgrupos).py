import requests

games = requests.get("https://worldcup.sfg.io/teams/").json()

for game in games:

    if(game['group_letter'] == 'A' or game['group_letter'] == 'E' or game['group_letter'] == 'D'):

        country = game['country']
        group = game['group_letter']
        

        print(country,group)


        #API https://worldcup.sfg.io/teams/

        
