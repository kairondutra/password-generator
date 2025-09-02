# 🔐 Gerador de Senhas em Python

Um simples gerador de senhas desenvolvido com Python.
Permite criar senhas personalizadas, escolhendo o comprimento e os tipos de caracteres (maiúsculas, minúsculas, números e símbolos).

## Como usar

1. Execute o arquivo `main.py`:
   ```
   python src/main.py
   ```

2. Siga as instruções no terminal:
   - Informe o tamanho desejado para a senha (apenas números inteiros maiores que zero).
   - Escolha os tipos de caracteres que deseja incluir, respondendo com `s` (sim) ou `n` (não) para:
     - Letras minúsculas
     - Letras maiúsculas
     - Números
     - Caracteres especiais

3. O programa irá gerar e exibir uma senha conforme suas escolhas.

## Exemplo de uso

```
Bem-vind@ ao Gerador de Senhas!
Informe o tamanho que deseja para a senha: 12

Responda com 's' para sim ou 'n' para não.
Deseja usar letras minúsculas? s
Deseja usar letras maiúsculas? s
Deseja usar números? s
Deseja usar caracteres especiais? n
----------------------------------------
Senha Gerada: aB3dE9fG2hJk
```

## Requisitos

- Python 3.x

## Observações

- O programa valida as entradas e só gera a senha se pelo menos um tipo de caractere for escolhido.
- Para sair, basta pressionar `Ctrl+C` ou informar um valor inválido para o tamanho da senha.

## Futuras mudanças

- Interface gráfica (GUI) para facilitar o uso.
- Opção de salvar senhas geradas em arquivo.
- Adicionar avaliação de força da senha.
- Permitir copiar a senha gerada automaticamente para a área de transferência.
- Suporte para outros idiomas.