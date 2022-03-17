#!/bin/bash

for i in {1..5}
	do
		cd add_test$i
		./test$i.sh
		cd ../	
	done
