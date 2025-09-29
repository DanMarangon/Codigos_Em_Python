from traceback import print_tb


def soma(a,b):
    return a + b

def subtração(a,b):
    return a - b

def main():
    valor1 = float(input("Digite o valor 1: "))
    valor2 = float(input("Digite o valor 2: "))
    valor3 = float(input("Digite o valor 3: "))
    valor4 = float(input("Digite o valor 4: "))

    escolha = (input("Digite + para somar e - para subtrair: "))
    if escolha == "+":
        resultadofinal = soma(valor1,valor2) + soma(valor3,valor4)
        print(resultadofinal)

    elif escolha == "-":
        resultado_final = subtração(valor1,valor2) - subtração(valor3,valor4)
        print(resultado_final)

    else:
        print("O número que você digitou não corresponde á nenhum tipo de escolha de operação.")


if __name__ == '__main__':
    main()
