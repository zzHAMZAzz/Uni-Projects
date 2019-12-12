#! /bin/bash




ok=1
while [[ $ok -eq 1 ]]
do
clear
echo "===================================="
echo "=  System Managment Tool  ="
echo "===================================="
echo ""
echo ""
echo "Select an Option:"

echo ""
echo ""
echo "(u)ptime"	
echo "(d)isk free"
echo "(c)urrent users"
echo "(e)xit"	

	
	read showmenu
	if [[ $showmenu == "u" ]]
	then
		ok=0
		echo ""
		echo ""
		echo ""
		echo "Uptime:"
		uptime
		read waiting
		clear
		ok=1
	elif [[ $showmenu == "e" ]]
	then
	clear
	exit

	elif [[ $showmenu == "d" ]]
	then
	ok=0
	clear
	df
	read waiting
	ok=1

	elif [[ $showmenu == "c" ]]
	then
		ok=0
		echo ""
		echo "Logged in users:"
		users
		read waiting
		ok=1
 	fi

done
