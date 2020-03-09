import dimod

exactsolver = dimod.ExactSolver()

# Set up the QUBO. Start with the equations from the slides:
# The graph needs to be split into 2 subsets - of the same size
# as few edges as possible between the subsets
# x0, x1, x2, x3 in a full mesh
# 0 3
# 1 2
# x0 if node 0 is in set A, and so on
# want to favor having x0 and x1 in the same set - lower energy if they
# are the same
# x0 + x1 - 2x0x1
# x0 + x2 - 2x0x2
# x0 + x3 - 2x0x3
# x1 + x2 - 2x1x2
# x1 + x3 - 2x1x3
# x2 + x3 - 2x2x3
# 3x0 + 3x1 + 3x2 + 3x3 - 2x0x1 - 2x0x2 - 2x0x3 - 2x1x2 - 2x1x3 - 2x2x3
# but then we also want the sum of x0 + x1 + x2 + x3 - 2 to be minimal
# 2x0x1 + 2x0x2 + 2x0x3 + 2x1x2 + 2x1x3 + 2x2x3 - 3x0 - 3x1 - 3x2 - 3x3 + 4
gamma = 1.5
linear = 3 - (3 * gamma)
quad = (2 * gamma) - 2

Q = {(0, 0): linear, (1, 1): linear, (2, 2): linear, (3, 3): linear, (0, 1): quad, (0, 2): quad, (0, 3): quad, (1, 2): quad, (1, 3): quad, (2, 3): quad}

results = exactsolver.sample_qubo(Q)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
