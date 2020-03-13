from dwave.system import DWaveSampler
from dwave.system.composites import FixedEmbeddingComposite
from minorminer import find_embedding
import dimod
import math
import sys

N = int(sys.argv[1])
chainstrength = 40
numruns = 1000

# Ising model is x_i x_j
h = {}
J = {(i, j): 1 for i in range(N) for j in range(i + 1, N)}

bqm = dimod.BinaryQuadraticModel.from_ising(h, J)

# Do the embedding
dwave_sampler = DWaveSampler()
A = dwave_sampler.edgelist
embedding = find_embedding(J, A)

sampler = FixedEmbeddingComposite(DWaveSampler(), embedding)
response = sampler.sample(bqm, chain_strength=chainstrength, num_reads=1000)

for sample, energy, num, cbf in response.data(['sample', 'energy', 'num_occurrences', 'chain_break_fraction']):
    print(sample, energy, num, cbf)
