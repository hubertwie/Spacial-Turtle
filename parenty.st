# =========================================================
# TEST ZAGNIEŻDŻONYCH PĘTLI I WIELOKROTNEGO PARENT::
# =========================================================

int x = 10  # Zmienna globalna (poziom 0)

for (int i = 0; i < 2; i = i + 1) {
    
    # Przesłaniamy globalne x
    int x = 20  # Zmienna lokalna pętli zewnętrznej (poziom -1)

    for (int j = 0; j < 2; j = j + 1) {
        
        # Przesłaniamy oba wyższe x
        int x = 30  # Zmienna lokalna pętli wewnętrznej (poziom -2)

        # ----------------------------------------------------
        # W TYM MOMENCIE W PAMIĘCI SĄ 3 RÓŻNE ZMIENNE O NAZWIE 'x'!
        # ----------------------------------------------------
        
        # 1. Samo 'x' zmienia najbardziej lokalne (30 -> 130)
        x = x + 100
        
        # 2. 'parent::x' przeskakuje jedną bańkę wyżej (20 -> 120)
        parent::x = parent::x + 100
        
        # 3. 'parent::parent::x' dociera aż do zmiennej globalnej! (10 -> 110)
        parent::parent::x = parent::parent::x + 100
    }
}

# Po zakończeniu obu pętli, wszystkie lokalne zmienne 'x' znikają.
# Zostaje tylko globalne 'x'.

# Obliczenia: Zmienna globalna zaczęła od 10. 
# Wewnętrzna pętla wykonała się 4 razy (2x2).
# Za każdym razem globalne x dostało +100.
# Spodziewany wynik globalnego x: 10 + 400 = 410.

# Sprawdźmy to!
bool sukces = x == 410

if (sukces) {
    pen down
    move 5
} else {
    # Gdyby stosy pamięci źle działały, żółw narysowałby kreskę w bok.
    pen down
    turnY 90
    move 1
}