saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    print("Saque sendo realizado.")

if saldo < saque:
    print("Você não possui saldo suficiente para o saque.")
    