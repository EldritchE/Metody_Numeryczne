plik1=open('plik1.txt')         #otwarcie plików
plik2=open("plik2.txt")
lista1=[]                          #utworzenie 2 list
lista2=[]
for line in plik1:                  #zapisanie zawartości plików do list z pominięciem znaków specjalnych
    liczba=line.strip()
    lista1.append(liczba)
print ("Zawartość plik1.txt ",lista1)
for line in plik2:
    liczba=line.strip()
    lista2.append(liczba)
print ("Zawartość plik1.txt ",lista2)
dlugoscListy1=(len(lista1))
dlugoscListy2=(len(lista2))
print()
wspólne=[]          #szukanie części wspólnej w dwóch plikach
zbior1=set(lista1)  #zamiana list na zbiory w celu eliminacji powtórzeń wystąpień (właściwość zbiorów)
zbior2=set(lista2)
for element1 in lista1:         #iteracja po pierwszej liście i próba dopasowania kolejnych elementów na drugiej liście,
    for element2 in lista2:     #jeśli pasuje dopisanie elementu wspólniewystępującego do listy wspolne
        if element1 == element2:
            wspólne.append(element1)

zbiorwsp=set(wspólne)           #zamiana listy na zbiór w celu eliminacji powtórzeń
list1=list(zbior1)              #powrotna zmiana zbiorów na listy w celu przeprowadzenia eliminacji elementów wspólnych
list2=list(zbior2)              #z zaadniczych zbiorów ,

print ("elementy występujące w dwóch plikach ", zbiorwsp)       #Prezentacji znalezionych wspólnych elementów
for wsp in zbiorwsp:
    for druga in list1:                                         #wyodrębnienie elementów unikalnych dla każdej listy
        if wsp==druga:                                          #przez sprawdzenie czy w zbiorach unikalnych znajdują się jescze elementy wspólne
            list1.remove(wsp)

for wsp in zbiorwsp:
    for druga in list2:
        if wsp==druga:
            list2.remove(wsp)



print ("elementy występujące tylko w pliku1.txt ", list1)       #prezentacja list z elementami unikalnymi,
print ("elementy występujące tylko w pliku2.txt ",list2)