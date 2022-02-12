# Push_Swap Algorithm Sorting Checker

## What is the purpose of this script?

This little bash script allows you to check how your program sorts all the combinations of a number.

**Example:**

You are trying to check if your algorithm sort correctly ***5 different numbers***.
There are 5! = 120 different combinations between five numbers, and checking it by yourself would be a waste of time.

That's why this script will check:

- for all the combinations, if the checker provided by 42 school returns OK or KO.
- for all the combinations, the number of moves used to sort the combination.
- the average number of moves used by your algorithm to sort one combination.

## Requirements

You have to put the checker at the root of your repository. It should be called **checker_Mac** or **checker_linux**. If you use the Linux checker, please change all occurrences of 'Mac' inside the tester.sh.

## How to use the script?


1/ `git clone git@github.com:julien-ctx/push_swap_tool.git && mv push_swap_tool/tester.sh . && rm -rf push_swap_tool`

2/ Go to https://www.dcode.fr/generateur-permutations and enter your number (if you enter 5, you'll get all the combinations of 5 numbers)

3/ Copy all the combinations and paste them inside a file called **test_values** inside your repository

4/ Use `cat test_values | wc -l` to check the number of combinations

5/ Inside the script, replace **YOUR_NUMBER** by the number of combinations

6/ Use one of the following commands:
- `sh tester.sh results` : results of your algorithm (KO or OK) for all the combinations will be put into results.txt file
- `sh tester.sh moves`: number of moves used by your algorithm to sort all the different combinations will be put into moves.txt file
- `sh tester.sh average` : prints in the standard output the average number of moves your algorithm used to sort all the combinations of numbers.
- `sh tester.sh remove` : removes all the generated files, except test_values

7/ Check **results.txt** and/or **moves.txt** and refer to the line to see where your algorithm failed (or succeeded!)
