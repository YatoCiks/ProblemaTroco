troco = 40 # reais
moedas = [1, 2, 5, 10, 20]
quant_moedas = len(moedas)
troco_moedas = [[None for _ in range(troco+1)] for _ in moedas]


def mostrar_tabela():
    print("array troco x moedas: ")
    for i in troco_moedas:
        print(str(i))

def calcular_troco(troco_restante, indice_atual_moeda = 0):
    if troco_restante == 0:
        return 0

    if troco_restante > 0 and indice_atual_moeda == quant_moedas:
        return float("inf")

    if troco_restante < 0:
        return float("inf")

    if troco_moedas[indice_atual_moeda][troco_restante] == None:
        pegar_moeda = 1 + calcular_troco(troco_restante - moedas[indice_atual_moeda], indice_atual_moeda)
        nao_pegar = calcular_troco(troco_restante, indice_atual_moeda + 1)
        troco_moedas[indice_atual_moeda][troco_restante] = min(pegar_moeda, nao_pegar)
    return troco_moedas[indice_atual_moeda][troco_restante]


print("troco para "+str(troco)+" é "+str(calcular_troco(troco)))