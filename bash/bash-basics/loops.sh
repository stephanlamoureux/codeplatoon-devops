#!/bin/bash

# while loop
i=0
while [ $i -le 2 ]; do
	echo Number: $i
	((i++))
done

# for loop
for ((counter = 1; counter <= 10; counter++)); do
	echo -n "$counter "
done
printf "\n"

# continue
for ((i = 0; i < 10; i++)); do
	if [[ "$i" -ge 4 ]] && [[ "$i" -le 8 ]]; then
		echo "$i"
	else
		continue
	fi
done

# break
i=$((0))
while ((i < 10)); do
	echo "$i"
	i=$((i + 1))

	if [[ "$i" -eq 7 ]]; then
		break
	fi
done
