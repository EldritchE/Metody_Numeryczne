#  KMP (złożonośc czasowa algorytmu) O(m+n)
def KMPSearch(pat, txt):    #szukanie paternu w tekscie
    M = len(pat)              #zmienna długości paternu
    N = len(txt)              #zmienna długości tekstu

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M           #pusta lista dla najdłuższego prefixu sufixu o długości patenu
    j = 0                   #index paternu

    # najpierw tworzymy tablice lps dla patternu
    computeLPSArray(pat, M, lps)

    i = 0  # index dla  txt[]
    print(txt)  # wizualizacja obliczen wydruki
    print(pat)

    while i < N:        #dopóki i jest mniejsze od długości tekstu

        if pat[j] == txt[i]:        #jeśli znak z pozycji i  z tekstu pasuje do znaku z pozycji j paternu to
            print("pasuje", "  ", "mamy i=",i,"litera TEXTU dla i=",txt[i], "mamy j=",j,"Litera PAT dla j=",pat[j])
                #wydruka info o pasowaniu znaku

            i += 1      #zwiększenie liczników do badania 2 kolenych znaków patternu do tekstu
            j += 1


        if j == M:      #jeśli j jest takie samo jak długość patternu mamy trafienie patternu w tekscie
            print("Dopasowano wzorzec na pozycji o indeksie ", str(i - j)) #info o trafieniu
            print(txt)
            print(" " * (i - 1), pat)

            j = lps[j - 1]      # przypisanie do j wartości z tablicy prefixu sufixu wartości wcześniejszej

        # jeśli znaki zw tekscie i patternie z pozycji i i j sobie nie odpowiadają i i jest w dalszym ciągu mniejsze od długości patternu
        elif i < N and pat[j] != txt[i]:





            # Nie dopasowuj znaków od pozycji lps[0..lps[j-1]],

            # one już pasują

            if j != 0:

                j = lps[j - 1]




            else:

                i += 1  #w przeciwnym przypadku przesun wzorzec do i zwiększonego o 1 i zacznij kolejne sprawdzanie
                if pat[j] ==  txt[i]:           # wydruk graficznej reprezentacji w przypadku niedopasowania
                    print("Brak dopasowania , Przesuwamy wzorzec.")
                    print(txt)
                    print(" " * (i-1), pat)





def computeLPSArray(pat, M, lps): #tworzenie lps dla  patternu
    len = 0  # ustawienie długość poprzedniego najdłuższego prefixu sufixu

    lps[0]  # lps[0] zawsze zero dla pierwszego szukanego znaku
    i = 1

    # Oblicznie lps[i]do momentu aż braknie znaków w patternie
    while i < M:
        if pat[i] == pat[len]:    #jeśli znak na pozycji i w patternie odpowiada znakowi na pozycji len w patternie
            len += 1   #zwiększ len o 1
            lps[i] = len    #i zapisz do lps pod pozycją i wartość len
            i += 1             #zwiększ i o jeden
        else:
            # w przeciwnym przypadku
            if len != 0:                #jeśli len rózne od zera
                len = lps[len - 1]        #przypisz wartość do len z lps od len pomniejszonego o 1

                # nie zmiejszami tutaj i
            else:
                lps[i] = 0   # a jeśli lps doszło do wartości 0
                i += 1         # tu zwiększamy i
        #wyjściem jest gotowa tablica najdłuższego prefixu sufixu


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain