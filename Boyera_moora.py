def Boyera_Moorea():
    print()
    tablica_trafien = []
    punkt = 0  # punkt zaczepienia w tekście dla sprawdzenia ciągu przesuwany pod wpływem spełniania poszcególnych warunków w głownej pętli
    licznik_trafien = 0  # licznik trafień
    while punkt <= (dl_text - dl_szukane):  # głowna pętla wyszukująca
        # print("",text[punkt:punkt+dl_szukane],"\n",szukane)
        if text[punkt:punkt + dl_szukane] == szukane:  # jeśli badany fragment odpowiada szukanemu
            licznik_trafien += 1  # zwiekszenie licznika trafień i wydruk informacji
            print("Trafienie znaleziono zadany ciąg :", szukane_org, " w tekscie !! na pozycji o indeksie: ", punkt)
            print(text_oryg[
                  0:punkt] + '\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + szukane_org + '\x1b[38;2;255;0;0m\x1b[00;2;255;255;0m' + text_oryg[
                                                                                                                                 (
                                                                                                                                             punkt + dl_szukane):])
            # print("indeksy w tekscie pozycji dopasowań :", tablica_trafien)
            tablica_trafien.append(punkt)
            punkt = punkt + dl_szukane
        else:
            i = dl_szukane - 1
            while i >= 0:
                # print("szukamy w czesci tekstu :\n", text[punkt + (dl_szukane - 1)], "\n", szukane[i], )
                if i == dl_szukane - 1 and text[punkt + dl_szukane - 1] == szukane[
                    i]:  # jesli pierwsza litera pasuje to znaczy ze przesuwamy o cały wyraz bo nie będzie trafienia bo nie spełnił sie warunek z linii 7
                    # print ("dopasowanie 1 ze sprawdzanych  znaku , przesuwamy o dl_szukane" )
                    i = -2  # wyrzucenie z pętli while
                    punkt = punkt + dl_szukane
                elif i != dl_szukane - 1 and i != 0 and text[punkt + dl_szukane - 1] == szukane[
                    i]:  # sprawdzanie kolejnych liter nie pierwsza i nie ostatnia z szukanego ciągu
                    # print("pasuje cos ze srodka")
                    punkt = punkt + i  # jeśli wystąpiła przesuwamy o pozycję równą indeksowi psaujacego znaku
                    i = i - 2  # wyrzucenie z pętli while
                elif i != dl_szukane - 1 and i == 0 and text[punkt + dl_szukane - 1] == szukane[
                    i]:  # sprawdzanie czy pasuje ostatnia litera szukanego ciągu
                    # print("pasuje ostatni znak ")
                    punkt = punkt + (
                                dl_szukane - 1)  # jeśli ostatnia pasuje przesunięcie punktu zaczepienia o długość szukanego ciągu -1
                    i = -2  # wyrzucenie z pętli while
                else:  # Jeżeli żaden z powyższych warunków nie zadziałał , znaczy ze nie było dopasowania nigdzie  i przesuwamy punkt zaczepienie o długość całego ciągu
                    i -= 1  # jak w przypadku trafienia
                    if i < 0:
                        punkt = punkt + dl_szukane

    print("znaleziono : " + '\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + str(
        licznik_trafien) + "" + '\x1b[38;2;255;0;0m\x1b[00;2;255;255;0m' + " " + "wystąpień szukanej frazy w tekscie"+" na pozycjach \n o indeksach "+str(tablica_trafien))  # jesli speniono warunek wyjscie wydruk info o ilości trafień

    return


text = """Lorem Ilopsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.


"""
text_oryg = text  # pozostawienie tekstu w oryginalnej postaci postaci do prawidłowego wydruku wyniku
text = text.lower()  # tekst do obróbki ignorujący wielkość znaków
# tekst do przeszukania TROSZKĘ GŁUPI tekst ale pozwala zbadać wszystkie przypadki trafien :)
szukane = input("Podaj szukaną frazę :")  # wzorzec do wyszukania
szukane_org = szukane  # pozostawienie szukanego zorca  w oryginalnej postaci postaci do prawidłowego wydruku wyniku
szukane = szukane.lower()  # do obróbki  do obróbki ignorujący wielkość znaków

dl_text = len(text)  # długość tekstu
dl_szukane = len(szukane)  # długość szukanego ciągu

if dl_text <= dl_szukane:  # sprawdzenie czy dlugosć szukanego nie jest dłuższa niz przeszukiwany tekst
    print("długość szukanego ciągu jest większa niż długość tekstu ")
    exit()
print("\n",
      "szukanie frazy: '"'\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + szukane + '\x1b[38;2;255;0;0m\x1b[00;2;255;255;0m' "' w tekscie \n",
      "IGNORUJEMY WIELKOŚĆ LITER np :  m=M")
Boyera_Moorea()
