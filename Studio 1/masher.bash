#! /bin/bash


if [ $# -lt 1 ]
then
        echo "ERROR: masher expected an argument."
        echo "Usage: $0 argument"
        echo "Example: ./masher.bash abc/123"
        exit 1
fi

clear

argument1=$1

echo "Selected argument: $argument1"
echo ""
echo ""

echo "Using the selected argument as string: "
echo -n "$arugment1"

echo ""
echo ""


echo "Number of letters in string: "
echo -n "$argument1" | wc -m
echo ""
echo ""


echo "Number of characters in string: "
echo -n "$argument1" | tr -d '0-9' | wc -m
echo ""
echo ""


echo "Number of digits in string: "
echo -n "$argument1" | tr -dc '0-9' | wc -m
echo ""
echo ""

echo "Number of non-alpha characters in string: "
echo -n "$argument1" | tr -d '[a-zA-Z0-9]._-' | wc -m
echo ""
echo ""


read wait
clear
exit
