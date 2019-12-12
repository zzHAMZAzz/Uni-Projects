#! /bin/bash

echo "===================================="
echo "=  Area/Perimeter of a Rectangle Calculator  ="
echo "===================================="
echo ""
echo ""
echo "Choose (A)rea or (P)ermieter:"

read calc


if [ $calc = "A" ]
then
	echo "You've chosen to calculate Area..."
	echo ""
	echo ""
	echo ""
	echo "Enter length x of the rectangle:"
	
	read lengthX
	
	echo "Enter length y of the rectangle:"
	
	read lengthY
	
	echo "Calculating Area"
	echo ""
	echo "==="
	echo ""
	echo "Area of the Rectangle is:"
	
	expr $lengthX \* $lengthY 
	
	read wait
    clear
    exit
fi

if [ $calc = "P" ]
then
	echo "You've chosen to calculate Perimeter..."
	echo ""
	echo ""
	echo ""
	echo "Enter length x of the rectangle:"
	
	read lengthX
	
	echo "Enter length y of the rectangle:"
	
	read lengthY
	
	echo "Calculating Permieter"
	echo ""
	echo "==="
	echo ""
	echo "Permieter of the Rectangle is:"
	
	expr $lengthX \+ $lengthY 
	
    read wait
    clear
    exit
    fi
