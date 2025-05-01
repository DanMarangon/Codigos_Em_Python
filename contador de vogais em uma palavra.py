def conta_vogais(texto):
    Vogais = "AeIoUuOiea"
    contador = 0

    for char in texto:
        if char in Vogais:
            contador += 1

    return contador

texto = input()

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")