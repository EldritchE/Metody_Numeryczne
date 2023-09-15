def brute_force():
    print()
    punkt=0         #index poczatkowej litery z tekstu do sprawdzenia
    licznik_trafien=0 #licznik trafień
    while punkt<=(dl_text-dl_szukane):
        if text[punkt:punkt+dl_szukane]==szukane:       #jeśli badany fragment odpowiada szukanemu
            licznik_trafien += 1    #zwiekszenie licznika trafień i wydruk informacji
            print("Trafienie znaleziono zadany ciąg :", szukane, " w tekscie !! na pozycji o indeksie: ", punkt)
            print(text[0:punkt] + '\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + szukane + '\x1b[38;2;255;0;0m\x1b[00;2;255;255;0m' + text[(punkt  + dl_szukane):])

        punkt+=1    # szukamy dalej przeuswając się  o jeden w tekscie

    print("znaleziono :", licznik_trafien, "wystąpień szukanej frazy w tekscie") # jesli speniono warunek wyjscie wydruk info o ilości trafień
    return




text = "zlek pamięlektnika młodej lekarki lek   saleksanlek"  # tekst do przeszukania
szukane = "lek"  # wzorzec do wyszukania

dl_text = len(text)         #długość tekstu
dl_szukane = len(szukane)   #długość szukanego ciągu

if dl_text <= dl_szukane:  # sprawdzenie czy dlugosć szukanego nie jest dłuższa niz przeszukiwany tekst
    print("długość szukanego ciągu jest większa niż długość tekstu ")
    exit()
print("\n","szukanie frazy: '",szukane, "' w tekscie :'",text,"'\n")
brute_force()
