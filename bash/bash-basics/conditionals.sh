#!/usr/bin/env bash

name="steve"

if [[ "$name" == "$USER" ]]; then
	echo "Your name is your username"
elif [[ "$EUID" == 0 ]]; then
	echo "Oh, hello superuser"
else
	echo "Your name is something else"
fi

age=35

if [[ "$USER" == "steve" ]] && [[ "$age" -eq 35 ]]; then
	echo "These are just the facts"
fi

num=1
case "$num" in
0) echo "There is a zero." ;;
1) echo "There is a one." ;;
*) echo "It's something else" ;;
esac
