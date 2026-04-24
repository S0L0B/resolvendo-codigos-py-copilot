palavra = input("Digite uma palavra: ")

# Invertendo a palavra
invertida = palavra[::-1]

# Verificando se é palíndromo
if palavra == invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
