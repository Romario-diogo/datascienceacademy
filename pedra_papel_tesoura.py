"""
escolha 
1 = pedra 
2 = papel 
3 = tesoura 

entrada escolhe 
tratamento da entrada para int 
sistema sorteia (rando 1 a 3)

se entrada == sistema 
    empate
se não se entrada == 1
    se sistema == 2
        sistema vence
    se sistema == 3 
        sistema perde

se não se entrada == 2
    se sistema == 1 
        sistema perde
    se sistema == 3
        sistema vence 

se não se entrada == 3
    se sistema == 1 
        sistema vence
    se sistema == 2
        sistema perde 

se não 
    escolha errada tente novamente !
    repita tudo !!!!
        
"""
usuario_pont = 0
sistema_pont = 0

import random
#opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
opcoes = {
    1: "🪨  Pedra",
    2: "📄 Papel",
    3: "✂️  Tesoura"
}

def placar(usuario, sistema, final=False):
    print("==========================")
    if final:
        print("Placar final do jogo")
    else:
        print("Placar do jogo")
    print(f"Você -> {usuario}")
    print(f"Sistema -> {sistema}")
    print("==========================")


while True:
    print("=============================")
    print("Escolha uma das opções abaixo")
    if sistema_pont == 0 and usuario_pont == 0:
        print("Bem-Vindo ao jogo ")
    else:
        print("Continue.....")
    print("Digite para jogar")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Sair")
    escolha = input("")
    print("=============================")
    sistema = random.randint(1,3)



    if escolha.isdigit():
        escolha_int = int(escolha)
        if escolha_int < 1 or escolha_int > 4:
            print("Escolha entre o intervalo de 1 a 4")
            continue
    else:
        print("O numero digitado esta incorreto, digite uma das escolhas")
        continue
    if sistema == escolha_int:
        print("Empate")
        placar(usuario_pont, sistema_pont)
        continue
    match escolha_int:
        case 1:
            if sistema == 2:
                print("Sistema pontuou!")
                sistema_pont += 1
            else:
                print("Você pontou!")
                usuario_pont += 1
               
            print(f"Você: {opcoes[escolha_int]} vs sistema: {opcoes[sistema]}")
            placar(usuario_pont, sistema_pont)

        case 2:
            if sistema == 3:
                print("Sistema pontuou!")
                sistema_pont += 1
            else:
                print("Você pontou!")
                usuario_pont += 1
            
            print(f"Você: {opcoes[escolha_int]} vs sistema: {opcoes[sistema]}")
            placar(usuario_pont, sistema_pont)
        case 3:
            if sistema == 1:
                print("Sistema pontuou!")
                sistema_pont += 1
            else:
                print("Você pontou!")
                usuario_pont += 1
            print(f"Você: {opcoes[escolha_int]} vs sistema: {opcoes[sistema]}")
            placar(usuario_pont, sistema_pont)
        case 4:
            if sistema_pont == 0 and usuario_pont == 0:
                print("Jogue pelomenos uma vez para sair")
                placar(usuario_pont, sistema_pont)
            else:
                placar(usuario_pont, sistema_pont, True)
                break
