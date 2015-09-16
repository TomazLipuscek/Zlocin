# -*- coding: utf-8 -*-

import sys
import csv
import datetime

__author__ = 'Tomaž'


def script():
    st1 = raw_input("Podaj prvo stevilo: ")
    st2 = raw_input("Podaj drugo stevilo: ")
    st3 = raw_input("Podaj operacijo: +, -, /, *: ")
    try:
        st1s = float(st1)
        st2s = float(st2)
        if st3 == "+":
            rezultat = st1s+st2s
            print(rezultat)
        elif st3 == "-":
            rezultat = st1s-st2s
            print(rezultat)
        elif st3 == "/":
            rezultat = st1s/st2s
            print(rezultat)
        elif st3 == "*":
            rezultat = st1s*st2s
            print(rezultat)
        else:
            print("Napaka pri vnosu operacije!")
        ura = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('log.csv', 'a') as fp:
            a = csv.writer(fp, delimiter='/')
            data = [['---------------------------------------------------------'],
            [ura, st1s, st2s, st3, rezultat]]
            a.writerows(data)
        restart()
    except ValueError:
            print "Opala! Tega pa ni bilo mogoce izracunati!"
            restart()
def restart():
    ponovno = raw_input("Zelis ponovno racunati?")
    if ponovno=="da":
        script()
    elif ponovno=="ne":
        sys.exit()
    else:
        print("da/ne?")
        restart()
script()

