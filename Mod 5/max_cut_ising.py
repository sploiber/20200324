import dimod
import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

exactsolver = dimod.ExactSolver()

h = {}
J = {}
for node in G.nodes:
    h[node] = 0
for edge in G.edges:
    J[edge] = 0.5

results = exactsolver.sample_ising(h, J)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
