#!/bin/bash 

_=$BASH_ARGC
OLDIFS=$IFS 

declare    arr=""
declare -i length=0

## Arg 1 - index 1: First swap index
## Arg 2 - index 2: Second swap index
function swap() { 
	local -a my_array 
	local    tmpval="" 
	local -i index1=${1} 
	local -i index2=${2}  
	OLDIFS=$IFS
	IFS=" " read -ra my_array <<< "${arr}"
	tmpval=${my_array[${index1}]}
	my_array[${index1}]=${my_array[${index2}]}
	my_array[${index2}]=${tmpval}
	IFS=$OLDIFS
	arr="${my_array[@]}"
}

## Arg1 - Integer: size
function heappermutation() { 
	local -i size=${1}
	local -i i=0
	if((${size}==1)); then  
		echo "${arr}"
		return
	fi 
	for((i=0;i<${size};i++)) { 
		heappermutation $((${size}-1)) 
		if(((${size}%2)==1)); then    
			swap 0 $((${size}-1))
		else 
			swap ${i} $((${size}-1))
		fi 
	} 
}

function init() { 
	arr="${BASH_ARGV[@]}"
	length=${BASH_ARGC}
}

function main() { 
	init 
	heappermutation ${length}
} 

if(($#<1))||[[ "${1}" =~ ^- ]]; then 
	cat<<EOF 

Usage: ${0##*/} <args=eg. 1 2 3 4 5>

 Eg. $> ${0##*/} 1 2 3 
		3 2 1
		2 3 1
		1 3 2
		3 1 2
		2 1 3
		1 2 3
EOF
exit 1
fi

main
exit 0
