# Push_Swap Algorithm Sorting Checker

## What is the purpose of this script?

This little bash script allows you to check how your program sort all the combinations of a number.

**Example:**

You are trying to check if your algorithm sort correctly ***5 different numbers***.
There are 5! = 120 different combinations between five numbers, and checking it by yourself would be a waste of time.

That's why this script will check:

- for all the combinations, if the checker provided by 42 school returns OK or KO.
- for all the combinations, the number of moves used to sort the combination.

## Requirements

You have to put the checker at the root of your repository. It should be called **checker_Mac** or **checker_linux**. If you use the Linux checker, please change all occurrences of 'Mac' inside the tester.sh.

## How to use the script?

```
1/ git clone git@github.com:julien-ctx/push_swap_tool.git && mv push_swap_tool/tester.sh . && rm -rf push_swap_tool
```
```
2/ Go to https://www.dcode.fr/generateur-permutations and enter your number (if you enter 5, you'll get all the combinations of 5 numbers)
```
```
3/ Copy all the combinations and paste them inside a file called **test_values** inside your repository
```
```
4/ Use 'cat test_values | wc -l' to check the number of combinations
```
```
5/ Replace YOUR_NUMBER by the number of combinations
```
```
6/ Use 'sh tester.sh results' to see if your program sorted the numbers, or 'sh tester.sh moves' to see the number of moves
```
```
7/ Check the the **results.txt** and/or the **moves.txt** files
