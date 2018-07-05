import random
import os
qtd = int(input())
count = 0
while(qtd!=count):
    teste = int(input())
    if(teste==random.randint(1, 10)):
        print("AHHHHHHHHHH EH VERDADE")
        os._exit(0)
    count = count +1
print("Suas tentativas nao deram certo amigao,uma pena nao é?")
