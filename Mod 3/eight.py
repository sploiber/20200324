import dimod

exactsolver = dimod.ExactSolver()

# Set up the QUBO. Start with the equation insisting that there are 3
# numbers turned on:
# (x1 + x2 + x3 + x4 + x5 - 3) ** 2
# Constant is 9

# (x1 + 2x2 + 3x3 + 4x4 + 5x5 - 8) ** 2
# Constant is 64
Q = {(1, 1): -20, (2, 2): -33, (3, 3): -44, (4, 4): -53, (5, 5): -60, (1, 2): 6, (1, 3): 8, (1, 4): 10, (1, 5): 12, (2, 3): 14, (2, 4): 18, (2, 5): 22, (3, 4): 26, (3, 5): 32, (4, 5): 42}

results = exactsolver.sample_qubo(Q)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
