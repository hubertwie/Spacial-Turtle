int x = 10

for (int i = 0; i < 2; i = i + 1) {
    int x = 20

    for (int j = 0; j < 2; j = j + 1) {
        int x = 30
        x = x + 100
        parent::x = parent::x + 100
        parent::parent::x = parent::parent::x + 100
    }
}

bool sukces = x == 410

if (sukces) {
    pen down
    move 5
} else {
    pen down
    turnY 90
    move 1
}