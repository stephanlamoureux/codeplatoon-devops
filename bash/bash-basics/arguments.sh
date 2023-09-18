#!/bin/bash

# $0 is name of file. $1 and so an are variables for arguments.
echo "name of script: $0"
echo "the number of arguments are: " "$#"
echo "print individually using $1, $2 etc: " "$1" "$2" "$3"
echo 'print all using $*: ' "$*"
# store arguments as an array
args=("$@")
echo "print as individual array items: " "${args[0]}" "${args[1]}" "${args[2]}"
echo "print the index:" "${!args[@]}"
echo "print all items in array: " "$@"
