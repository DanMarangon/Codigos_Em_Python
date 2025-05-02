def antecessor_e_sucessor(numero): # Puxa o antecessor e o sucesso do número fornecido.
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print (antecessor_e_sucessor(10))

def calcular_total(numeros): # Soma todos os valores atribuídos para "numeros".
    return sum(numeros)

print(calcular_total([10,20,30]))

print(antecessor_e_sucessor(200))
