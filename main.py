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
    
    def ordenar(self, c1, c2):
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

    def mostrar_solucao(self):
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
                conjunto.ordenar(x,y)

print("\nExemplo do slide: ")

grafo = Grafo(9)
grafo.add_vertice("A")
grafo.add_vertice("B")
grafo.add_vertice("C")
grafo.add_vertice("D")
grafo.add_vertice("E")
grafo.add_vertice("F")
grafo.add_vertice("G")
grafo.add_vertice("H")
grafo.add_vertice("I")
grafo.add_aresta("A", "B", 4)
grafo.add_aresta("A", "H", 8)
grafo.add_aresta("B", "A", 4)
grafo.add_aresta("B", "H", 11)
grafo.add_aresta("B", "C", 8)
grafo.add_aresta("C", "B", 8)
grafo.add_aresta("C", "D", 7)
grafo.add_aresta("C", "I", 2)
grafo.add_aresta("C", "F", 4)
grafo.add_aresta("D", "C", 7)
grafo.add_aresta("D", "E", 9)
grafo.add_aresta("D", "F", 14)
grafo.add_aresta("E", "D", 9)
grafo.add_aresta("E", "F", 10)
grafo.add_aresta("F", "D", 14)
grafo.add_aresta("F", "E", 10)
grafo.add_aresta("F", "C", 4)
grafo.add_aresta("F", "G", 2)
grafo.add_aresta("G", "F", 2)
grafo.add_aresta("G", "I", 6)
grafo.add_aresta("G", "H", 1)
grafo.add_aresta("I", "C", 2)
grafo.add_aresta("I", "G", 6)
grafo.add_aresta("I", "H", 7)
grafo.add_aresta("H", "A", 8)
grafo.add_aresta("H", "B", 11)
grafo.add_aresta("H", "I", 7)
grafo.add_aresta("H", "G", 1)
grafo.kruskal()
grafo.mostrar_solucao()

#Exercicio

print("\nExercicio: ")
grafo = None
grafo = Grafo(8)
grafo.add_vertice("A")
grafo.add_vertice("B")
grafo.add_vertice("C")
grafo.add_vertice("D")
grafo.add_vertice("E")
grafo.add_vertice("F")
grafo.add_vertice("G")
grafo.add_vertice("H")

grafo.add_aresta("A", "B", 3)
grafo.add_aresta("A", "C", 5)
grafo.add_aresta("A", "D", 2)
grafo.add_aresta("A", "H", 10)

grafo.add_aresta("B", "A", 3)
grafo.add_aresta("B", "C", 5)
grafo.add_aresta("B", "D", 8)
grafo.add_aresta("B", "E", 4)
grafo.add_aresta("B", "G", 6)
grafo.add_aresta("B", "H", 6)

grafo.add_aresta("C", "A", 5)
grafo.add_aresta("C", "B", 5)
grafo.add_aresta("C", "E", 1)
grafo.add_aresta("C", "F", 7)
grafo.add_aresta("C", "G", 9)

grafo.add_aresta("D", "A", 2)
grafo.add_aresta("D", "B", 8)
grafo.add_aresta("D", "E", 12)
grafo.add_aresta("D", "H", 14)

grafo.add_aresta("E", "B", 4)
grafo.add_aresta("E", "C", 1)
grafo.add_aresta("E", "D", 12)
grafo.add_aresta("E", "G", 15)

grafo.add_aresta("F", "C", 7)
grafo.add_aresta("F", "H", 9)

grafo.add_aresta("G", "B", 6)
grafo.add_aresta("G", "C", 9)
grafo.add_aresta("G", "E", 15)
grafo.add_aresta("G", "H", 3)

grafo.add_aresta("H", "A", 10)
grafo.add_aresta("H", "B", 6)
grafo.add_aresta("H", "D", 14)
grafo.add_aresta("H", "F", 9)
grafo.add_aresta("H", "H", 3)

grafo.kruskal()
grafo.mostrar_solucao()

print("\nImplementação: ")
grafo = None

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
grafo.mostrar_solucao()
