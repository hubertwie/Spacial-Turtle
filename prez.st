func sprawdz(a: int): int {
    if (a == 5) {
        return 100
    }
    print("To nie powinno się wypisać, jeśli a to 5!")
    return 0
}

print(sprawdz(5))

# 1. Zasięgi zmiennych – zmienna lokalna w funkcji nie wpływa na globalną
int globalna = 100

func test_scope(x: int) : int {
    int lokalna = x * 2
    print("wewnątrz funkcji: globalna=", globalna, " lokalna=", lokalna)
    return lokalna
}

print("przed: globalna=", globalna)          # przed: globalna= 100
int wynik_scope = test_scope(5)              # wewnątrz funkcji: globalna= 100 lokalna= 10
print("po: globalna=", globalna)             # po: globalna= 100
print("wynik_scope=", wynik_scope)           # wynik_scope= 10

# Próba dostępu do lokalnej spoza funkcji (powinien być błąd, ale jeśli ignorujemy, to puste lub 0)
#print(lokalna)  # odkomentuj by sprawdzić błąd

# 2. Rekurencja – silnia
func factorial(n: int) : int {
    if (n <= 1) {
        return 1
    } else {
        return n * factorial(n - 1)
    }
}
print("silnia(5)=", factorial(5))            # silnia(5)= 120

# 3. Rekurencja – Fibonacci (z drzewem wywołań)
func fib(n: int) : int {
    if (n <= 1) {
        return n
    } else {
        return fib(n - 1) + fib(n - 2)
    }
}
print("fib(6)=", fib(6))                     # fib(6)= 8

# 4. Pętla for i while z break/continue
func test_loops() : int {
    int suma = 0
    for (int i = 0; i < 5; i = i + 1) {
        if (i == 2) {
            continue    # pomiń i=2
        }
        if (i == 4) {
            break       # zakończ przed i=4
        }
        suma = suma + i
    }
    # i = 0,1,3 -> suma = 4
    int j = 0
    while (j < 3) {
        suma = suma + j
        j = j + 1
    }
    # dodane 0+1+2=3, suma=7
    return suma
}
print("test_loops()=", test_loops())          # test_loops()= 7

# 5. Instrukcje warunkowe zagnieżdżone
func test_if(a: int, b: int) : int {
    if (a > b) {
        if (a - b > 5) {
            return 10
        } else {
            return 5
        }
    } else {
        if (b - a > 3) {
            return 20
        } else {
            return 2
        }
    }
}
print("test_if(10,3)=", test_if(10,3))       # 10-3=7>5 => 10
print("test_if(8,4)=", test_if(8,4))         # 8-4=4 <=5 => 5
print("test_if(2,10)=", test_if(2,10))       # 10-2=8>3 => 20
print("test_if(5,7)=", test_if(5,7))         # 7-5=2 <=3 => 2

# 6. Zasięg zmiennych w bloku if (bez osobnego zakresu, jeśli nie ma klamry?)
# W języku bloki if tworzą zakres (push_scope w firstpass dla if)
func test_if_scope(cond: bool) : int {
    int x = 1
    if (cond) {
        int y = 10
        x = x + y
    } else {
        int y = 20
        x = x + y
    }
    # y nie powinno być dostępne tutaj (powinien być błąd)
    #  print(y)  # błąd
    return x
}
print("test_if_scope(true)=", test_if_scope(true))   # 1+10=11
print("test_if_scope(false)=", test_if_scope(false)) # 1+20=21

# 7. Funkcja zwracająca wartość logiczną
func is_even(n: int) : bool {
    return n % 2 == 0
}
print("is_even(4)=", is_even(4))               # true
print("is_even(7)=", is_even(7))               # false

# 8. Funkcja z pętlą for i warunkiem wewnątrz
func sum_of_squares(limit: int) : int {
    int s = 0
    for (int i = 1; i <= limit; i = i + 1) {
        s = s + i * i
    }
    return s
}
print("sum_of_squares(3)=", sum_of_squares(3)) # 1+4+9=14

# 9. Funkcja wzajemnie rekurencyjna (even/odd)
func even(n: int) : bool {
    if (n == 0) { return true }
    else { return odd(n - 1) }
}
func odd(n: int) : bool {
    if (n == 0) { return false }
    else { return even(n - 1) }
}
print("even(4)=", even(4))                     # true
print("odd(4)=", odd(4))                      # false

# 10. Pętla while z warunkiem złożonym
func sum_until(limit: int) : int {
    int i = 0
    int s = 0
    while (i < limit and s < 100) {
        i = i + 1
        s = s + i
    }
    return s
}
print("sum_until(200)=", sum_until(200))       # 105? (suma 1..14=105, 15>100) -> 105

# 11. Zagnieżdżone pętle for
func nested_loops() : int {
    int count = 0
    for (int i = 0; i < 3; i = i + 1) {
        for (int j = 0; j < 3; j = j + 1) {
            count = count + 1
        }
    }
    return count
}
print("nested_loops()=", nested_loops())       # 9

# 12. Funkcja z domyślną wartością zmiennej (brak inicjalizacji) – domyślnie 0
func test_default() : int {
    int x  # brak inicjalizacji – powinno być 0
    return x
}
print("test_default()=", test_default())       # 0

# 13. Wywołanie funkcji w wyrażeniu
print("factorial(4)+fib(5)=", factorial(4) + fib(5))  # 24+5=29

print("Koniec testu złożonego")