# Desafio: Jogo de Adivinhação
# Autor: Gui
# Descrição: O jogador deve tentar adivinhar o número secreto em até 5 tentativas.

# Número secreto definido pelo programador
numero_secreto = 23

print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 5 tentativas para descobrir o número secreto.\n")

# O jogador terá até 5 tentativas
for tentativa in range(1, 6):
    print(f"Tentativa {tentativa} de 5")
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("\n🎉 Parabéns! Você acertou o número secreto! 🎉")
        break
    elif palpite > numero_secreto:
        print("O número secreto é menor que o seu palpite.\n")
    else:
        print("O número secreto é maior que o seu palpite.\n")

else:
    # Executa se o loop terminar sem acerto
    print("\n❌ Suas tentativas acabaram! Você perdeu.")
    print(f"O número secreto era {numero_secreto}.")
