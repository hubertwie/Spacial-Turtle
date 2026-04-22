# Spacial Turtle 3D

Spacial Turtle is a programming language and tool for creating 3D graphics. It is based on "Turtle Graphics" but expanded into 3D space with a custom compiler.

## Key Features

**3D Movement:** Control the turtle in XYZ space using commands like move, turnX, turnY, and turnZ.

**Simple Types:** Supports int, float, and bool with type checking.

**Variable Scopes:** Handles local and global variables. Use the parent:: keyword to update variables in outer blocks.

**Creating Shapes:** Use the face { ... } block to define 3D surfaces and objects.

**Export to .OBJ:** You can save your 3D models as .obj files to use them in other 3D software.

**Live Preview:** An interactive console (REPL) lets you run code and see the results immediately.

## How it Works

The project is divided into a few main parts:

**Grammar:** Defined using ANTLR4 (SpacialTurtle.g4).

**Symbol Table:** Manages variables and ensures they are used correctly.

**Interpreter:** Uses the Visitor pattern to execute the code.

**3D Engine:** Handles 3D math and shows the visualization using Tkinter.

## Code Example

```C
# Draw a simple 3D shape
float a = 2.0
int walls_drawn = 0

for (int i = 0; i < 4; i = i + 1) {
    face {
        for (int j = 0; j < 4; j = j + 1) {
            move a
            turnY 90
        }
    }
    move a
    turnX -90
    parent::walls_drawn = parent::walls_drawn + 1
}
export
```

## Requirements

- Python 3.x
- antlr4-python3-runtime
- numpy
- tkinter