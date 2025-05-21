def funcao_python(runner,code,palavra,numero):
    vogais = "AEIOUaeiou"
    contador_vogais = 0

    print(f"Os valores dessa função são: {runner} e {code}")
    if runner == True:
        print("O valor é verdadeiro")



    else:
        print("O valor dele é falso")



    while runner < 10:
        print(f"Aumentando o contador... {runner}")
        runner += 1



    if code <= 60:
        print(f"Você precisa de mais código porque o valor {code} não satisfaz as condições.")



    else:
        print(f"O valor {code} satisfaz as condições de código")



    for letra in  palavra:
        if letra in vogais:
            contador_vogais += 1

    quantidade_algarismos = len(str(numero)) # Aqui transformamos o valor atribuido para numero em uma string e utilizamos o "len" para contar quantos caracteres possui nessa string
    print(f"O seu numero possui {quantidade_algarismos} algarismos")

    print(f"Essa palavra possui {contador_vogais} vogais")

    if code % 2 == 1:
        print("O valor fornecido é ímpar")


    else:
        print("O valor fornecido é par")



    if palavra.isupper():
        print(f"A palavra {palavra} está com letras maiúsculas.")


    elif palavra.islower():
        print(f"A palavra {palavra} está com letras minúsculas.")


    else:
        print(f"A palavra {palavra} está com letras maiúsculas e minúsculas")



    palavra_invertida = palavra[::-1]

    print(f"A palavra {palavra} invertida é: {palavra_invertida}")

    tamanho = len(palavra)

    if tamanho <= 3:
        print("A palavra é curta")


    elif tamanho > 3 and tamanho < 8:
        print("A palavra é média")

    elif tamanho > 8:
        print("A palavra é grande")




funcao_python(1,70,"Robertoooooo",2020202020)
