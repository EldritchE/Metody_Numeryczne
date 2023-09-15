def sortujSlowo(slowo):  # definujemy funkcje sorutjaca slowo - wykorzystujemy tutaj sortowanie babelkowe
    s = list(slowo)  # poniewaz w Pythonie nie da sie modyfikowac stringa jako tablicy, potrzebujemy zapisac go jako liste
    zmian = 1
    for i in range(len(s) - 1): # sortowanie alfabetyczne
        if zmian == 0:
            break
        zmian = 0
        for j in range(len(s) - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
                zmian += 1
    ulozone="".join(s)  # miana podręcznej , posortowanej listy w string

    return ulozone #zwrot posortowanego alfabertcznie słowa słowa


def czyAnagramy(s1, s2):
    if len(s1) != len(s2):  # jezeli sa roznej dlugosci, to z gory wiadomo ze nie sa anagramami
        return False
    return sortujSlowo(s1.lower()) == sortujSlowo(s2.lower())  # w przeciwnym wypadku wystarczy sprawdzic, czy po posortowaniu sa identyczne lower() zapewnia pasowanie do siebie D i M liter


print("Program sprawdzajacy czy dwa slowa sa anagramami")
print("wczytujemy anagramy_plik1.txt ")
plik1=open('anagramy_plik1.txt','r')
plik2=open('anagramy_plik2.txt', 'w')
slowa=plik1.readlines()
plik1.close()


#teraz pętle przechodzące przez każde słowo w liscie i sprawdzające czy są jednakowej długości i czy pasują do siebie
j=0   #liczniki pętli
i=1
k=len(slowa)-1 #żeby nie porównywał ostatniego słowa do samego siebie
plik_wynikowy=open("anagramy_plik2.txt", "w") #przygotowanie pliku do zapisu wyników

#Przejście po każdym słowie  z każdym
while j<k:

    s1=slowa[j]

    i=i+j
    while i<len(slowa):

        s2=slowa[i]

        #wywołanie funkcji sprawdzającej czy dana para jest anagramem
        if czyAnagramy(s1,s2):

            wynik=("Podane slowo "+" "+s1[:-1]+" o o indeksie "+str(j)+" i slowo:"+s2[:-1]+" o indeksie "+str(i)+" " + "sa " + "anagramami"+"\n") # [-1] ogranicza wyświetlanie znaku końca linii
            print (wynik)
            plik2.write(wynik)
        i+=1
    i=1
    j+=1












