# =========================================================
# TEST KOMPLEKSOWY (ZASIĘGI, LOGIKA, IF/ELSE)
# =========================================================

# 1. Test inicjalizacji i osobnego przypisania
int global_counter
global_counter = 0
float step_size = 3.5

pen down

# 2. Test pętli FOR i poprawionych zasięgów (BEZ parent::)
for (int i = 0; i < 4; i = i + 1) {
    move step_size
    turnY 90
    
    # Skoro poprawiliśmy klamerki i przypisania, 
    # to poniższa linijka musi zaktualizować zmienną globalną!
    global_counter = global_counter + 1
}

# Żółw odjeżdża na bok, by narysować coś nowego
pen up
turnY -90
move 5
turnY 90
pen down

# 3. Test operatorów logicznych i porównań
bool is_square_done = global_counter == 4
bool is_step_big = step_size > 5.0

# test_and musi być FALSE (bo step_size to 3.5)
bool test_and = is_square_done and is_step_big 

# test_or musi być TRUE (bo is_square_done to prawda)
bool test_or = is_square_done or is_step_big

# test_not musi być FALSE (bo test_or to prawda)
bool test_not = not test_or


# 4. Test instrukcji IF oraz ELSE
# Sprawdzamy nasz test_or (który jest TRUE). 
# Żółw POWINIEN wejść do IF i narysować trójkąt.
if (test_or) {
    
    # Rysujemy trójkąt z użyciem własnej, nowej zmiennej
    for (int k = 0; k < 3; k = k + 1) {
        move 4.0
        turnY 120
    }
    
} else {
    
    # Gdyby test_or był FALSE (lub logika była zepsuta), 
    # żółw wszedłby tutaj i narysował długą kreskę w górę.
    turnX 90
    move 10.0
}

# 5. ODKOMENTUJ LINIJKĘ PONIŻEJ, ABY ZOBACZYĆ BŁĄD TYPÓW (Float vs Bool)
# bool crash_test = 5.0 == true