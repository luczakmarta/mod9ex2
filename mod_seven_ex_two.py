from datetime import datetime #importowanie daty

# Każdy film powinien mieć następujące atrybuty:
# Tytuł
# Rok wydania
# Gatunek
# Liczba odtworzeń


#Każdy serial powinien mieć następujące atrybuty:

 # Tytuł
 # Rok wydania
 # Gatunek
 # Numer odcinka
 # Numer sezonu
 # Liczba odtworzeń

import random

class Film:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen

  #Metoda play


    def play(self):
        self.liczba_odtworzen = self.liczba_odtworzen + 1

    def __str__(self):
        return f"{self.tytul} {self.rok_wydania} {self.liczba_odtworzen} "

#Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu
# w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym). Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania
# np. “Pulp Fiction (1994)”.
# Przechowuje filmy i seriale w jednej liście.


class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
    def __str__(self):
        return f"{self.tytul} S{self.numer_odcinka:02}E{self.numer_sezonu:02} {self.liczba_odtworzen}"


film_1 = Film (tytul="Avatar", rok_wydania=1981, gatunek="Science Fiction", liczba_odtworzen=89)
film_2 = Film (tytul="Shrek", rok_wydania=2005, gatunek="Comedy", liczba_odtworzen=51)
film_3 = Film (tytul="Titanic", rok_wydania=2001, gatunek="Melodrama", liczba_odtworzen=209)

serial_1 = Serial (tytul="Friends", rok_wydania=1990, gatunek="Sitcom", numer_odcinka=1, numer_sezonu=1, liczba_odtworzen=21)
serial_2 = Serial (tytul="Friends", rok_wydania=1991, gatunek="Sitcom", numer_odcinka=2, numer_sezonu=2, liczba_odtworzen=99)
serial_3 = Serial (tytul="Friends", rok_wydania=1992, gatunek="Sitcom", numer_odcinka=3, numer_sezonu=3, liczba_odtworzen=46)
serial_4 = Serial (tytul="Friends", rok_wydania=1994, gatunek="Sitcom", numer_odcinka=5, numer_sezonu=4, liczba_odtworzen=29)

lista = [film_1, film_2, film_3, serial_1, serial_2, serial_3, serial_4]

#Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz tylko seriale.



def get_movies(lista):
    for i in lista:
        if type(i) is Film:
            print(i)

def get_series(lista):
    for i in lista:
        if type(i) is Serial:
            print(i)

print ('Filmy')
get_movies(lista)
print()
print('Seriale')
get_series(lista)
print()


# Napisz funkcję search, która wyszukuje film lub serial po jego tytule.

def search (lista, wynik):
    l = []
    for i in lista:
        if wynik.lower() in i.tytul.lower():
            l.append(i)
    return l



wynik = input("podaj nazwę filmu:  ")
l = search(lista, wynik)

for i in l:
    print (i)
search (lista,wynik)

print ()
print ()

#Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.


def generate_views(lista):
    losowy = random.choice(lista)
    losowy.liczba_odtworzen += random.randrange(1, 100)

generate_views(lista)

# Napisz funkcję, która uruchomi generate_views 10 razy.

def gen10(lista):
    for i in range(10):
        generate_views(lista)

gen10(lista)
print ("")

print ("top_titles")

# Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych
# tytułów z biblioteki.



def top_titles(lista, rodzaj, ilosc):
    lista2 = sorted(lista, key=lambda lista: lista.liczba_odtworzen, reverse=True)

    l = []
    for i in lista2:
        if type(i) is rodzaj:
            l.append(i)
        if len(l) == ilosc:
            return l
    return l

def top_titles2(lista, ilosc):
    lista2 = sorted(lista, key=lambda lista: lista.liczba_odtworzen, reverse=True)

    l = []
    x = 0
    for i in lista2:
        x = x + 1
        l.append(i)
        if x == ilosc:
            return l
    return l


tt = top_titles(lista, Serial, 2)
print("2 najlepsze seriale")
for i in tt:
    print(i)

tt = top_titles(lista, Film, 2)
print("2 najlepsze filmy")
for i in tt:
    print(i)

print()

# Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki.
# Funkcja powinna przyjmować parametry takie jak: tytuł serialu, rok wydania, gatunek, numer sezonu, liczba odcinków do dodania.

def dodaj_seriale(lista, tytul, rok_wydania, gatunek, liczba_odcinkow, sezon):
    for i in range(1, liczba_odcinkow + 1):
        serial1 = Serial (tytul=tytul, rok_wydania=rok_wydania, gatunek=gatunek, numer_odcinka=i, numer_sezonu=sezon, liczba_odtworzen=0)
        lista.append(serial1)

dodaj_seriale(lista, "The Big Bank Theory", 2005, "Sitcom", 10, 2)

for i in lista:
    print(i)

print()
print("Biblioteka filmów")

film_1 = Film (tytul="Avatar", rok_wydania=1981, gatunek="Science Fiction", liczba_odtworzen=89)
film_2 = Film (tytul="Shrek", rok_wydania=2005, gatunek="Comedy", liczba_odtworzen=51)
film_3 = Film (tytul="Titanic", rok_wydania=2001, gatunek="Melodrama", liczba_odtworzen=209)
serial_1 = Serial (tytul="Friends", rok_wydania=1990, gatunek="Sitcom", numer_odcinka=1, numer_sezonu=1, liczba_odtworzen=21)
serial_2 = Serial (tytul="Friends", rok_wydania=1991, gatunek="Sitcom", numer_odcinka=2, numer_sezonu=2, liczba_odtworzen=99)
serial_3 = Serial (tytul="Friends", rok_wydania=1992, gatunek="Sitcom", numer_odcinka=3, numer_sezonu=3, liczba_odtworzen=46)
serial_4 = Serial (tytul="Friends", rok_wydania=1994, gatunek="Sitcom", numer_odcinka=5, numer_sezonu=4, liczba_odtworzen=29)


lista = [film_1, film_2, film_3, serial_1, serial_2, serial_3, serial_4]

for i in range(len(lista)):
    generate_views(lista)

now = datetime.now() # data

data = now.strftime("%d.%m.%Y")

print("Najpopularniejsze filmy i seriale z dziś " + data)

l = top_titles2(lista, 3)
for i in l:
    print(i)
