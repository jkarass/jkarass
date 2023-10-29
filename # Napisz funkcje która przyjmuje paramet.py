# Napisz funkcje która przyjmuje parametr 'n' i zlicza sumę 1 do n.

# Zmierz czas wykonywania powyższej funkcji 

def suma_od_1_do_n(n):
    n = int(input("Podaj liczbę n: "))
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
 
wynik = suma_od_1_do_n(0)
print("Suma od 1 do n wynosi:", wynik)
 
