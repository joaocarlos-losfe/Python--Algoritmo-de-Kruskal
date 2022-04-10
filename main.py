class Conjuntos:
    def __init__(self, vertices):
        self.numero_vertices = vertices
        self.parent = {}

        for v in vertices:
            self.parent[v] = v
        self.classificados = dict.fromkeys(vertices, 0)
    
    def buscar(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.buscar(self.parent[item])
    
    def unir_conjuntos(self, c1, c2):
        raiz1 = self.buscar(c1)
        raiz2 = self.buscar(c2)

        if self.classificados[raiz1] < self.classificados[raiz2]:
            self.parent[raiz1] = raiz2

        elif self.classificados[raiz1] > self.classificados[raiz2]:
            self.parent[raiz2] = raiz1

        else:
            self.parent[raiz2] = raiz1
            self.classificados[raiz1] += 1


class Grafo:
    def __init__(self, numero_de_vertices):
        self.numero_vertices = numero_de_vertices
        self.grafo = []
        self.nos = []

        self.AGM = [] #Arvore Geradora Minima

    def add_aresta(self, v1, v2, peso):
        self.grafo.append([v1, v2, peso])
    
    def add_vertice(self, vertice):
        self.nos.append(vertice)

    def mostrar_solucao(self,v1, v2, peso):
        for v1, v2, peso in self.AGM:
            print("%s - %s: %s" % (v1, v2, peso))
    
    def kruskal(self):
        i = 0 
        j = 0

        conjunto = Conjuntos(self.nos)
        self.grafo = sorted(self.grafo, key=lambda item: item[2]) #ordena o conjunto
        
        while j < self.numero_vertices - 1:

            v1, v2, peso = self.grafo[i]
            i += 1
            x = conjunto.buscar(v1)
            y = conjunto.buscar(v2)

            if x != y:
                j += 1
                self.AGM.append([v1,v2,peso])
                conjunto.unir_conjuntos(x,y)

        self.mostrar_solucao(v1,v2,peso)

grafo = Grafo(8)
grafo.add_vertice("A")
grafo.add_vertice("B")
grafo.add_vertice("C")
grafo.add_vertice("D")
grafo.add_vertice("E")
grafo.add_vertice("F")
grafo.add_vertice("G")
grafo.add_vertice("H")

grafo.add_aresta("A", "B", 240)
grafo.add_aresta("A", "C", 210)
grafo.add_aresta("A", "D", 340)
grafo.add_aresta("A", "E", 280)
grafo.add_aresta("A", "F", 200)
grafo.add_aresta("A", "G", 345)
grafo.add_aresta("A", "H", 120)

grafo.add_aresta("B", "C", 265)
grafo.add_aresta("B", "D", 175)
grafo.add_aresta("B", "E", 215)
grafo.add_aresta("B", "F", 180)
grafo.add_aresta("B", "G", 185)
grafo.add_aresta("B", "H", 155)

grafo.add_aresta("C", "D", 260)
grafo.add_aresta("C", "E", 115)
grafo.add_aresta("C", "F", 350)
grafo.add_aresta("C", "G", 435)
grafo.add_aresta("C", "H", 195)

grafo.add_aresta("D", "E", 160)
grafo.add_aresta("D", "F", 330)
grafo.add_aresta("D", "G", 295)
grafo.add_aresta("D", "H", 230)

grafo.add_aresta("E", "F", 360)
grafo.add_aresta("E", "G", 400)
grafo.add_aresta("E", "H", 170)

grafo.add_aresta("F", "G", 175)
grafo.add_aresta("F", "H", 205)

grafo.add_aresta("G", "H", 305)

grafo.kruskal()