import dimod

# Three qubits - and we want to penalize states greater than 1

exactsolver = dimod.ExactSolver()

Q = {(0, 1): 1, (0, 2): 1, (1, 2): 1}

results = exactsolver.sample_qubo(Q)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
