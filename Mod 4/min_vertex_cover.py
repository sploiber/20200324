import dimod

exactsolver = dimod.ExactSolver()

gamma = 4
linear = 3 - (3 * gamma)
quad = (2 * gamma) - 2

Q = {(1, 1): 1 - (2 * gamma), (2, 2): 1 - (2 * gamma), (1, 2): gamma, (1, 3): gamma, (2, 4): gamma, (3, 3): 1 - (3 * gamma), (3, 4): gamma, (3, 5): gamma, (4, 4):1 - (3 * gamma), (4, 5): gamma, (5, 5): 1 - (2 * gamma)}

results = exactsolver.sample_qubo(Q)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
