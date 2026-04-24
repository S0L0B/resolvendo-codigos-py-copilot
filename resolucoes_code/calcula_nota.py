def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            
            # Validação (0 a 10, padrão mais comum)
            if 0 <= nota <= 10:
                return nota
            else:
                print("Digite uma nota entre 0 e 10.")
        
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Entrada de dados
nota1 = ler_nota("Digite a primeira nota: ")
nota2 = ler_nota("Digite a segunda nota: ")
nota3 = ler_nota("Digite a terceira nota: ")

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Resultado
print(f"\nMédia final: {media:.2f}")

# Classificação
if media >= 7:
    print("Status: Aprovado ✅")
elif media >= 5:
    print("Status: Recuperação ⚠️")
else:
    print("Status: Reprovado ❌")
