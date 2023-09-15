# import bibliotek
import random
import sys
#funkcja zakończenia programu
def koniec():
    print("KONIEC ! Do widzenia.")
    sys.exit(0)
#funkcja pytającą o jeszce jedną próbę lub koniec programu
def czykoniec():
    decyzja=input("kończymy (T) czy jescze raz (N) (?)    (T/N)")
    if decyzja=="t" or decyzja == "T":
        koniec()
    if decyzja=="n" or decyzja=="N":
        main()
    czykoniec()

#Funkcja algorytmu zgadywania liczby
def pro(zgadywana,zgadujemy):
    # inicjalizacja licznika prób
    i = int(0)

    # pętla while do wykonywanan do czasu do kiedy zgadujemy  nie równa się zgadywana
    niska=1
    wysoka=1000
    while (zgadujemy != zgadywana):
        zgadujemy = random.randint(niska, wysoka) #losowanie wartości zmiennej do sprawdzenia
        i += 1 #zwiększanie licznika prób

        print("proba numer", i)  #Informacja o nr kolejnym próby

        if (zgadujemy < zgadywana): #sprawdzanie czy zgadujemy jest mniejsza od zgadywanej

            print(zgadujemy,"  jest za mala")    #jeśli tak print 'za mała'

        elif (zgadujemy > zgadywana):   #jeśli zgadujemy większa od zgadywanej

            print(zgadujemy,"  jest za duża")     #jeśli tak print 'za duża'



    print("Brawo ! ", zgadywana,     #jeśli obydwa powyższe warunki nie spełnione znaczy że nastąpiło trafienie
          "to właściwa liczba. Odkryta po ",    #wypisanie informacji o właściwym trafieniu , podanie zgadniętej liczby
          i, " probach")                        #oraz wypisanie ilości prób , które wykonano
    czykoniec()                                    #Wywołanie funkcji kończącej program
#główny moduł porgramu


def main():
    zgadujemy = random.randint(0, 1000)     #losowanie liczby do sprawdzenia
    print("Zgadywanie liczb z przedzialu  [0; 1000] ")  # napis informujący o funkcjonalności  programu

    zgadywana = input(
        'Podaj liczbę naturalną z przedziału (1 do 1000) do zgadnięcia :')  # wprowadzanie liczby do odgadnięcia przez użytkownika
    if zgadywana.isnumeric():   #sprawdzanie czy podana wartość w INPUT jest wartością liczbową jeśli tak to :
        zgadywana = int(zgadywana)  # zamian wprowadzonej liczby ze zmiennej typu str na int
        if zgadywana > 1000 or zgadywana < 0:   #po sprawdzenieu ze zmienna jest liczbą i jej zamianie na INT sprawdzanie czy należy do zadanego zakresu
            zgadywana = 0                      #Jeżeli wypada z zakresu przypisanie jej wartości 0
            print('zla liczba (nie z zakresu <1-1000>)')                #informacja że liczba jest z poza zakresu
            main()                                                      # W związku ze złymi danymi powrót do głównej funkcji programu
        pro(zgadywana,zgadujemy)   #jeśli walidacja wprowadzonych danych poprawna wywołanie funkcji szukającej liczby z przekazaniem zmiennych
    else:
        print("To ma być liczba !!")    #w przypadku wpisane inne znaki niż cyfry  informacja o złych danych i wywołanie głónwego programu
        main()

main()