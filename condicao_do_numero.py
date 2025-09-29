def positivo_negativo_neutro(numero):
    if numero > 0:
        print("Valor Positivo")



    elif numero == 0:
        print("Valor nulo")



    elif numero < 0:
        print("Valor negativo")


def main():
    valor = float(input("Digite o valor: "))

    positivo_negativo_neutro(valor)




if __name__ == '__main__':
    main()
