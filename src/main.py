# 1. Importar as bibliotecas
import random
import string

# Função para perguntas de sim/não
def perguntar_sim_nao(pergunta):
    """Exibe uma pergunta e retorna True para 's' e False para 'n'."""
    while True:
        resposta = input(pergunta).lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print("\nERRO: Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

# 2. Definir os conjuntos de caracteres disponíveis
# Usamos a biblioteca 'string' para ter acesso fácil a estes conjuntos sem precisar digitá-los.
caracteres = {
    "letras_minusculas": string.ascii_lowercase,
    "letras_maiusculas": string.ascii_uppercase,
    "numeros": string.digits,
    "simbolos_especiais": string.punctuation
}

opcoes_de_caracteres = [
    ("letras_minusculas", "Deseja usar letras minúsculas? "),
    ("letras_maiusculas", "Deseja usar letras maiúsculas? "),
    ("numeros", "Deseja usar números? "),
    ("simbolos_especiais", "Deseja usar caracteres especiais? ")
]

# 3. Interagir com o usuário para obter as configurações da senha
print("\nBem-vind@ ao Gerador de Senhas!")

# Solicita o tamanho da senha e valida se o valor é um número inteiro
try:
    comprimento_senha = int(input("Informe o tamanho que deseja para a senha: "))
    if comprimento_senha <= 0:
        print("\nERRO: O tamanho da senha deve ser um número maior que zero.")
        exit()
except ValueError:
    # Caso o valor não seja um número, exibe um erro e encerra o programa
    print("\nERRO: O valor informado não é um número válido.")
    exit()

# Pergunta ao usuário quais tipos de caracteres ele deseja incluir na senha
print("\nResponda com 's' para sim ou 'n' para não.")

# 4. Construir a base de caracteres com base nas escolhas do usuário
caracteres_escolhidos = ''

for chave, pergunta in opcoes_de_caracteres:
    if perguntar_sim_nao(pergunta):
        caracteres_escolhidos += caracteres[chave]

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