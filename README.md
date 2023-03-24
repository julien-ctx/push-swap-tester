# Push_Swap Sorting Tester | 42

## What is the purpose of this script?

This little Python script allows you to know if **your program sorts correctly smalls and large stacks**.

**All features:**

- it checks a lot of different common parsing mistakes.
- for all the small stacks (3, 4 and 5 numbers), it checks if your program sorts correctly **all possible combinations of numbers**.
- for big stacks (100 and 500 numbers), it generates **10 random stacks** and checks if your program sorts them correctly.
- it displays how many moves your program used to sort the stack, as well as the average, max and min moves.

## How to install the script?
- ***For Mac***:

```
git clone git@github.com:julien-ctx/push-swap-tester.git && mv push-swap-tester/tester.py . && mv push-swap-tester/checker_Mac . && rm -rf push-swap-tester && chmod 777 checker_Mac && make && python3 tester.py
```

- ***For Linux***:

```
git clone git@github.com:julien-ctx/push-swap-tester.git && mv push-swap-tester/tester.py . && mv push-swap-tester/checker_linux . && rm -rf push-swap-tester && chmod 777 checker_linux && sed -i -- 's/checker_Mac/checker_linux/g' tester.py && make && python3 tester.py
```

## How to use the script?

Atfer installation, all you have to do is execute the Python script at the root of your repository using: `python3 tester.py`

If the script detects errors (too much moves or KO), a **trace.txt** file is created to help you understand your mistakes.
