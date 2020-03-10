import dimod
from pyqubo import Constraint, Array

exactsolver = dimod.ExactSolver()

# Set up variables
x = Array.create('x', shape=5, vartype='BINARY')

# Set up the QUBO. Start with the equation insisting that there are 3
# numbers turned on, and then the equation insisting that they sum up to 8.
H = Constraint((sum(x) - 3) ** 2, label='3_hot')
H += Constraint((x[0] + (2 * x[1]) + (3 * x[2]) + (4 * x[3]) + (5 * x[4]) - 8) ** 2, label='8_sum')

# Compile the model, and turn it into a QUBO object
model = H.compile()
Q = model.to_qubo()
bqm = dimod.BinaryQuadraticModel.from_qubo(Q[0], offset=Q[1])

# solve the problem
results = exactsolver.sample(bqm)

# print the results
for sample, energy in results.data(['sample', 'energy']):
    _, broken, _ = model.decode_solution(sample, vartype='BINARY')
    if not broken:
        print(sample, energy)
