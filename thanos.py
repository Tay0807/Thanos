import random
print ("Thanos caiu em um bosque com 50 árvores e se escondeu entre uma delas, descubra em que árvore ele esta. Suas chances serão o nivel escolhido vezes 5. Boa sorte!")
print( "Escolha um nível: 3-Fácil 2-Médio 1-Difícil: ")
niveis = int(input("Digite qual o número do nivel: "))

chances = niveis * 5

arvores = random.randrange (0,50)

while chances > 0:
    
    tentativas= int(input("Digite um número: "))
    
    if tentativas > arvores:
        print("Está mais para a esquerda")
        chances -= 1
    elif tentativas < arvores:
        print("Está mais para a direita")
        chances -= 1
    else:
        print("Acertou")
        chances = 0