import random
import sys

moves = ['U1', "U3", 'U2', 'R1', "R3", 'R2', 'F1', "F3", 'F2', 'D1', "D3", 'D2', 'L1', "L3", 'L2', 'B1', "B3", 'B2']

n_moves = int(sys.argv[1])

for lp in range(1000000):
   scramble_moves = random.choices(moves, k=n_moves)
   print( ' '.join(map(str, scramble_moves)))
