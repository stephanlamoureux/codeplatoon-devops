#!/usr/bin/env bash

count=0
while true; do
	# &> is stdout and stderr outputted to a file
	./test.sh &>log
	# $? is the return code of the previous command. Anything other than 0 is an error.
	if [ $? != 0 ]; then
		break
	fi
	((count++))
done

echo "total run times: $count"
cat log
