import dimod
import dwave.inspector
from dwave.system import DWaveSampler, EmbeddingComposite

Q = {('x', 'x'): 1, ('w', 'w'): 1, ('x', 'y'): -2, ('y', 'z'): 2, ('z', 'w'): -2}

chainstrength = 5
numruns = 1000

bqm = dimod.BinaryQuadraticModel.from_qubo(Q)
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, chain_strength=chainstrength, num_reads=numruns)
dwave.inspector.show(bqm, sampleset, sampler)
