# import bibliotek
import random


# inicjalizacja licznika prób
i = int(0)
licznikPrzejść = 0
niska=1
wysoka=1000
while licznikPrzejść <=1000000:
    licznikPrzejść=licznikPrzejść+1
    zgadujemy = random.randint(0, 1000)     #losowanie liczby do sprawdzenia
    print (zgadujemy, "to szukana liczba")
    print("Zgadywanie liczb z przedzialu  [0; 1000] ")  # napis informujący o funkcjonalności  programu

    max=1000
    min=1
    zgadywana = int(random.random()*max+1)
    print (zgadywana)


    print("Próba :",licznikPrzejść)


    # pętla while do wykonywanan do czasu do kiedy zgadujemy  nie równa się zgadywana
    niska = 1
    wysoka = 1000
    while (zgadujemy != zgadywana):
        zgadujemy = random.randint(niska, wysoka)  # losowanie wartości zmiennej do sprawdzenia
        i += 1  # zwiększanie licznika prób

        print("proba numer", i)  # Informacja o nr kolejnym próby

        if (zgadujemy < zgadywana):  # sprawdzanie czy zgadujemy jest mniejsza od zgadywanej
            niska = zgadujemy + 1  # jeżeli próba zgadnięcia jest mniejsza od zgadywanej zawężamy zakres od dołu do próbowanej liczby bez niej samej
            print(zgadujemy, "  jest za mala")  # jeśli tak print 'za mała
            print("teraz zakres został zawężony do liczb od (", niska, "-", wysoka,
                  (")"))  # wypisanie zawężonego zakresu wyszukiwania
        elif (zgadujemy > zgadywana):  # jeśli zgadujemy większa od zgadywanej
            wysoka = zgadujemy - 1  # jeżeli próba zgadnięcia jest większa od zgadywanej zawężamy zakres od góry  do próbowanej liczby bez niej samej
            print(zgadujemy, "  jest za duża")  # jeśli tak print 'za duża'
            print("teraz zakres został zawężony do liczb od (", niska, "-", wysoka,
                  (")"))  # wypisanie zawężonego zakresu wyszukiwania


    print("Brawo ! ", zgadywana,  # jeśli obydwa powyższe warunki nie spełnione znaczy że nastąpiło trafienie
            "to właściwa liczba. Odkryta po ",  # wypisanie informacji o właściwym trafieniu , podanie zgadniętej liczby
            i, " probach")  # oraz wypisanie ilości prób , które wykonano
print ("Srednia liczba prób zgadnięcia liczby z przedziału (1-1000) w milionie przebiegów to ",i/1000000)





