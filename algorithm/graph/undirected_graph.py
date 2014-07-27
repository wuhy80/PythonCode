import pprint

class Graph:
	def __init__(self, v):
		""" create a V-vertex graph with no edges """
		self.v = v
		self.e = 0
		self.adj = [] * v
		pp = pprint.PrettyPrinter(indent=4)

		pp.pprint(self)
		#for v in range(v):
		#	self.adj[v] = []

	def V():
		""" number of vertices"""
		self.v

	def E():
		""" number of edges"""
		self.e

	def addEdge(self, v, w):
		""" add edge v-w to this graph """
		print(self.adj[v])
		self.adj[v] << w
		self.adj[w] << v
		self.e = self.e + 1

	def adj(self, v):
		self.adj[v]

	def degree(self, g, v):
		degree = 0
		for w in g.adj(v):
			degree = degree + 1
		return degree

	def maxDegree(self, g):
		maxD = 0
		for v in range(g.V()):
			if self.degree(g, v) > maxD:
				maxD = self.degree(g, v)

		return maxD

	def avgDegress(self, g):
		return 2 * g.E() / g.V()

	def numOfSelfLoops(self, g):
		count = 0
		for v in range(g.V()):
			for w in g.adj(v):
				if v == w:
					count = count + 1
		return count / 2

	def to_s(self):
		s = V() + " vertices, " + E() + " edges\n"
		for v in range(V()):
			s += v + ": "
			for w in self.adj(v):
				s += w + " "
			s += "\n"
		return s



g = Graph(100)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(3, 4)

print(g.to_s)