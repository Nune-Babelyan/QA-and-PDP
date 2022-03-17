#!/usr/bin/env python3
import sys

#name = input('name: ')
def name_function(name):
    if len(name) == 0:
        print('Please enter the first letter of the name in capital letters: \n LAST WARNING')
        #name = input('name: ')
        if len(name) == 0:
            return 0
            sys.exit()
        if name[0].isupper() and name[0].isdigit() == False:
            name = name
            print(name)
            return name
        else:
            return 0
            sys.exit()
    if name[0].isupper() and name[0].isdigit() == False:
        name = name
        print(name)
        return name
    else:
        print('Please enter the first letter of the name in capital letters: \n LAST WARNING')
        #name = input('name: ')
        if name[0].isupper() and name[0].isdigit() == False:
            name = name
            print (name)
            return name
        else:
            return 0
            #sys.exit()
#name_function(name)
