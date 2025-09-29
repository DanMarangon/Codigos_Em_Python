numero1 = int(input("Digite o número de início: "))
numero2 = int(input("Digite o número final: "))
contador = 0
somador = 0
print("Número naturais na vertical:")



for i in range(numero1,numero2+1,1):
    print(i)
    contador = contador + 1
    somador = somador + i


print(f"Quantidade: {contador}")
print(f"Soma total: {somador}")
