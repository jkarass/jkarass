import random

# Definicje stanów
KAMIEN = 0
PAPIER = 1
NOZYCE = 2

# Funkcja zwracająca wynik gry
def wynik_gry(stan1, stan2):
    if stan1 == stan2:
        return 0
    elif (stan1 == KAMIEN and stan2 == NOZYCE) or (stan1 == PAPIER and stan2 == KAMIEN) or (stan1 == NOZYCE and stan2 == PAPIER):
        return 1
    else:
        return -1 
# test
# Funkcja, która losuje wybór bota na podstawie jego macierzy przejść
def wybory_bota(obecny_stan, macierz_przejsc):
    liczba = random.random()
    suma = 0
    for i in range(3):
        suma += macierz_przejsc[obecny_stan][i]
        if liczba < suma:
            return i

# Definiujemy funkcję, która konwertuje liczbę na nazwę stanu
def nazwa_stanu(liczba):
    if liczba == KAMIEN:
        return "kamień"
    elif liczba == PAPIER:
        return "papier"
    else:
        return "nożyce"

# Definiujemy funkcję, która aktualizuje macierz przejść na podstawie obecnego i następnego stanu dla danego bota
def aktualizuj_macierz(poprzedni_stan, obecny_stan, macierz_przejsc):
    for i in range(3):
        if i == obecny_stan:
            macierz_przejsc[poprzedni_stan][i] += 0.01
        else:
            macierz_przejsc[poprzedni_stan][i] -= 0.005

# Inicjalizacja macierzy przejść dla obu botów
macierz_przejsc_bot1 = {
    KAMIEN: [1/3, 1/3, 1/3],
    PAPIER: [1/3, 1/3, 1/3],
    NOZYCE: [1/3, 1/3, 1/3]
}

macierz_przejsc_bot2 = {
    KAMIEN: [1/3, 1/3, 1/3],
    PAPIER: [1/3, 1/3, 1/3],
    NOZYCE: [1/3, 1/3, 1/3]
}

# Definiujemy zmienną, która przechowuje liczbę rund gry
liczba_rund = 200

# Definiujemy zmienną, która przechowuje obecny stan dla obu botów
obecny_stan_bot1 = random.randint(0, 2)
obecny_stan_bot2 = random.randint(0, 2)

# Inicjalizacja punktów dla obu botów
punkty_bot1 = 0
punkty_bot2 = 0

# Pętla główna gry
for runda in range(liczba_rund):
    # Wypisujemy numer rundy
    print("\nRunda", runda + 1)

    # Wybór botów na podstawie ich macierzy przejść
    wybor_bot1 = wybory_bota(obecny_stan_bot1, macierz_przejsc_bot1)
    wybor_bot2 = wybory_bota(obecny_stan_bot2, macierz_przejsc_bot2)

    # Wyświetlamy wybory botów
    print("Bot 1 wybiera:", nazwa_stanu(wybor_bot1))
    print("Bot 2 wybiera:", nazwa_stanu(wybor_bot2))

    # Obliczanie wyniku rundy
    wynik = wynik_gry(wybor_bot1, wybor_bot2)
    if wynik == 0:
        print("Remis!")
    elif wynik == 1:
        print("Bot 1 wygrywa!")
        punkty_bot1 += 1
    else:
        print("Bot 2 wygrywa!")
        punkty_bot2 += 1

    # Aktualizujemy macierze przejść dla obu botów na podstawie ich wyborów
    aktualizuj_macierz(obecny_stan_bot1, wybor_bot1, macierz_przejsc_bot1)
    aktualizuj_macierz(obecny_stan_bot2, wybor_bot2, macierz_przejsc_bot2)

    # Zmieniamy obecny stan dla obu botów na ich wybory
    obecny_stan_bot1 = wybor_bot1
    obecny_stan_bot2 = wybor_bot2

    # Wyświetlamy liczbę punktów dla obu botów po każdej rundzie
    print("Punkty Bot 1:", punkty_bot1)
    print("Punkty Bot 2:", punkty_bot2)

# Wyświetlamy liczbę punktów dla obu botów po zakończeniu gry
print("\nPunkty końcowe - Bot 1:", punkty_bot1)
print("Punkty końcowe - Bot 2:", punkty_bot2)


