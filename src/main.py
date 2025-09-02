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
