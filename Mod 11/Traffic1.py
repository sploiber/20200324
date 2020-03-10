from dimod import BinaryQuadraticModel
from pyqubo import Constraint, Placeholder, Array
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Code for training demo on Traffic Flow
# 9/3/19 JMG

# Parameters
chainstrength = 70
numruns = 100

# Problem size
N_CARS = 2
N_ROUTES = 3

# Form the pyqubo binary variables representing (Car, Route)
q = Array.create('q', shape=(N_CARS, N_ROUTES), vartype='BINARY')

gamma = Placeholder('gamma')

# Constraints, one for each Car
H = 0
for i in range(N_CARS):
    H += gamma * Constraint((sum(q[i, j] for j in range(N_ROUTES)) - 1) ** 2, label=str(i))

# Cost functions
# Be sure to count them once for each segment
# s0 and s3
H += 2 * ((q[0, 0] + q[0, 1] + q[1, 0] + q[1, 1]) ** 2)
# s2 and s7 and s10
H += 3 * ((q[0, 2] + q[1, 2]) ** 2)
# s6 and s9
H += 2 * ((q[0, 0] + q[1, 0]) ** 2)
# s8
H += (q[0, 1] + q[1, 1]) ** 2
# s11
H += (q[0, 1] + q[0, 2] + q[1, 1] + q[1, 2]) ** 2

# Compile the model, and turn it into a QUBO object
model = H.compile()
Q = model.to_qubo(feed_dict={'gamma': 100})

# Turn the QUBO object into a BinaryQuadraticModel, using the computed
# offset
bqm = BinaryQuadraticModel.from_qubo(Q[0], offset=Q[1])

# Run the QUBO on the solver from your config file
response = EmbeddingComposite(DWaveSampler()).sample(bqm, chain_strength=chainstrength, num_reads=numruns)

# Write complete results to file
output = open('Traffic1_results.txt', 'w')
for smpl, energy in response.data(['sample', 'energy']):
    sol, broken, eny = model.decode_solution(smpl, feed_dict={'gamma': 100}, vartype='BINARY')
    if not broken:
        output.write(str(energy) + ' ' + str([node for node in smpl if smpl[node] > 0]) + '\n')
output.close()
