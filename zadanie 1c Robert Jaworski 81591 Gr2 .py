def mergeSort(arr):
    if len(arr) > 1:  # jeśli długość listy wejsciowej wieksza od 1 , (warunek wyjścia z rekurencji)

        # znajdowanie środka tablicy
        mid = len(arr) // 2

        # podział na stronę Lewą
        L = arr[:mid]
        print (L)
        # i stronę prawą
        R = arr[mid:]
        print(R)

        # dzielenie części lewej
        mergeSort(L)

        # sortowanie części prawej
        mergeSort(R)
        #Ustawienie 3 zmiennych licznikowych na 0
        i = j = k = 0

        # Kopiowanie danych do tymczasowych list
        while i < len(L) and j < len(R): #dopóki długość listy lewej i listy prawej jesky większe od licznika długości
            if L[i] <= R[j]: #jeśli element i z listy lewej jest <= od elementu j z listy prawej
                arr[k] = L[i]# zpisz ten element i na pozycji k w liscie
                i += 1  # zwiększ licznik pozycji i
            else:
                arr[k] = R[j] # w przeciwnymy przypadku zpisz element prawy  na pozycji k w liscie
                j += 1  # zwiększ licznik j 0 jeden listy prawej
            k += 1      #zwieksz licznik pozycji listy wynikowej (pozycja w liscie głownej)

        # sprawdzanie czy zostały jakieś elementy listy Lewej
        while i < len(L):#dopóki i< od dlugości listy lewej
            arr[k] = L[i]#do listy na pozycję k zapisz wartość listy Lewej z pozycji i
            i += 1      # zwiększ licznik  o jeden listy lewej
            k += 1      #zwieksz licznik pozycji listy wynikowej (pozycja w liscie głownej)
        # sprawdzanie czy zostały jakieś elementy listy prawej
        while j < len(R):#dopóki i< od dlugości listy prawej
            arr[k] = R[j]#do listy na pozycję k zapisz wartość listy Prawej z pozycji j
            j += 1      # zwiększ licznik o jeden listy prawej
            k += 1      #zwieksz licznik pozycji listy wynikowej (pozycja w liscie głownej)


# kod odpowiedzialny za wydruk listy


def printList(arr):                     #procedura wydruku wyniku
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':                              #początek programu inicjalizacja listy do posortowania
    arr = [19, 11, 3, 554, 6, 7]  # lista wejsciowa        #wywołania fuknkcji sortującycych i drukujących wynik
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)