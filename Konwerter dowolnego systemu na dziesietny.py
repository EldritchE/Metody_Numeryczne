#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *

def conv(liczba, z, do):    #konwertuje najpierw liczbę na system dziesiętny,
    dec=0
    int(dec)

    #potem na docelowy
    val="0123456789abcdefghijklmnoprstuwvxyz"
    for V in liczba:        #duże V - znak
        dec*=int(z)              #przemnożenie aktualnej wartości liczby dziesiętnej
                            #przez podstawę systemu źródłowego
        v=0                 #małe v - wartość liczbowa danego znaku
        while V!=val[v]:    #szukanie w tablicy `val tej wartości małe v
            v+=1
        dec+=v
    #w tym miejscu mamy już liczbę w systemie dziesiętnym
    #teraz zamiana na docelowy
    print("dziesiętnie :",dec)
    liczba="" #źródłowy tekst nam już nie jest potrzebny, więc czyścimy
    while dec>0:                    #dopóki licza w postaci 10 jest większa od zera
        v=dec%do                    #wartość liczbowa danego znaku w
                                    #docelowym systemie
        liczba=str(val[v])+str(liczba)   #na początek stringu wstawia
        int(do)                            #wartość w docelowym systemie
        dec//=do
    return liczba

print ("wprowadź liczbę: ")
liczba=input()
print ("Z systemu: ")
z=input()
print ("Na system: ")
do=int(input())

print ("Wynik: "+conv(liczba, z, do))