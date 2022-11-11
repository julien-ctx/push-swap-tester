import os, math, subprocess, random, sys

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96;1m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94;1m'
   GREEN = '\033[92;1m'
   YELLOW = '\033[93;1m'
   RED = '\033[91;1m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def swap(elmt, i, j):
    elmt[i], elmt[j] = elmt[j], elmt[i]

def generate_permutations(a):
    n = len(a)
    c = [0] * n
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
	limit = 3 if nb == 3 else 12 if nb == 5 else math.inf
	for perm in permutations(elmt):
		cmd = ' '.join([str(x) for x in perm])

		moves_cmd = "./push_swap " + cmd + " | wc -l"
		moves_output = int(os.popen(moves_cmd).read())
		if (moves_output > max_moves):
			max_moves = moves_output
		all_moves.append((int(moves_output), str(cmd)))

		res_cmd = "./push_swap " + cmd + " | ./checker_Mac " + cmd
		res_output = os.popen(res_cmd).read()
		all_res.append((str(res_output), str(cmd)))

	# Printing max moves and results
	print(color.BOLD + "👉 MAX = " + str(max_moves) + color.END, end = '')
	if (max_moves > limit):
		print(color.RED + "\t❌ Too Much Moves" + color.END)
	else:
		print(color.GREEN + "\t✅ OK" + color.END)
	state = True
	for x in all_res:
		if x[0] == "KO\n":
			print(color.BOLD + "👉 RESULTS\t" + "❌ " + color.RED + "KO" + color.END)
			state = False
			break
	if state:
		print(color.BOLD + "👉 RESULTS\t" + "✅ " + color.GREEN + "OK" + color.END)

	# Printing trace
	if limit == 3:
		all_too_much = [("./push_swap " + item[1] + " | wc -l") for item in all_moves if item[0] > 3]
	elif limit == 12:
		all_too_much = [("./push_swap " + item[1] + " | wc -l") for item in all_moves if item[0] > 12]
	else:
		all_too_much = None
	all_wrong_values = [("./push_swap " + item[1] + " | ./checker_Mac " + item[1]) for item in all_res if item[0] == "KO\n"]
	if all_too_much:
		f = open('trace.txt', 'a+')
		if limit == 3:
			f.write("** TOO MUCH MOVES FOR THESE TESTS (MAX = 3) **\n\n")
		elif limit == 12:
			f.write("** TOO MUCH MOVES FOR THESE TESTS (MAX = 12) **\n\n")
		for item in all_too_much:
			f.write(item + "\n\n")
		f.write("\n")
		f.close()
	if all_wrong_values:
		f = open('trace.txt', 'a+')
		f.write("** KO ON THESE TESTS **\n\n")
		for item in all_wrong_values:
			f.write(item + "\n\n")
		f.close()

def mean(lst):
    return round(sum(lst) / len(lst))

def calculate(nb):
	moves = []
	wrong_values = []
	for x in range(0, 10):
		nbs = ' '.join([str(random.randint(-2147483648, 2147483647)) for x in range(0, nb)])

		res_cmd = "./push_swap " + nbs + " | ./checker_Mac " + nbs	
		res_output = os.popen(res_cmd).read()
		if res_output == "KO\n":
			print(color.BOLD + f"TEST {x + 1} 👉 \t❌ " + color.RED + "KO" + color.END)
			wrong_values.append(("./push_swap " + nbs + " | ./checker_Mac " + nbs))
		else:
			print(color.BOLD + f"TEST {x + 1} 👉 \t✅ " + color.GREEN + "OK" + color.END)
		
		moves_cmd = "./push_swap " + nbs + " | wc -l"
		moves_output = os.popen(moves_cmd).read()	
		moves.append(int(moves_output))

	if wrong_values:
		f = open('trace.txt', 'a+')
		f.write("** KO ON THESE TESTS **\n\n")
		for item in wrong_values:
			f.write(item + "\n\n")
		f.close()
	else:
		print(color.BOLD + "\nMEAN 👉\t" + str(round(mean(moves))) + " moves" + color.END, end = '')
		print(color.RED + "\nMAX 👉\t" + str(max(moves)) + " moves" + color.END, end = '')
		print(color.GREEN + "\nMIN 👉\t" + str(min(moves)) + " moves" + color.END)

def parsing_error():
	print(color.RED + "❌ KO" + color.END)
	with open("trace.txt", "w") as f:
		f.write("** PARSING ERRORS DETECTED, PLEASE REFER TO THE TESTS **\n\n")

