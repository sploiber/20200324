import numpy as np
import dimod
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Boxes problem with gamma = 36
Q = {(1, 1): -91, (2, 2): -87, (3, 3): -89, (1, 2): 72, (1, 3): 72, (2, 3): 72}


exactsolver = dimod.ExactSolver()

bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=144)

results = exactsolver.sample(bqm)

# First, print the results, showing the sums - this helps confirm the QUBO
# is correct
for sample, energy in results.data(['sample', 'energy']):
    print(sample, energy)

(h, J, ising_offset) = bqm.to_ising()
print(h)
print(J)
print(ising_offset)

chainstrength = 1
numruns = 1000
sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
response = sampler.sample(bqm, chain_strength=chainstrength, num_reads=numruns)
for sample, energy, num, cbf in response.data(['sample', 'energy', 'num_occurrences', 'chain_break_fraction']):
    print(sample, energy, num, cbf)
