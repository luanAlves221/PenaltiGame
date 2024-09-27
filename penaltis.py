import random
import keyboard
import time

golsJ = 0
golsCp = 0

def jogador():
    while True:
        print("De qual lado deseja bater o pênalte? (a esquerda, d direita, m meio)")
        if keyboard.is_pressed("a"):
            print("Você escolheu o lado esquerdo")
            break
        elif keyboard.is_pressed("d"):
            print("Você escolheu o lado direito")
            break
        elif keyboard.is_pressed("m"):
            print("Você escolheu o meio")
            break       

    time.sleep(2)

    while True:
        print("Qual a altura da cobrança? (w alto, b baixo)")
        if keyboard.is_pressed("w"):
            print("Você escolheu a altura alta")
            break
        elif keyboard.is_pressed("b"):
            print("Você escolheu a altura baixa")
            break

    time.sleep(2)

    print("Se prepara para a cobrança...")
    time.sleep(2)
    print("Autorizado!")
    while True:
        if keyboard.is_pressed("space"):
            break
        time.sleep(1)

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

def placar():
    global golsJ, golsCp
    print("Placar final")
    print(f"Jogador {golsJ} X Computador {golsCp}")

    if golsJ > golsCp:
        print("Você venceu as cobranças de pênalti!")
    elif golsJ < golsCp:
        print("O computador ganhou as cobranças de pênalti!")
    elif golsJ == golsCp:
        print("Vamos para as alternadas!")

def main():
    global golsJ, golsCp, cobranca
    cobranca = 0

    for cobranca in range(5):
        print(f"\nRodada {cobranca + 1}: Jogador")
        jogador()

        print(f"\nRodada {cobranca + 1}: Computador")
        computador()

        verPlacar()

        if golsJ > (golsCp + (5 - cobranca - 1)):
            print("Você venceu! O computador não pode mais alcançar.")
            return
        if golsCp > (golsJ + (5 - cobranca - 1)):
            print("O computador venceu! Você não pode mais alcançar.")
            return

    placar()

main()
