#!/usr/bin/env bash

# Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run.
# Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end.
# Bonus points if you can also report how many runs it took for the script to fail.

n=$((RANDOM % 100))

if [[ n -eq 42 ]]; then
	echo "Something went wrong"
	echo >&2 "The error was using magic numbers"
	exit 1
fi

echo "Everything went according to plan"
