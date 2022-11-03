import os
import math
import subprocess

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94;1m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91;1m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def swap(elmt, i, j):
    elmt[i], elmt[j] = elmt[j], elmt[i]

def generate_permutations(a):
    n = len(a)
    c = [0]*n
    A = list(a)
    yield A
    i = 1
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                temp = A[0]
                A[0] = A[i]
                A[i] = temp
            else:
                temp = A[c[i]]
                A[c[i]] = A[i]
                A[i] = temp
            yield A
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1

def permutations(elements):
    yield from generate_permutations(elements)

def calculate_all(nb):
	elmt = [x for x in range(1, nb + 1)]
	all_moves = []
	max_moves = [0, ""]
	for perm in permutations(elmt):
		cmd = None
		moves_cmd = ' '.join([str(x) for x in perm])
		# check max moves
		moves_cmd = "./push_swap " + moves_cmd + " | wc -l"
		moves_output = int(os.popen(moves_cmd).read())
		print(moves_cmd)
		print("." + str(moves_output) + ".")
		if (moves_output > max_moves[0]):
			max_moves[0] = moves_output
			max_moves[1] = moves_cmd
	print(color.BOLD + "👉 MAX = " + str(max_moves[0]), end = '')
	limit = 3 if nb == 3 else 12 if nb == 5 else math.inf
	if (max_moves[0] > limit):
		print(color.BOLD + "\t❌ Too Much Moves: " + max_moves[1])
	else:
		print(color.BOLD + "\t✅ OK")

if __name__ == "__main__":
	print(color.RED + "\n** Welcome to push_swap tester for small stacks **\n" + color.END)
	# print(color.BOLD + ">> Testing all combinations for 3 numbers <<" + color.END)
	# calculate_all(3)
	print()
	print(color.BOLD + ">> Testing all combinations for 5 numbers <<" + color.END)
	calculate_all(5)
