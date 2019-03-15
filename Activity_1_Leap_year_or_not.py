# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:34:35 2019
@author: korayguneri
Objective:Leap year or not
Description: determines if the given year is a leap year or not
Version:1.0
global evaluation score: 8.75/10
"""
# get the year as input from the user
YEAR = int(input("Enter a year: "))

if (YEAR % 4) == 0:
    if (YEAR % 100) == 0:
        if (YEAR % 400) == 0: #if it is devisable by 400 then it's a leap year
            print("{0} is a leap year".format(YEAR))
        else:
            print("{0} is not a leap year".format(YEAR))
    else:
        print("{0} is a leap year".format(YEAR))
else:
    print("{0} is not a leap year".format(YEAR))
    