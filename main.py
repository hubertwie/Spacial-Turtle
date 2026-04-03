import sys
import os
from antlr4 import FileStream, CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from SpacialTurtleLexer import SpacialTurtleLexer
from SpacialTurtleParser import SpacialTurtleParser
from interpreter import SpacialTurtleInterpreter, TurtleVisualization
from turtle3d import Turtle3D


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Syntax error at line {line}, column {column}: {msg}"
        self.errors.append(error_msg)
        print(error_msg)


def run_repl(interpreter, app):
    print("Spacial Turtle REPL. Type 'quit' to exit, 'export' to save mesh.")
    print("Wpisz 'face {' aby rozpocząć płaszczyznę, i '}' aby ją zamknąć i pokolorować.")
    
    while True:
        try:
            # Zmieniamy znak zachęty, jeśli żółw jest w trakcie rysowania płaszczyzny
            prompt = "... " if interpreter.turtle.in_face else "> "
            line = input(prompt).strip()
        except EOFError:
            break
            
        if line == "quit" and not interpreter.turtle.in_face:
            break
            
        if not line:
            continue
            
        # 1. Ręczne przechwycenie otwarcia bloku
        if line == "face {" or line == "face{":
            interpreter.turtle.begin_face()
            app.update_visualization(interpreter.turtle)
            continue
            
        # 2. Ręczne przechwycenie zamknięcia bloku
        if line == "}":
            if interpreter.turtle.in_face:
                interpreter.turtle.end_face()
                app.update_visualization(interpreter.turtle)
            else:
                print("Błąd: Próbujesz zamknąć płaszczyznę, ale żadna nie została otwarta!")
            continue
            
        # 3. Każda inna komenda (move, turn) jest od razu kompilowana i rysowana!
        try:
            input_stream = InputStream(line)
            lexer = SpacialTurtleLexer(input_stream)
            lexer.removeErrorListeners()
            error_listener = SyntaxErrorListener()
            lexer.addErrorListener(error_listener)
            stream = CommonTokenStream(lexer)
            parser = SpacialTurtleParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            
            # Traktujemy pojedynczą linijkę jako kompletny program
            tree = parser.program()
            
            if error_listener.errors:
                print("Syntax errors found. Not executing.")
                continue
                
            # Wykonujemy ruch
            interpreter.execute_program(tree, app)
            # Aktualizujemy grafikę NATYCHMIAST po wciśnięciu Enter!
            app.update_visualization(interpreter.turtle)
            
        except Exception as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found")
            sys.exit(1)
        try:
            input_stream = FileStream(filename)
            lexer = SpacialTurtleLexer(input_stream)
            error_listener = SyntaxErrorListener()
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            stream = CommonTokenStream(lexer)
            parser = SpacialTurtleParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            tree = parser.program()
            if error_listener.errors:
                print(f"\n{len(error_listener.errors)} syntax error(s). Cannot execute.")
                sys.exit(1)

            turtle = Turtle3D()
            interpreter = SpacialTurtleInterpreter(turtle)
            app = TurtleVisualization(interpreter)

            # Load program for animation
            app.load_program(tree)

            print(f"Loaded '{filename}'. Press Play to start animation.")
            app.mainloop()

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        # REPL mode
        turtle = Turtle3D()
        interpreter = SpacialTurtleInterpreter(turtle)
        app = TurtleVisualization(interpreter)
        app.after(100, lambda: run_repl(interpreter, app))
        app.mainloop()


if __name__ == "__main__":
    main()