import dimod
from dimod import BinaryQuadraticModel
import numpy as np
from dwave.system import LeapHybridSampler
import sys

N = int(sys.argv[1])

# Ising model x_i x_j
h = {}
J = {(i, j): 1 for i in range(N) for j in range(i + 1, N)}

bqm = dimod.BinaryQuadraticModel.from_ising(h, J)

sampler = LeapHybridSampler()
sampleset = sampler.sample(bqm, time_limit=15)
print(sampleset.info)
print("Found solution at energy {}.".format(
    sampleset.first.energy))
print(len(sampleset.record[0][0]))
