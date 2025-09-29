numero = int(input("Digite o valor: "))
x = 0
contador = 0
soma = 0
while x <= numero:
    soma = soma + x
    print(x)
    x = x + 1
    contador = contador + 1



print(f"A operação do while foi realizada {contador} vezes")
print(f"A soma total é: {soma}")
