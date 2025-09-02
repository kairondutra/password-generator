# 1. Importar as bibliotecas necessárias
import random
import string

# 2. Definir os conjuntos de caracteres disponíveis
# Usamos a biblioteca 'string' para ter acesso fácil a estes conjuntos sem precisar digitá-los.
caracteres = {
    "letras_minusculas": string.ascii_lowercase,
    "letras_maiusculas": string.ascii_uppercase,
    "numeros": string.digits,
    "simbolos_especiais": string.punctuation
}

# 3. Interagir com o usuário para obter as configurações da senha
print("\nBem-vind@ ao Gerador de Senhas!")

# Solicita o tamanho da senha e valida se o valor é um número inteiro
try:
    comprimento_senha = int(input("Informe o tamanho que deseja para a senha: "))
except ValueError:
    # Caso o valor não seja um número, exibe um erro e encerra o programa
    print("\nERRO: O valor informado não é um número válido.")
    exit()

# Pergunta ao usuário quais tipos de caracteres ele deseja incluir na senha
print("\nResponda com 's' para sim ou 'n' para não.")
usar_letras_minusculas = input("Deseja usar letras minúsculas? ").lower() == "s"
usar_letras_maiusculas = input("Deseja usar letras maiúsculas? ").lower() == "s"
usar_numeros = input("Deseja usar números? ").lower() == "s"
usar_caracteres_especiais = input("Deseja usar caracteres especiais? ").lower() == "s"

# 4. Construir a base de caracteres com base nas escolhas do usuário
caracteres_escolhidos = ''
if usar_letras_minusculas:
    caracteres_escolhidos += caracteres["letras_minusculas"]
if usar_letras_maiusculas:
    caracteres_escolhidos += caracteres["letras_maiusculas"]
if usar_numeros:
    caracteres_escolhidos += caracteres["numeros"]
if usar_caracteres_especiais:
    caracteres_escolhidos += caracteres["simbolos_especiais"]

# Verificação de segurança: garante que o usuário escolheu pelo menos uma opção
if not caracteres_escolhidos:
    print("\nERRO: Você precisa escolher pelo menos um tipo de caractere para gerar a senha.")
    exit()

# 5. Gerar e exibir a senha final
# A função 'random.choices' sorteia 'k' caracteres da nossa base de escolhidos
# O ''.join() transforma a lista de caracteres sorteados em uma única string
senha_gerada = ''.join(random.choices(caracteres_escolhidos, k=comprimento_senha))

print("-"*40)
print(f"Senha Gerada: {senha_gerada}\n")