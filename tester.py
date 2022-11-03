import os
import math
import subprocess
import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96;1m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94;1m'
   GREEN = '\033[92;1m'
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

def calculate_combination(nb):
	elmt = [x for x in range(1, nb + 1)]
	max_moves = 0
	all_moves = []
	all_res = []
	for perm in permutations(elmt):
		cmd = ' '.join([str(x) for x in perm])

		# check max moves
		moves_cmd = "./push_swap " + cmd + " | wc -l"
		moves_output = int(os.popen(moves_cmd).read())
		if (moves_output > max_moves):
			max_moves = moves_output
		all_moves.append((int(moves_output), str(cmd)))

		# check results
		res_cmd = "./push_swap " + cmd + " | ./checker_Mac " + cmd
		res_output = os.popen(res_cmd).read()
		all_res.append((str(res_output), str(cmd)))

	# print max moves
	limit = 3 if nb == 3 else 12 if nb == 5 else math.inf
	if limit == 3:
		all_too_much = [("./push_swap " + item[1] + " | wc -l") for item in all_moves if item[0] > 3]
	elif limit == 12:
		all_too_much = [("./push_swap " + item[1] + " | wc -l") for item in all_moves if item[0] > 12]
	else:
		all_too_much = None
	all_wrong_values = [("./push_swap " + item[1] + " | ./checker_Mac " + item[1]) for item in all_res if item[0] == "KO\n"]
	print(color.BOLD + "👉 MAX = " + str(max_moves), end = '')
	if (max_moves > limit):
		print(color.BOLD + "\t❌ Too Much Moves")
	else:
		print(color.BOLD + "\t✅ OK")

	# print results
	state = True
	for x in all_res:
		if x[0] == "KO\n":
			print(color.BOLD + "👉 RESULTS\t" + "❌ KO")
			state = False
			break
	if state:
		print(color.BOLD + "👉 RESULTS\t" + "✅ OK" + color.END)
	if all_too_much:
		f = open('results.txt', 'a+')
		if limit == 3:
			f.write("** TOO MUCH MOVES FOR THESE TESTS (MAX = 3) **\n\n")
		elif limit == 12:
			f.write("** TOO MUCH MOVES FOR THESE TESTS (MAX = 12) **\n\n")
		for item in all_too_much:
			f.write(item + "\n\n")
		f.write("\n")
		f.close()
	if all_wrong_values:
		f = open('results.txt', 'a+')
		f.write("** KO ON THESE TESTS **\n\n")
		for item in all_wrong_values:
			f.write(item + "\n\n")
		f.close()

def mean(lst):
    return round(sum(lst) / len(lst))

def calculate(nb):
	moves = []
	min_moves = math.inf
	max_moves = 0
	wrong_values = []
	for x in range(0, 10):
		nbs = ' '.join([str(random.randint(-2147483648, 2147483647)) for x in range(0, nb)])
		res_cmd = "./push_swap " + nbs + " | ./checker_Mac " + nbs	
		res_output = os.popen(res_cmd).read()
		if res_output == "KO\n":
			print(color.BOLD + f"TEST {x + 1} 👉 \t❌ KO")
			wrong_values.append(("./push_swap " + nbs + " | ./checker_Mac " + nbs))
		else:
			print(color.BOLD + f"TEST {x + 1} 👉 \t✅ OK")
		moves_cmd = "./push_swap " + nbs + " | wc -l"
		moves_output = os.popen(moves_cmd).read()	
		moves.append(int(moves_output))
		if int(moves_output) < min_moves:
			min_moves = int(moves_output)
		if int(moves_output) > max_moves:
			max_moves = int(moves_output)
	if wrong_values:
		f = open('results.txt', 'a+')
		f.write("** KO ON THESE TESTS **\n\n")
		for item in wrong_values:
			f.write(item + "\n\n")
		f.close()
	else:
		print(color.BOLD + "\nMEAN 👉\t" + str(round(mean(moves))) + " moves", end = '')
		print(color.RED + "\nMAX 👉\t" + str(max_moves) + " moves", end = '')
		print(color.GREEN + "\nMIN 👉\t" + str(min_moves) + " moves")



if __name__ == "__main__":
	os.system("rm -rf results.txt")
	print(color.CYAN + "\n** Welcome to push_swap tester by jcauchet **" + color.END)
	for i in range(3, 6):
		print(color.BLUE + f"\n>> Testing for all combinations of {i} numbers <<" + color.END)
		calculate_combination(i)
	print(color.BLUE + f"\n>> Testing 10 times for 100 numbers <<" + color.END)
	calculate(100)
	print(color.BLUE + f"\n>> Testing 10 times for 500 numbers <<" + color.END)
	calculate(500)
	if os.path.exists("results.txt"):
		print(color.RED + "\n-> You can find details of failed tests in results.txt file <-" + color.END)
	else:
		print(color.GREEN + "\n-> Congratulations! all the tests are OK! <-" + color.END)
	print()
