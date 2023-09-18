#!/bin/bash

echo "System details:"
echo "---------------"
echo "bash location: $BASH"
echo "home dir: $HOME"
echo "current dir: $PWD"
echo "current user: $USER"
echo "---------------"

read -pr "enter your name: " name
echo "Hello $name!"

read -spr "enter hidden message: " hidden
echo ""
echo "hidden message: $hidden"

echo "three favorite animals: "
read -ar animals
echo "Favorite animals: ${animals[*]}"
