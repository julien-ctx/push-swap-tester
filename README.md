# Push_Swap Sorting Tester | For small stacks

## What is the purpose of this script?

This little Python script allows you to check how your program sorts **all the combinations** of small stacks. It is very convenient to be sure you meet the moves requirements for **3 and 5 numbers** as they are tested during the correction.

**Example:**

You want to know if your algorithm sorts correctly ***5 different numbers***.
There are 5! = 120 different combinations between five numbers, and checking it by yourself would be a waste of time!

That's why this script checks:

- for all the combinations of 3, 4 and 5 numbers, if the checker provided by 42 school returns OK or KO.
- for all the combinations of 3, 4 and 5 numbers, if the number of moves used to sort the combination is greater than the subject requirements.

## How to install the script?
- ***For Mac***:

`git clone https://github.com/julien-ctx/push_swap_tester.git && mv push_swap_tester/tester.py . && mv push_swap_tester/checker_Mac . && rm -rf push_swap_tester && chmod 777 checker_Mac && make && python3 tester.py`

- ***For Linux***:

`git clone https://github.com/julien-ctx/push_swap_tester.git && mv push_swap_tester/tester.py . && mv push_swap_tester/checker_linux . && rm -rf push_swap_tester && chmod 777 checker_linux && make && python3 tester.py`

## How to use the script?

Atfer installation, all you have to do is execute the Python script at the root of your repository using: `python3 tester.py`
If the script detects errors (too much moves or KO), a **results.txt** file is created to help you understand your mistakes.
