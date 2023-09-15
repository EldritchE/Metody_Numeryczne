#zamiana z systemy dziesiętnego na dowolny

def conv(liczba, z, do):

    val="0123456789abcdefghijklmnoprstuwvxyz"
    dec=int(liczba)
    #zamiana na docelowy
    print("dziesiętnie :",dec)
    liczba="" #źródłowy tekst nam już nie jest potrzebny, więc czyścimy
    while dec>0:                    #dopóki licza w postaci 10 jest większa od zera
        v=dec%do                    #wartość liczbowa danego znaku w
                                    #docelowym systemie
        liczba=str(val[v])+str(liczba)   #na początek stringu wstawia
        int(do)                            #wartość w docelowym systemie
        dec//=do
    print("Odpowiedź ::", liczba)
    return liczba

print ("wprowadź liczbę w systemie dziesiętnym : ")
liczba=input()
z=10
print ("zamieniamy na  system: ")
do=int(input())

conv(liczba, z, do)