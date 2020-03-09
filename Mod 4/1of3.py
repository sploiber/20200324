import dimod

exactsolver = dimod.ExactSolver()

# Set up the QUBO. Start with the equations from the slides:
# - red - green - blue + 2 * red * green + 2 * red * blue + 2 * blue * green
Q = {('red', 'red'): -1, ('green', 'green'): -1, ('blue', 'blue'): -1, ('red', 'green'): 2, ('green', 'blue'): 2, ('red', 'blue'): 2}

results = exactsolver.sample_qubo(Q)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
