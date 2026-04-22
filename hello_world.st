# =================================================================
# TEST ZAAWANSOWANYCH FUNKCJI KOMPILATORA SPACIAL TURTLE
# =================================================================

# 1. Test mocnego typowania i przestrzeni globalnej
float a
a = 2
int walls_drawn = 0
pen down

# 2. Test pętli 'for' (tworzy swój własny lokalny zasięg!)
for (int i = 0; i < 4; i = i + 1) {
    
    # Test bezpiecznego rysowania płaszczyzny w pętli
    face {
        for (int j = 0; j < 4; j = j + 1) {
            move a
            turnY 90
        }
    }
    
    # Zaginamy sześcian
    move a
    turnX -90
    
    # 3. TEST ZASIĘGÓW (parent::)
    # Zmienna i jest lokalna, ale walls_drawn jest globalne.
    # Używamy parent:: aby wyjść z bańki pętli 'for' i zaktualizować zmienną globalną!
    walls_drawn = walls_drawn + 1
}

# --- ZAMYKAMY SZEŚCIAN (LEWY I PRAWY BOK) ---

turnZ 90
face {
    for (int k = 0; k < 4; k = k + 1) {
        move a
        turnY 90
    }
}
turnZ 90

pen up
turnY -90
move a
turnY 90
pen down

turnZ -90
face {
    for (int l = 0; l < 4; l = l + 1) {
        move a
        turnY 90
    }
}

# 4. Test operacji logicznych, porównywania typów i instrukcji IF
bool is_finished = walls_drawn == 4

if (is_finished) {
    # Odjeżdżamy żółwiem na koniec, żeby ładnie odsłonić wygenerowaną bryłę
    pen up
    turnZ 90
    turnY -90
    move 3
    turnY 180
}