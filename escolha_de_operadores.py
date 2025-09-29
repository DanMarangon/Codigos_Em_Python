def soma(numero1,numero2):
    print(numero1 + numero2)

def divisao(numero1,numero2):
    print(numero1 / numero2)

def subtracao(numero1,numero2):
    print(numero1 - numero2)

def multiplicacao(numero1,numero2):
    print(numero1 * numero2)

def main():
    valor1 = float(input("Digite o valor 1: "))
    valor2 = float(input("Digite o valor 2: "))
    operador = input("Digite o operador: (+),(-),(*),(/): ")
    if operador == '+':
        soma(valor1,valor2)

    elif operador == '-':
        subtracao(valor1,valor2)

    elif operador == '*':
        multiplicacao(valor1,valor2)

    elif operador == '/':
        divisao(valor1,valor2)

    else:
        print("Você não digitou nenhum dos operadores disponíveis.")


if __name__ == '__main__':
    main()
