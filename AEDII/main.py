class Nodo:
    def __init__(self, info):
        self.info = info   
        self.prox = None

class ListaEncadeada:
    def __init__(self):        
        self.inicio = None
        self.fim = None


    def inserir(self, info):
        ptAux = Nodo(info)
        if self.inicio == None:
            self.inicio = ptAux
            self.fim = ptAux
        else:
            self.fim.prox = ptAux
            self.fim = ptAux

            
    def imprimir(self):
        ponteiroAux = self.inicio
        while ponteiroAux != None:
            print(ponteiroAux.info)
            ponteiroAux = ponteiroAux.prox
              

    def consultar(self, info):
        ponteiroAux = self.inicio
        while ponteiroAux != None:
            ponteiroAux = ponteiroAux.prox

        return "Tem"




    def remover():
        pass


    def destruir():
        pass


lista = ListaEncadeada()
lista.inserir(1)
lista.inserir(6)
lista.inserir(4)
lista.inserir(2)
lista.imprimir()
lista.consultar(1)

