# Push_Swap Sorting Tester

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


1/ `git clone https://github.com/julien-ctx/push_swap_tool.git && mv push_swap_tool/tester.sh . && mv push_swap_tool/combination.sh . && rm -rf push_swap_tool` && chmod 777 tester.sh

2/ Use one of the following commands:

⚠️ ***You need to put the sequence of number as an argument in the following commands: for example, use `"1 2 3 4 5"` as an argument to check all combinations of 5 numbers. Replace the arguments in the following commands according to your needs*** ⚠️

- `sh tester.sh results "1 2 3 4 5"` : results of your algorithm (KO or OK) for all the combinations will be put into results.txt file
- `sh tester.sh moves "1 2 3 4 5"` : number of moves used by your algorithm to sort all the different combinations will be put into moves.txt file
- `sh tester.sh average "1 2 3 4 5"` : prints in the standard output the average number of moves your algorithm used to sort all the combinations of numbers.
- `sh tester.sh max "1 2 3 4 5"` : prints in the standard output the max number of move used in all the combinations.
- `sh tester.sh remove` : removes all the generated files

3/ Check **results.txt** and/or **moves.txt** and refer to the line to see where your algorithm failed (or succeeded!)
