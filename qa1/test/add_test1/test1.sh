#!/bin/bash

../../ex6.py < input.txt > out.txt

d=$(diff golden_out.txt out.txt)

if [[ -z $d ]]
then 
	echo PASS test1
else
	echo FATL test1
fi