def parsing_check():
	res = os.popen("./push_swap").read()
	ret_code = subprocess.run(["./push_swap"]).returncode
	print(color.BOLD + "./push_swap\t\t\t\t" + color.END, end = '')
	if res or ret_code == -11:
		parsing_error()
	else:
		print(color.GREEN + "✅ OK" + color.END)

	print(color.BOLD + './push_swap ""\t\t\t\t' + color.END, end = '')
	res = subprocess.run(["./push_swap", ""], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	ret_code = res.returncode
	if ret_code != -11 and ("Error" in str(res.stderr) or str(res.stdout) == "b''"):
		print(color.GREEN + "✅ OK" + color.END)
	elif "Error" in str(res.stdout) and ret_code != -11:
		print(color.YELLOW + "❗️ Errors must be displayed on stderr" + color.END)
	else:
		parsing_error()

	res = subprocess.run(['./push_swap', '3 2 -'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	print(color.BOLD + './push_swap "3 2 -"\t\t\t' + color.END, end = '')
	if "Error" in str(res.stdout):
		print(color.YELLOW + "❗️ Errors must be displayed on stderr" + color.END)
	elif "Error" in str(res.stderr):
		print(color.GREEN + "✅ OK" + color.END)
	else:
		parsing_error()

	res = subprocess.run(['./push_swap', '3', '+', '1'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	print(color.BOLD + './push_swap 3 + 1\t\t\t' + color.END, end = '')
	if "Error" in str(res.stdout):
		print(color.YELLOW + "❗️ Errors must be displayed on stderr" + color.END)
	elif "Error" in str(res.stderr):
		print(color.GREEN + "✅ OK" + color.END)
	else:
		parsing_error()
	
	res = os.popen('./push_swap 1 2 3').read()
	print(color.BOLD + './push_swap 1 2 3\t\t\t' + color.END, end = '')
	if res:
		parsing_error()
	else:
		print(color.GREEN + "✅ OK" + color.END)

	res = subprocess.run(['./push_swap', '3 2 1a'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	print(color.BOLD + './push_swap "3 2 1a"\t\t\t' + color.END, end = '')
	if "Error" in str(res.stdout):
		print(color.YELLOW + "❗️ Errors must be displayed on stderr" + color.END)
	elif "Error" in str(res.stderr):
		print(color.GREEN + "✅ OK" + color.END)
	else:
		parsing_error()

	res = subprocess.run(['./push_swap', '0 3 0'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	print(color.BOLD + './push_swap "0 3 0"\t\t\t' + color.END, end = '')
	if "Error" in str(res.stdout):
		print(color.YELLOW + "❗️ Errors must be displayed on stderr" + color.END)
	elif "Error" in str(res.stderr):
		print(color.GREEN + "✅ OK" + color.END)
	else:
		parsing_error()
	
	res = os.popen('./push_swap "2147483647 -2147483648"').read()
	print(color.BOLD + './push_swap "2147483647 -2147483648"\t' + color.END, end = '')
	if res != "sa\n" and res != "ra\n" and res != "rra\n":
		parsing_error()
	else:
		print(color.GREEN + "✅ OK" + color.END)	

if __name__ == "__main__":
	if os.path.exists("trace.txt"):
		os.system("rm -rf trace.txt")
	if not os.path.exists("push_swap"):
		os.system("make")
	if not os.path.exists("checker_Mac"):
		print(color.RED + "\nError: the tester needs checker_Mac at the root of the repository!\n" + color.END)
		exit(1)

	print(color.CYAN + "\n** Welcome to push_swap tester by jcauchet **" + color.END)

	print(color.BLUE + "\n>> Testing parsing <<" + color.END)
	parsing_check()

	for i in range(3, 6):
		print(color.BLUE + f"\n>> Testing for all combinations of {i} numbers <<" + color.END)
		calculate_combination(i)
	
	print(color.BLUE + f"\n>> Testing 10 times for 100 numbers <<" + color.END)
	calculate(100)

	print(color.BLUE + f"\n>> Testing 10 times for 500 numbers <<" + color.END)
	calculate(500)

	if os.path.exists("trace.txt"):
		print(color.RED + "\n-> You can find details of failed tests in trace.txt file <-" + color.END)
	else:
		print(color.GREEN + "\n-> Congratulations! all the tests are OK! <-" + color.END)
	print()
