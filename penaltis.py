import random
import keyboard
import time

golsJ = 0
golsCp = 0

def jogador():
    print("De qual lado deseja bater o pênalte? (a esquerda, d direita, m meio)")
    while True:
        if keyboard.is_pressed("a"):
            print("Você escolheu o lado esquerdo")
            break
        elif keyboard.is_pressed("d"):
            print("Você escolheu o lado direito")
            break
        elif keyboard.is_pressed("m"):
            print("Você escolheu o meio")
            break       
        elif keyboard.is_pressed("q"):
            placar()
    time.sleep(1)

    print("Qual a altura da cobrança? (w alto, b baixo)")
    while True:
        if keyboard.is_pressed("w"):
            print("Você chutará no alto")
            break
        elif keyboard.is_pressed("b"):
            print("Você chutará baixo")
            break
        elif keyboard.is_pressed("q"):
            placar()

    time.sleep(2)

    print("Se prepara para a cobrança...")
    time.sleep(2)
    print("Autorizado!")
    while True:
        if keyboard.is_pressed("space"):
            break
        elif keyboard.is_pressed("q"):
            placar()

    actions = ["gol", "defendido", "fora", "trave"]
    porcentagem = [55, 20, 15, 10]
    resultadoJ = random.choices(actions, weights=porcentagem)[0]

    if resultadoJ == "gol":
        print("Goooooool!")
        global golsJ
        golsJ += 1
    elif resultadoJ == "defendido":
        print("Defendeeeeu!")
    elif resultadoJ == "fora":
        print("Pra foooora!")
    elif resultadoJ == "trave":
        print("Na traaave!")

def computador():
    ladoC = random.choice(["A", "M", "D"])
    alturaC = random.choice(["W", "B"])
    print("O computador se prepara...")
    time.sleep(2)
    print("Autorizado a cobrança do computador!")
    time.sleep(2)

    actions2 = ["gol", "defendido", "fora", "trave"]
    porcentagem = [55, 20, 15, 10]
    resultadoCp = random.choices(actions2, weights=porcentagem)[0]

    if resultadoCp == "gol":
        print("Goooooool!")
        global golsCp
        golsCp += 1
    elif resultadoCp == "defendido":
        print("Defendeeeeu!")
    elif resultadoCp == "fora":
        print("Pra foooora!")
    elif resultadoCp == "trave":
        print("Na traaave!")

def placarFinal():
    global golsJ, golsCp
    print("Placar final")
    print(f"Jogador {golsJ} X Computador {golsCp}")

    if golsJ > golsCp:
        print("Você venceu as cobranças de pênalti!")
    elif golsJ < golsCp:
        print("O computador ganhou as cobranças de pênalti!")
    elif golsJ == golsCp:
        print("Vamos para as alternadas!")

def placar():
    global golsJ, golsCp
    print(f"Placar atual: Jogador {golsJ} X Computador {golsCp}")

def sortear():
    sorteio = random.choice(["Jogador", "Computador"])
    print(f"{sorteio} começará cobrando.")
    return sorteio

def main():
    print("Seja bem-vindo ao jogo de pénaltis!")
    global golsJ, golsCp
    cobranca = 0

    sortearQ = sortear()

    for cobranca in range(5):
        if sortearQ == "Jogador":
            print(f"Cobrança {cobranca + 1}: Jogador")
            jogador()
            print(f"\nCobrança {cobranca + 1}: Computador")
            computador()
        else:
            print(f"\nCobrança {cobranca + 1}: Computador")
            computador()
            print(f"\nCobrança {cobranca + 1}: Jogador")
            jogador()

        if golsJ > (golsCp + (5 - cobranca - 1)):
            print("Você venceu! O computador não pode mais alcançar.")
            return
        if golsCp > (golsJ + (5 - cobranca - 1)):
            print("O computador venceu! Você não pode mais alcançar.")
            return

    placarFinal()

main()
