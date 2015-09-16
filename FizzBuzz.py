# -*- coding: utf-8 -*-

__author__ = 'Tomaž'

num_konec = raw_input("Vnesi stevilo med 1 in 100:")
num = 1
while num < int(num_konec)+1:
    if num%3 == 0 and num%5 == 0:
        print("fizzbuzz")
    elif num%3 == 0:
        print("fizz")
    elif num%5 == 0:
        print("buzz")
    else:
        print (num)
    num = num + 1