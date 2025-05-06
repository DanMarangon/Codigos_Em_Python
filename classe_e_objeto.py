class bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("PlimPlim...")

    def parar(self):
        print ("Parando a bicicleta...")
        print ("Bicicleta parada.")

    def correr(self):
        print("Bicicleta acelerando...")






caloi = bicicleta("Vermelha","caloi",2022,600)


caloi.correr()
caloi.parar()
caloi.buzinar()

print(caloi.cor,caloi.modelo,caloi.ano,caloi.valor) # Exibe os valores adicionados a bicileta "caloi"


caloi2 = bicicleta("Verde","Monark",2000,189)

bicicleta.buzinar(caloi2) # posso chamar a classe dessa forma
caloi2.parar() # ou dessa forma


