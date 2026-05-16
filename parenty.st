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




int global_counter
global_counter = 0
float step_size = 3.5

pen down

for (int i = 0; i < 4; i = i + 1) {
    move step_size
    turnY 90
    global_counter = global_counter + 1
}

pen up
turnY -90
move 5
turnY 90
pen down

bool is_square_done = global_counter == 4
bool is_step_big = step_size > 5.0

bool test_and = is_square_done and is_step_big 

bool test_or = is_square_done or is_step_big

bool test_not = not test_or


if (test_or) {
    for (int k = 0; k < 3; k = k + 1) {
        move 4.0
        turnY 120
    }
    
} else {
    turnX 90
    move 10.0
}

bool crash_test = 5.0 == true