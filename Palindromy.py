def czyPalindorm(tekst):
    # eliminacja wszystkich znaków specjalnych z  tekstu
    dozwolone_znaki = ['A', 'Ą' ,'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O',
                       'Ó', 'P','Q', 'R', 'S', 'Ś', 'T', 'U', 'W','V', 'X', 'Y', 'Z', 'Ż', 'Ź']
    for i in tekst:
        if i not in dozwolone_znaki:
            tekst = tekst.replace(i, "")
    #sprawdzanie poszczególnych elementów tekstu (pierwszy porównanie do ostaniego , drugi do przedostatniego )
    dlugoscCiagu=len(tekst)

    for i in range(dlugoscCiagu-1):
        a=tekst[i]
        b=tekst[dlugoscCiagu-1-i]
        if i>=dlugoscCiagu//2: # jak dojdziemy do środka ciągu nie ma sensu  dalej sprawdzać , słowo jest palindromem
            return True
        else:
             if tekst[i]!=tekst[dlugoscCiagu-1-i]:
                return False

    return True





print("Program sprawdzajacy czy dwa slowa w pliku sa Palindromami ")
print("wczytujemy palindromy_plik1.txt ")
plik1=open('palindromy_plik1.txt','r', encoding='utf8')
plik2=open('palindromy_plik2.txt', 'w',encoding='utf8')
slowa=plik1.readlines()
print(slowa)
plik1.close()

i=0
plik_wynikowy=open("anagramy_plik2.txt", "w") #przygotowanie pliku do zapisu wyników
print()
#Przejście po każdym słowie  z każdym
j=len(slowa)
i=0
licznik_trafien=0
while i<j:

    tekst=slowa[i]
    if czyPalindorm(tekst.upper()):
        licznik_trafien +=1
        wynik = ("ciąg znaków z pliku palindromy_plik1.txt "+tekst[:-1]+" o indeksie  "+str(i)+" Jest Palindromem !"+"\n")  # [-1] ogranicza wyświetlanie znaku końca linii
        print(wynik)
        plik2.write(wynik)


    i+=1
ogolnie="W pliku palindromy_plik1.txt na "+str(j)+" ciągów "+str(licznik_trafien)+ " okazał(o) się Palindromami."
print(ogolnie)
plik2.write(ogolnie)
plik2.close()