#Use https://www.dcode.fr/generateur-permutations to retrieve all the combinations
#Put them in a file called test_values, separated by a \n
#Change 120 in results() and moves() by the number of lines in test_values

#This part is used to check if all the combinations are OK or KO
#Use 'sh tester.sh 1' in the terminal to retrieve results.txt file

results()
{
    for i in {1..120}
    do
        ./push_swap $(sed -n "$i"p test_values) | ./checker_Mac $(sed -n "$i"p test_values) | cat >> results.txt
    done
}

#This part is used to check the number of moves your program used to sort the numbers
#Use 'sh tester.sh 2' in the terminal to retrieve moves.txt file

moves()
{
    for i in {1..120}
    do
        ./push_swap $(sed -n "$i"p test_values) | wc -l | cat >> moves.txt
    done 
}

if [ "$#" -ne 1 ]
then
    echo "Please use a correct format: 'sh tester.sh results' or 'sh tester.sh moves'\n"
    exit 1
fi

if (($1 == 1))
then
    results
elif (($1 == 2))
then
    moves
else
    echo "Please use a correct format: 'sh tester.sh results' or 'sh tester.sh moves'\n"
fi
