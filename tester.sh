#This part is used to check if all the combinations are OK or KO
#Use 'sh tester.sh results' in the terminal to retrieve results.txt file

results()
{
    l=$(($( cat test_values | wc -l | tr -d ' ' )))
    for ((i=1;i<=l;i++))
    do
        ./push_swap $(sed -n "$i"p test_values) | ./checker_Mac $(sed -n "$i"p test_values) | cat >> results.txt
    done
}

#This part is used to check the number of moves your program used to sort the numbers
#Use 'sh tester.sh moves' in the terminal to retrieve moves.txt file

moves()
{
    l=$(($( cat test_values | wc -l | tr -d ' ' )))
    for ((i=1;i<=l;i++))
    do
        ./push_swap $(sed -n "$i"p test_values) | wc -l | tr -d ' ' | cat >> moves.txt
    done 
}

if [ "$1" == "results" ]
then
	rm -rf results.txt
	sh combination.sh $2 | cat > test_values
    results
elif [ "$1" == "moves" ]
then
	rm -rf moves.txt
	sh combination.sh $2 | cat > test_values
    moves
elif [ "$1" == "average" ]
then
	rm -rf test_values
	sh combination.sh $2 | cat > test_values
	moves
	lines=$( cat moves.txt | wc -l )
	average=$( awk '{s+=$1} END {print s}' moves.txt )
	result=$((average))/$((lines))
	printf $((result))
	rm -rf moves.txt
	rm -rf test_values
elif [ "$1" == "remove" ]
then
	rm -rf test_values
	rm -rf moves.txt
	rm -rf results.txt
else
    echo "Please use a correct format. Use the GitHub docs"
fi
