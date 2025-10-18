# Desafio: Organização de evento escolar

# Quantidade máxima de ingressos disponíveis
INGRESSOS_TOTAIS = 100
# Limite máximo de convidados permitido
LIMITE_CONVIDADOS = 20

# Entrada de dados
alunos = int(input("Digite a quantidade de alunos: "))
monitores = int(input("Digite a quantidade de monitores: "))
convidados = int(input("Digite a quantidade de convidados: "))

# Cálculo do total de pessoas
total_pessoas = alunos + monitores + convidados

# Verificação das condições
if convidados > LIMITE_CONVIDADOS:
    print("Quantidade de convidados excede o limite de 20.")
elif total_pessoas > INGRESSOS_TOTAIS:
    print("Número total de pessoas excede os 100 ingressos disponíveis.")
else:
    print("Tudo certo! O evento pode ser realizado dentro dos limites.")
    print(f"Total de pessoas: {total_pessoas}")
    print(f"Ingressos restantes: {INGRESSOS_TOTAIS - total_pessoas}")
