import sys
import os
from antlr4 import FileStream, CommonTokenStream, InputStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener

from SpacialTurtleLexer import SpacialTurtleLexer
from SpacialTurtleParser import SpacialTurtleParser
from interpreter import SpacialTurtleInterpreter, TurtleVisualization
from turtle3d import Turtle3D
from symbols import SymbolTable
from firstpass import FirstPassListener


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.real_errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Błąd składni w linii {line}, kol. {column}: {msg}"
        self.errors.append(error_msg)

        symbol_text = offendingSymbol.text if offendingSymbol else ""
        if symbol_text != "<EOF>":
            self.real_errors.append(error_msg)


def run_repl(interpreter, app):
    print("Spacial Turtle REPL. Type 'quit' to exit, 'export' to save mesh.")
    print("Wprowadzaj kod – REPL teraz sprawdza błędy linijka po linijce na bieżąco!")

    buffer = []
    brace_count = 0

    while True:
        try:
            prompt = "... " if buffer else "> "
            line = input(prompt).rstrip()
        except EOFError:
            break

        if line == "quit":
            break
        if not line and not buffer:
            continue

        buffer.append(line)
        for ch in line:
            if ch == '{':
                brace_count += 1
            elif ch == '}':
                brace_count -= 1

        if brace_count < 0:
            msg = "Błąd: Zamknięto za dużo klamerek '}'! Zaczynamy od nowa."
            print(msg)
            app.status.config(text=msg)
            buffer = []
            brace_count = 0
            continue

        full_input = "\n".join(buffer)
        input_stream = InputStream(full_input)
        lexer = SpacialTurtleLexer(input_stream)
        lexer.removeErrorListeners()

        stream = CommonTokenStream(lexer)
        parser = SpacialTurtleParser(stream)
        parser.removeErrorListeners()

        error_listener = SyntaxErrorListener()
        parser.addErrorListener(error_listener)

        tree = parser.program()

        if error_listener.real_errors:
            msg = "Błąd składniowy wyłapany w locie:\n" + "\n".join(error_listener.real_errors)
            print(msg)
            app.status.config(text=msg[:200]) 
            buffer = []
            brace_count = 0
            continue

        if brace_count == 0 and buffer:
            print(f"\n--- WYKONUJĘ: ---\n{full_input}\n------------------")
            try:
                first_pass = FirstPassListener(interpreter.symbol_table)
                walker = ParseTreeWalker()
                walker.walk(first_pass, tree)

                interpreter.execute_program(tree, app)
                app.update_visualization(interpreter.turtle)
                print("wykonano :)")
                app.status.config(text="Program executed successfully")
            except Exception as e:
                error_msg = f"Błąd wykonania (Runtime): {e}"
                print(error_msg)
                app.status.config(text=error_msg[:200])
            buffer = []
            brace_count = 0
def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print(f"File {filename} not found")
            sys.exit(1)
        input_stream = FileStream(filename, encoding='utf-8')
        lexer = SpacialTurtleLexer(input_stream)
        lexer.removeErrorListeners() 
        stream = CommonTokenStream(lexer)
        parser = SpacialTurtleParser(stream)
        parser.removeErrorListeners()
        
        syntax_listener = SyntaxErrorListener()
        parser.addErrorListener(syntax_listener)
        
        tree = parser.program()
        
        if syntax_listener.real_errors:
            for err in syntax_listener.real_errors:
                print(err)
            sys.exit(1)
        
        symbol_table = SymbolTable()
        first_pass = FirstPassListener(symbol_table)
        walker = ParseTreeWalker()
        try:
            walker.walk(first_pass, tree)
        except Exception as e:
            print(e)
            sys.exit(1)
        
        turtle = Turtle3D()
        interpreter = SpacialTurtleInterpreter(turtle, symbol_table)
        app = TurtleVisualization(interpreter)
        app.load_program(tree)
        app.after(500, app.start_animation)
        app.mainloop()
    else:
        turtle = Turtle3D()
        symbol_table = SymbolTable()
        interpreter = SpacialTurtleInterpreter(turtle, symbol_table)
        app = TurtleVisualization(interpreter)
        app.after(100, lambda: run_repl(interpreter, app))
        app.mainloop()

if __name__ == "__main__":
    main()