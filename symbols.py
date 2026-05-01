from enum import Enum
from typing import Dict, List, Tuple

class Type(Enum):
    INT = 1
    FLOAT = 2
    BOOL = 3
    VOID = 4
    STRING = 5

class Symbol:
    def __init__(self, name: str, typ: Type, line: int, column: int):
        self.name = name
        self.type = typ
        self.line = line
        self.column = column

class FunctionSymbol:
    def __init__(self, name: str, params: List[Tuple[str, Type]], return_type: Type, line: int, column: int):
        self.name = name
        self.params = params
        self.return_type = return_type
        self.line = line
        self.column = column

class SymbolTable:
    def __init__(self):
        self.scopes: List[Dict[str, Symbol]] = [{}]
        self.functions: Dict[str, FunctionSymbol] = {}

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        self.scopes.pop()

    def add_variable(self, name: str, typ: Type, line: int, col: int):
        current_scope = self.scopes[-1]
        if name in current_scope:
            raise Exception(f"Błąd (Linia {line}): Zmienna '{name}' została już zadeklarowana w tym samym bloku (w linii {current_scope[name].line})!")
        current_scope[name] = Symbol(name, typ, line, col)

    def get_variable(self, name: str, line: int, col: int) -> Symbol:
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Błąd (Linia {line}): Użycie niezadeklarowanej zmiennej '{name}'!")

    def add_function(self, func: FunctionSymbol):
        if func.name in self.functions:
            raise Exception(f"Błąd (Linia {func.line}): Funkcja '{func.name}' już istnieje!")
        self.functions[func.name] = func

    def get_function(self, name: str, line: int, col: int) -> FunctionSymbol:
        if name not in self.functions:
            raise Exception(f"Błąd (Linia {line}): Wywołanie nieznanej funkcji '{name}'!")
        return self.functions[name]