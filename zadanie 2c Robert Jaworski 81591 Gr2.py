import random
import sys


def szukaj(lista):
    global i
    i = 0  # licznik wszystkich operacji
    przebiegi = 1

    while przebiegi <= 1000000:  # ilość liczk losowanych do odgadnięcia , w celach wyilicznia średniej
        maxi = 1000  # zakres górny losowaniej liczby do odnalezienia
        zgadywana = int(random.random() * maxi+ 1)  # losowanie poszukiwwanej
        przebiegi = przebiegi + 1

        # początek algorytmu binarnego wyszukiwania

        lewa = 0  # inicjowanie granic szukania
        prawa = len(lista) - 1
        proba = 0
        while lewa < prawa:
            proba = proba + 1

            srodek = (lewa + prawa) // 2  # wybór srodka

            if lista[srodek] < zgadywana:  # jeżeli element w srodku jest mniejszy od szukanego
                lewa = srodek + 1  # to odrzuć lewą stronę (przesuń lewą granicę)

            else:  # w drugim przypadku
                prawa = srodek  # odrzuć prawą stronę (przesuń prawą granicę)

            if lista[srodek] == zgadywana:  # sprawdzanie czy znaleziono szukany element

                i = i + proba
    return i


def tworzenie():
    liczba = 1  # tworzenie przedziału od 1 do 1000 (lista)
    global lista
    lista = []

    while liczba < 1001:
        lista.append(liczba)
        liczba = liczba + 1
    return


def wydrukWyniku(i):
    print("Srednia liczba prób zgadnięcia liczby z przedziału (1-1000) w milionie przebiegów to ", i / 1000000, "",
          "wykonano prób trafienia", i)


def main():
    tworzenie()
    szukaj(lista)
    wydrukWyniku(i)


main()

