#!/usr/bin/env bash

# 1. Store the output of the command “hostname” in a variable. Display “This script is running on .” where “” is the output of the “hostname” command.

# 2. Write a shell script to check to see if the file “file_path” exists. If it does exist, display “file_path passwords are enabled.” Next, check to see if you can write to the file. If you can, display “You have permissions to edit “file_path.””If you cannot, display “You do NOT have permissions to edit “file_path””.

# 3. Write a shell script that displays “man”,”bear”,”pig”,”dog”,”cat”,and “sheep” on the screen with each appearing on a separate line. Try to do this in as few lines as possible.

# 4. Write a shell script that prompts the user for a name of a file or directory and reports if it is a regular file, a directory, or another type of file. Also perform an ls command against the file or directory with the long listing option.

# 5. Modify the previous script to that it accepts the file or directory name as an argument instead of prompting the user to enter it.

# Assignment 1
hostname=$(hostname)
echo "This script is running on $hostname."

# Assignment 2
if [ -f file_path ]; then
	echo "file_path passwords are enabled."
	if [ -w file_path ]; then
		echo "You have permissions to edit file_path."
	else
		echo "You do NOT have permissions to edit file_path."
	fi
fi

# Assignment 3
printf "man\nbear\npig\ndog\ncat\nsheep\n"

# Assignment 4
read -rp "Enter a file or directory name: " name

if [ -f "$name" ]; then
	echo "Regular file."
elif [ -d "$name" ]; then
	echo "Directory."
elif [ -e "$name" ]; then
	echo "Other file."
else
	echo "Error."
fi

ls "$name" -lah

# Assignment 5
if [ -f "$1" ]; then
	echo "Regular file."
elif [ -d "$1" ]; then
	echo "Directory."
elif [ -e "$1" ]; then
	echo "Other file."
else
	echo "Error."
fi
