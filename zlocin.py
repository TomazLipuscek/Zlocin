# -*- coding: utf-8 -*-

__author__ = 'Tomaž'

import urllib2

data = urllib2.urlopen("https://dl.dropboxusercontent.com/u/29645703/SmartNinja/DNK/dna.txt")
for line in data:
    #barva las
    if line.find("CCAGCAATCGC") != -1:
        print("Crni lasje")
    if line.find("GCCAGTGCCG") != -1:
        print("Rjavi lasje")
    if line.find("TTAGCTATCGC") != -1:
        print("Korenckasti lasje")

    #oblika obraza
    if line.find("GCCACGG") != -1:
        print("Kvadraten obraz")
    if line.find("ACCACAA") != -1:
        print("Okrogel obraz")
    if line.find("AGGCCTCA") != -1:
        print("Ovalen obraz")
    #barva oci
    if line.find("TTGTGGTGGC") != -1:
        print("Modre oci")
    if line.find("GGGAGGTGGC") != -1:
        print("Zelene oci")
    if line.find("AAGTAGTGAC") != -1:
        print("Rjave oci")
    #spol
    if line.find("TGCAGGAACTTC") != -1:
        print("Moski")
    if line.find("TGAAGGACCTTC") != -1:
        print("Zenska")
    #rasa
    if line.find("AAAACCTCA") != -1:
        print("Belec")
    if line.find("CGACTACAG") != -1:
        print("Crnec")
    if line.find("CGCGGGCCG") != -1:
        print("Azijec")


    #Ziga
    if line.find("TTAGCTATCGC") != -1 and line.find("ACCACAA") != -1 and line.find("AAGTAGTGAC") != -1 and line.find("TGCAGGAACTTC") != -1 and line.find("AAAACCTCA") != -1:
        print("Osumljenec je Ziga!")
    #Matej
    if line.find("CCAGCAATCGC") != -1 and line.find("AGGCCTCA") != -1 and line.find("TTGTGGTGGC") != -1 and line.find("TGCAGGAACTTC") != -1 and line.find("AAAACCTCA") != -1:
        print("Osumljenec je Matej!")
    #Miha
    if line.find("GCCAGTGCCG") != -1 and line.find("GCCACGG") != -1 and line.find("GGGAGGTGGC") != -1 and line.find("TGCAGGAACTTC") != -1 and line.find("AAAACCTCA") != -1:
        print("Osumljenec je Miha!")