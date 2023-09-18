#!/usr/bin/env bash

>output.txt

echo "type new lines, followed by enter. When done, hit enter on an empty input."

while read -r line; do
	echo "$line" >>output.txt

	if [[ -z "$line" ]]; then
		break
	fi
done
