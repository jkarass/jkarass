# Napisz funkcje która przyjmuje parametr 'n' i zlicza sumę 1 do n.

# Zmierz czas wykonywania powyższej funkcji 

import time

def suma_od_1_do_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Dane wsadowe użytkownika
n = int(input("Podaj liczbę n: "))

# Pomiar długości działania funkcji 
start_time = time.time()
wynik = suma_od_1_do_n(n)
end_time = time.time()

print("Suma od 1 do", n, "wynosi:", wynik)
print("Czas wykonania funkcji:", end_time - start_time, "sekundy"),
