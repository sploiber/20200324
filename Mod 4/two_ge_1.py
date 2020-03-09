import dimod

# Two qubits - and we want to penalize states less than 1

exactsolver = dimod.ExactSolver()

Q = {(0, 0): -1, (1, 1): -1, (0, 1): 2}

results = exactsolver.sample_qubo(Q)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
