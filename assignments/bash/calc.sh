#!/usr/bin/env bash

echo "Basic Calculator"
printf "\n"

sum=0
continue="y"
read -rp "First number: " n1
read -rp "Second number: " n2

while [ "$continue" = "y" ]; do
	echo "1.Addition"
	echo "2.Subtraction"
	echo "3.Multiplication"
	echo "4.Division"
	read -rp "Enter [1-4]: " option

	case $option in
	1)
		sum=$(echo " $n1 + $n2" | bc -l)
		echo "$n1 + $n2 =" "$sum"
		;;
	2)
		sum=$(echo "$n1 - $n2" | bc -l)
		echo "$n1 - $n2 =" "$sum"
		;;
	3)
		sum=$(echo "$n1 * $n2" | bc -l)
		echo "$n1 * $n2 =" "$sum"
		;;
	4)
		sum=$(echo "$n1 / $n2" | bc -l)
		echo "$n1 / $n2 =" "$sum"
		;;
	*) echo "invalid choice" ;;
	esac

	read -rp "Do you want to continue y/n: " continue
	if [ "$continue" != "y" ]; then
		exit
	fi
done
