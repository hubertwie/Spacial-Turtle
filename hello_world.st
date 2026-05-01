float a
a = 2
int walls_drawn = 0
pen down

for (int i = 0; i < 4; i = i + 1) {
    face {
        for (int j = 0; j < 4; j = j + 1) {
            move a
            turnY 90
        }
    }
    
    move a
    turnX -90
    
    walls_drawn = walls_drawn + 1
}

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

bool is_finished = walls_drawn == 4

if (is_finished) {
    pen up
    turnZ 90
    turnY -90
    move 3
    turnY 180
}