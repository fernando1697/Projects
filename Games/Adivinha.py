#biblioteca random
import random 
#biblioteca os para sair do programa
import os
#qtd = int(input())
count = 0
rando = random.randint(1, 20)
print("Vamos jogar!Tente adivinhar o numero que estou pensando em 10 tentativas!")
while(count!=10):
    
    teste = int(input())
    if(teste==rando):
        print("Parabéns voce acertou!")
        print("E gastou apenas {} tentativas!".format(count))
        #sai do programa
        os._exit(0) 
    elif(teste>rando):
        print("Tente um valor menor")
    elif(teste<rando):
        print("Tente um valor maior")
    count = count +1
print("Suas tentativas nao deram certo amigao,uma pena nao é?")
