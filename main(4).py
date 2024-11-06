import string
#zad 1
#--------------------------------------------------------------------------
Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
#odwołanie do pierwszego/ostatniego elementu listy
print(Moja_lista[0])
print(Moja_lista[-1])
#zwraca długość listy (liczbę elementów)
print(len(Moja_lista))
#zwraca największa/najmniejszą wartość z list
print(max(Moja_lista))
print(min(Moja_lista))
#zwraca sumę elementów listy
print(sum(Moja_lista))
#Sortuje elementy listy (od najmniejszego lub alfabetycznie
print(sorted(Moja_lista))
#dodanie kolejnego elementu na końcu listy
Moja_lista.append(6)
print(Moja_lista)
#wstawienie elementu w określonym indeksie i oraz odpowiednie przesunięcie kolejnych elementów
Moja_lista.insert(2, 5)
print(Moja_lista)
#zwrócenie ostatniego elementu z listy z jednoczesnym usunięciem go z niej
popped = Moja_lista.pop()
print(popped)
print(Moja_lista)
#odwrócenie kolejności elementów w liście
Moja_lista.reverse()
print(Moja_lista)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
#łączenie dwóch list w jedną Pięciokrotne
listaL = lista1 + lista2
print(listaL)

#powtórzenie wartości listy1 w nowej liście 5 raz
listaM = lista1 * 5
print(listaM)

n = 3
m = 1
k = 2
#od początku do elementu n
print(Moja_lista[:n])
#od elementu o indeksie m do końca
print(Moja_lista[m:])
#dany zakres elementów m-n z krokiem k (jak w range)
print(Moja_lista[m:n:k])
#odwrócenie listy
print(Moja_lista[::-1])


#zad 2
#--------------------------------------------------------------------------
names = ["John", "Alice", "Michael", "Emma"]

# a. Posortuj ją alfabetycznie i wyświetl
names.sort()
print(names)

# b. Dodaj na końcu dwie osoby i pobierz ostatnią z nich poleceniem pop()
names.extend(["William", "Sarah"])
print(names)
removed_name = names.pop()
print(removed_name)
print(names)

# c. Na pozycji 3 dodaj jeszcze jedną osobę.
names.insert(2, "David")
print(names)

# d. Odwróć kolejność na liście i zdubluj ją.
names.reverse()
print(names)
names = names * 2
print(names)


#zad 3
#--------------------------------------------------------------------------
# a. Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
name = input("Insert name")
print("Witaj", name)

# Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to:” oraz wczytany wiek.
age = input("Insert your age: ")
print("Twój wiek to:", age)

# c. Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
first_name = input("Insert name: ")
last_name = input("Insert last name: ")
initials = first_name[0] + last_name[0]
print("initials:", initials.upper())

# d. Wczyta łańcuch i wyświetli go pięć razy.
string = input("Insert string: ")
print(string * 5)

# e. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy.
string1 = input("Insert first string: ")
string2 = input("Insert seconds string: ")
string3 = string1 + string2
print("third string", string3)

# f. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę pierwszego i drugą połowę drugiego.
string1 = input("Insert first string: ")
string2 = input("Insert seconds string: ")
half1 = len(string1) // 2
half2 = len(string2) // 2
string3 = string1[:half1] + string2[half2:]
print("third string", string3)


#zad 4
#--------------------------------------------------------------------------
zdanie = input("Wprowadź zdanie: ")
litery = [char.lower() for char in zdanie if char.isalpha()]
litery_posortowane = tuple(sorted(litery))
print("Posortowane litery w zdaniu:", litery_posortowane)
alfabet = set(string.ascii_lowercase)
litery_w_zdaniu = set(litery)
brakujace_litery = alfabet - litery_w_zdaniu
print("Brakujące litery w zdaniu:", tuple(sorted(brakujace_litery)))


#zad 5
#--------------------------------------------------------------------------
dni_tygodnia = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
print(dni_tygodnia)


#zad 6
#--------------------------------------------------------------------------
owoce = ["jabłko", "banan", "gruszka", "banan", "banan", "malina"]
banany = owoce.count("banan")
print(banany)


#zad 7
#--------------------------------------------------------------------------
moja_krotka = (10, 2, 6, 6, 9, 13, 0, 1)
moja_lista = list(moja_krotka)
moja_lista.sort()
pk = tuple(moja_lista)
print(pk)


#zad 8
#--------------------------------------------------------------------------
stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżancie",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)

ilość_stopnii = len(stopnie)  
Major_index = stopnie.index("Major") 
Pułkownik_wstepowanie = "Pułkownik" in stopnie  

print(ilość_stopnii, Major_index, Pułkownik_wstepowanie)

#zad 9
#--------------------------------------------------------------------------
zakupy = {
    "Mleko": 3.50,
    "Chleb": 2.20,
    "Jajka": 4.00,
    "Masło": 5.50,
    "Ser": 7.30
}
print("Lista zakupów:", zakupy)
suma_wydatkow = sum(zakupy.values())
print("Podsumowanie wydatków:", suma_wydatkow)