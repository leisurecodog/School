"""Script to test the Graph and UndirectedGraph classes"""

from graph import Graph, UndirectedGraph

print ("***Directed graph***")
g = Graph()
g.add_vertex('A')
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

print("\nVertices:", g.vertices())

g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('C', 'B')
g.add_edge('B', 'D')
g.add_edge('D', 'A')

print("\nEdges:")
g.print_edges()

print("\nA->B?", g.is_connected('A', 'B'))
print("B->A?", g.is_connected('B', 'A'))
print("C->D?", g.is_connected('C', 'D'))

print("\nPaths from A to D:")
g.print_paths('A', 'D')


print("\nRemoving B -> D ...")
g.remove_edge('B', 'D')
print("\nEdges:")
g.print_edges()

print("\nPaths from A to D:")
g.print_paths('A', 'D')




print("\n\n***Undirected graph***")
u = UndirectedGraph()
u.add_vertex('A')
u.add_vertex('A')
u.add_vertex('B')
u.add_vertex('C')

print("\nVertices:", u.vertices())

u.add_edge('A', 'B')
u.add_edge('B', 'C')
u.add_edge('C', 'D')
u.add_edge('C', 'B')
u.add_edge('B', 'D')
u.add_edge('D', 'A')

print("\nEdges:")
u.print_edges()

print("\nA <-> B?", u.is_connected('A', 'B'))
print("B <-> A?", u.is_connected('B', 'A'))
print("C <-> D?",u.is_connected('C', 'D'))

print("\nPaths from A to D: ")
u.print_paths('A', 'D')

print("\nRemoving C ...")
u.remove_vertex('C')

print("\nEdges:")
u.print_edges()

print("\nPaths from A to D: ")
u.print_paths('A', 'D')
