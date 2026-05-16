import math
import tkinter as tk
from tkinter import ttk
from typing import Dict, Any, List, Tuple, Union
import numpy as np

from turtle3d import Turtle3D, Vertex
from SpacialTurtleVisitor import SpacialTurtleVisitor
from SpacialTurtleParser import SpacialTurtleParser
from symbols import SymbolTable, Type, FunctionSymbol


class BreakException(Exception):
    """Wyjątek przerywający pętlę (break)."""
    pass

class ContinueException(Exception):
    """Wyjątek powodujący przejście do następnej iteracji (continue)."""
    pass

class ReturnException(Exception):
    """Wyjątek powodujący natychmiastowe wyjście z funkcji."""
    pass


class SpacialTurtleInterpreter(SpacialTurtleVisitor):
    """
    Interpreter języka Spacial Turtle.
    Odwiedza drzewo parsowania i wykonuje instrukcje,
    aktualizując stan żółwia 3D oraz zmienne.
    """

    def __init__(self, turtle: Turtle3D, symbol_table: SymbolTable):
        """
        Inicjalizuje interpreter.

        :param turtle: Obiekt żółwia 3D, który będzie sterowany.
        :type turtle: Turtle3D
        :param symbol_table: Tablica symboli z informacjami o zmiennych i funkcjach.
        :type symbol_table: SymbolTable
        """
        self.turtle = turtle
        self.symbol_table = symbol_table
        self.current_return_value = None
        self.in_function = False
        self.user_functions = {}
        self._inside_loop = False          
        self.return_encountered = False

    def execute_program(self, tree, root_window=None):
        """
        Uruchamia wykonanie programu na podstawie drzewa parse.

        :param tree: Główny węzeł drzewa parse (program).
        :param root_window: Opcjonalne okno główne do aktualizacji wizualizacji.
        :type root_window: TurtleVisualization lub None
        """
        try:
            self.visit(tree)
            if root_window:
                root_window.update_visualization(self.turtle)
        except Exception as e:
            raise

    def error(self, ctx, msg):
        """
        Zgłasza błąd wykonania z lokalizacją (linia, kolumna) na podstawie kontekstu.

        :param ctx: Kontekst ANTLR (węzeł drzewa), z którego pobierana jest pozycja.
        :param msg: Komunikat błędu.
        :raises RuntimeError: Zawsze, z sformatowanym komunikatem.
        """
        line = ctx.start.line
        col = ctx.start.column
        raise RuntimeError(f"Linia {line}, kol. {col}: {msg}")

    def error_at(self, line, col, msg):
        """
        Zgłasza błąd wykonania z podaną linią i kolumną.

        :param line: Numer linii.
        :type line: int
        :param col: Numer kolumny.
        :type col: int
        :param msg: Komunikat błędu.
        :raises RuntimeError: Zawsze.
        """
        raise RuntimeError(f"Linia {line}, kol. {col}: {msg}")

    def get_variable(self, ctx, text: str) -> Tuple[Any, Type]:
        """
        Odczytuje wartość i typ zmiennej na podstawie jej nazwy (z uwzględnieniem parent::).

        :param ctx: Kontekst ANTLR (do raportowania błędów).
        :param text: Nazwa zmiennej, może zawierać przedrostki 'parent::'.
        :type text: str
        :return: Para (wartość, typ).
        :rtype: Tuple[Any, Type]
        :raises RuntimeError: Gdy zmienna nie istnieje lub parent:: wychodzi poza zakres.
        """
        parent_levels = text.count('parent::')
        var_name = text.split('::')[-1]

        if parent_levels > 0:
            target_scope_idx = -1 - parent_levels
            if self.turtle.scope_stack:
                if abs(target_scope_idx) <= len(self.turtle.scope_stack):
                    scope = self.turtle.scope_stack[target_scope_idx]
                    if var_name in scope:
                        return scope[var_name]
                elif abs(target_scope_idx) == len(self.turtle.scope_stack) + 1:
                    if var_name in self.turtle.global_vars:
                        return self.turtle.global_vars[var_name]
            self.error(ctx, f"Zbyt wiele 'parent::'. Zmienna '{var_name}' nie istnieje na tym poziomie.")
        else:
            for scope in reversed(self.turtle.scope_stack):
                if var_name in scope:
                    return scope[var_name]
            if var_name in self.turtle.global_vars:
                return self.turtle.global_vars[var_name]
            self.error(ctx, f"Zmienna '{var_name}' nie została zadeklarowana!")

    def set_variable(self, ctx, text: str, value: Any, value_type: Type):
        """
        Zapisuje wartość do istniejącej zmiennej (z uwzględnieniem parent::).

        :param ctx: Kontekst ANTLR.
        :param text: Nazwa zmiennej (może z parent::).
        :param value: Wartość do zapisania.
        :param value_type: Typ wartości.
        :type value_type: Type
        :raises RuntimeError: Gdy zmienna nie istnieje lub typ niezgodny.
        """
        parent_levels = text.count('parent::')
        var_name = text.split('::')[-1]

        if parent_levels > 0:
            target_scope_idx = -1 - parent_levels
            if self.turtle.scope_stack:
                if abs(target_scope_idx) <= len(self.turtle.scope_stack):
                    scope = self.turtle.scope_stack[target_scope_idx]
                    if var_name in scope:
                        old_val, old_type = scope[var_name]
                        self._check_type_compatibility(ctx, value_type, old_type, text, "przypisaniu")
                        if old_type == Type.FLOAT and value_type == Type.INT:
                            value = float(value)
                        elif old_type == Type.INT and value_type == Type.FLOAT:
                            value = int(value)
                        scope[var_name] = (value, old_type)
                        return
                elif abs(target_scope_idx) == len(self.turtle.scope_stack) + 1:
                    if var_name in self.turtle.global_vars:
                        old_val, old_type = self.turtle.global_vars[var_name]
                        self._check_type_compatibility(ctx, value_type, old_type, text, "przypisaniu")
                        if old_type == Type.FLOAT and value_type == Type.INT:
                            value = float(value)
                        elif old_type == Type.INT and value_type == Type.FLOAT:
                            value = int(value)
                        self.turtle.global_vars[var_name] = (value, old_type)
                        return
            self.error(ctx, f"Zbyt wiele 'parent::' dla zmiennej '{var_name}'")
        else:
            for scope in reversed(self.turtle.scope_stack):
                if var_name in scope:
                    old_val, old_type = scope[var_name]
                    self._check_type_compatibility(ctx, value_type, old_type, text, "przypisaniu")
                    if old_type == Type.FLOAT and value_type == Type.INT:
                        value = float(value)
                    elif old_type == Type.INT and value_type == Type.FLOAT:
                        value = int(value)
                    scope[var_name] = (value, old_type)
                    return
            if var_name in self.turtle.global_vars:
                old_val, old_type = self.turtle.global_vars[var_name]
                self._check_type_compatibility(ctx, value_type, old_type, text, "przypisaniu")
                if old_type == Type.FLOAT and value_type == Type.INT:
                    value = float(value)
                elif old_type == Type.INT and value_type == Type.FLOAT:
                    value = int(value)
                self.turtle.global_vars[var_name] = (value, old_type)
                return
            self.error(ctx, f"Przypisanie do niezadeklarowanej zmiennej '{var_name}'")

    def declare_variable(self, ctx, name: str, declared_type: Type, initial_value: Any, initial_type: Type):
        """
        Deklaruje nową zmienną w bieżącym zakresie.

        :param ctx: Kontekst ANTLR.
        :param name: Nazwa zmiennej.
        :type name: str
        :param declared_type: Zadeklarowany typ zmiennej.
        :type declared_type: Type
        :param initial_value: Wartość początkowa (może być None).
        :param initial_type: Typ wartości początkowej (może być None).
        :type initial_type: Type
        """
        if initial_value is not None:
            self._check_type_compatibility(ctx, initial_type, declared_type, name, "inicjalizacji")
            if declared_type == Type.FLOAT and initial_type == Type.INT:
                initial_value = float(initial_value)
            elif declared_type == Type.INT and initial_type == Type.FLOAT:
                initial_value = int(initial_value)

        if initial_value is None:
            if declared_type == Type.INT:
                initial_value = 0
            elif declared_type == Type.FLOAT:
                initial_value = 0.0
            elif declared_type == Type.BOOL:
                initial_value = False
            else:
                initial_value = 0

        if self.turtle.scope_stack:
            self.turtle.scope_stack[-1][name] = (initial_value, declared_type)
        else:
            self.turtle.global_vars[name] = (initial_value, declared_type)

    def _check_type_compatibility(self, ctx, src_type: Type, dst_type: Type, name: str, operation: str):
        """
        Sprawdza zgodność typów przy przypisaniu/inicjalizacji. Dozwolona konwersja int↔float.

        :param ctx: Kontekst ANTLR.
        :param src_type: Typ źródłowy.
        :param dst_type: Typ docelowy.
        :param name: Nazwa zmiennej (do komunikatu).
        :param operation: Opis operacji ("przypisaniu", "inicjalizacji").
        :raises RuntimeError: Gdy typy są niezgodne.
        """
        if src_type == dst_type:
            return
        if src_type == Type.INT and dst_type == Type.FLOAT:
            return
        if src_type == Type.FLOAT and dst_type == Type.INT:
            return
        self.error(ctx, f"Nie można wykonać {operation} zmiennej '{name}': typ {src_type.name} nie jest zgodny z {dst_type.name}")

    def get_python_type(self, val) -> Type:
        """
        Mapuje typ wartości Pythona na enum Type.

        :param val: Wartość w Pythonie.
        :return: Odpowiedni typ enum.
        :rtype: Type
        """
        if isinstance(val, bool):
            return Type.BOOL
        if isinstance(val, float):
            return Type.FLOAT
        if isinstance(val, int):
            return Type.INT
        if isinstance(val, str):
            return Type.STRING
        return Type.VOID

    def is_number(self, typ):
        """
        Sprawdza, czy typ jest numeryczny (int lub float).

        :param typ: Typ do sprawdzenia.
        :type typ: Type
        :return: True jeśli typ to INT lub FLOAT.
        :rtype: bool
        """
        return typ in [Type.INT, Type.FLOAT]

    def visitExpr(self, ctx):
        """Odwiedza wyrażenie (przekazuje do logicalOrExpr)."""
        return self.visit(ctx.logicalOrExpr())

    def visitLogicalOrExpr(self, ctx):
        """
        Obsługuje operator logiczny OR (krótkie wyłączanie).
        Zwraca (wartość, typ) – typ zawsze BOOL.
        """
        left_val, left_type = self.visit(ctx.logicalAndExpr(0))
        for i in range(1, len(ctx.logicalAndExpr())):
            right_val, right_type = self.visit(ctx.logicalAndExpr(i))
            if left_type != Type.BOOL or right_type != Type.BOOL:
                self.error(ctx, "Operator 'or' wymaga typów bool!")
            left_val = left_val or right_val
        return left_val, left_type

    def visitLogicalAndExpr(self, ctx):
        """
        Obsługuje operator logiczny AND (krótkie wyłączanie).
        Zwraca (wartość, typ) – typ zawsze BOOL.
        """
        left_val, left_type = self.visit(ctx.comparisonExpr(0))
        for i in range(1, len(ctx.comparisonExpr())):
            right_val, right_type = self.visit(ctx.comparisonExpr(i))
            if left_type != Type.BOOL or right_type != Type.BOOL:
                self.error(ctx, "Operator 'and' wymaga typów bool!")
            left_val = left_val and right_val
        return left_val, left_type

    def visitComparisonExpr(self, ctx):
        """
        Obsługuje operatory porównania (<, >, <=, >=, ==, !=).
        Zwraca (wartość logiczna, Type.BOOL).
        """
        left_val, left_type = self.visit(ctx.additiveExpr(0))
        if len(ctx.additiveExpr()) == 1:
            return left_val, left_type

        op = ctx.getChild(1).getText()
        right_val, right_type = self.visit(ctx.additiveExpr(1))

        if op in ['<', '>', '<=', '>=']:
            if not self.is_number(left_type) or not self.is_number(right_type):
                self.error(ctx, "Operatory relacyjne wymagają typów liczbowych (int/float).")
        if op in ['==', '!=']:
            if self.is_number(left_type) != self.is_number(right_type):
                self.error(ctx, "Nie można porównywać typu liczbowego z logicznym!")

        if op == '==': return left_val == right_val, Type.BOOL
        if op == '!=': return left_val != right_val, Type.BOOL
        if op == '<': return left_val < right_val, Type.BOOL
        if op == '>': return left_val > right_val, Type.BOOL
        if op == '<=': return left_val <= right_val, Type.BOOL
        if op == '>=': return left_val >= right_val, Type.BOOL

    def visitAdditiveExpr(self, ctx):
        """
        Obsługuje dodawanie i odejmowanie (+ i -).
        Zwraca (wynik, typ) – typ FLOAT jeśli którykolwiek operand był FLOAT, inaczej INT.
        """
        val, typ = self.visit(ctx.multiplicativeExpr(0))
        for i in range(1, len(ctx.multiplicativeExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right_val, right_type = self.visit(ctx.multiplicativeExpr(i))
            if not self.is_number(typ) or not self.is_number(right_type):
                self.error(ctx, "Dodawanie/Odejmowanie wymaga liczb.")

            if op == '+':
                val += right_val
            else:
                val -= right_val

            if typ == Type.FLOAT or right_type == Type.FLOAT:
                typ = Type.FLOAT
            else:
                typ = Type.INT
        return val, typ

    def visitMultiplicativeExpr(self, ctx):
        """
        Obsługuje mnożenie (*), dzielenie rzeczywiste (/), dzielenie całkowite (//) i modulo (%).
        Zwraca (wynik, typ) – odpowiednio FLOAT dla /, INT dla // i % oraz dla * w zależności od operandów.
        """
        val, typ = self.visit(ctx.unaryExpr(0))
        for i in range(1, len(ctx.unaryExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right_val, right_type = self.visit(ctx.unaryExpr(i))
            if not self.is_number(typ) or not self.is_number(right_type):
                self.error(ctx, "Mnożenie/Dzielenie wymaga liczb.")

            if op == '*':
                val *= right_val
                if typ == Type.FLOAT or right_type == Type.FLOAT:
                    typ = Type.FLOAT
                else:
                    typ = Type.INT
            elif op == '/':
                if right_val == 0:
                    self.error(ctx, "Dzielenie przez zero!")
                val = val / right_val
                typ = Type.FLOAT
            elif op == '//':
                if right_val == 0:
                    self.error(ctx, "Dzielenie przez zero!")
                val = val // right_val if isinstance(val, int) and isinstance(right_val, int) else int(val / right_val)
                typ = Type.INT
            elif op == '%':
                if right_val == 0:
                    self.error(ctx, "Modulo przez zero!")
                val = val % right_val
                typ = Type.INT
        return val, typ

    def visitUnaryExpr(self, ctx):
        """
        Obsługuje operatory unarne: +, -, not.
        Zwraca (wynik, typ).
        """
        if ctx.PLUS():
            val, typ = self.visit(ctx.unaryExpr())
            if not self.is_number(typ):
                self.error(ctx, "Znak '+' wymaga liczby.")
            return val, typ
        if ctx.MINUS():
            val, typ = self.visit(ctx.unaryExpr())
            if not self.is_number(typ):
                self.error(ctx, "Znak '-' wymaga liczby.")
            return -val, typ
        if ctx.NOT():
            val, typ = self.visit(ctx.unaryExpr())
            if typ != Type.BOOL:
                self.error(ctx, "NOT wymaga typu bool.")
            return not val, Type.BOOL
        return self.visit(ctx.primaryExpr())

    def visitPrimaryExpr(self, ctx):
        """
        Obsługuje wyrażenia podstawowe: stałe (liczby, napisy, true/false),
        zmienne, wywołania funkcji, nawiasy, rzutowania typów.
        """
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1], Type.STRING
        if ctx.NUMBER():
            txt = ctx.NUMBER().getText()
            if '.' in txt:
                return float(txt), Type.FLOAT
            else:
                return int(txt), Type.INT
        if ctx.TRUE(): return True, Type.BOOL
        if ctx.FALSE(): return False, Type.BOOL
        if ctx.variableRef():
            ref_name = ctx.variableRef().getText()
            val, typ = self.get_variable(ctx, ref_name)
            return val, typ
        if ctx.LPAREN():
            return self.visit(ctx.expr())
        if ctx.funcCall():
            return self.visitFuncCall(ctx.funcCall())
        if ctx.varType():
            val, typ = self.visit(ctx.expr())
            target_type_str = ctx.varType().getText()
            if target_type_str == 'int':
                return int(val), Type.INT
            elif target_type_str == 'float':
                return float(val), Type.FLOAT
            elif target_type_str == 'bool':
                return bool(val), Type.BOOL
        self.error(ctx, "Nieznane wyrażenie.")

    def ui_step(self):
        """
        Aktualizuje wizualizację (jeśli aplikacja istnieje) i obsługuje tryby
        odtwarzania (play, pause, step) w celu synchronizacji z interfejsem.
        """
        if hasattr(self, 'app') and self.app and getattr(self.app, 'is_running', False):
            try:
                self.app.update_visualization(self.turtle)
                if self.app.run_mode == "pause":
                    self.app.wait_variable(self.app.step_var)
                if self.app.run_mode == "step":
                    self.app.run_mode = "pause"
                elif self.app.run_mode == "play":
                    self.app.update()
                    import time
                    time.sleep(self.app.delay_ms / 1000.0)
            except Exception:
                pass

    def visitDeclaration(self, ctx):
        """
        Obsługuje deklarację zmiennej. W razie błędu (np. niezgodność typów)
        usuwa zmienną z tablicy symboli statycznych.
        """
        name = ctx.ID().getText()
        type_str = ctx.varType().getText()
        declared_type = {
            'int': Type.INT,
            'float': Type.FLOAT,
            'bool': Type.BOOL,
            'string': Type.STRING
        }[type_str]
        init_val = None
        init_type = None
        if ctx.expr():
            init_val, init_type = self.visit(ctx.expr())
        try:
            self.declare_variable(ctx, name, declared_type, init_val, init_type)
        except Exception as e:
            self.symbol_table.remove_variable(name)
            raise e
        self.ui_step()

    def visitAssignStmt(self, ctx):
        """Obsługuje przypisanie do zmiennej."""
        ref_text = ctx.variableRef().getText()
        val, typ = self.visit(ctx.expr())
        self.set_variable(ctx, ref_text, val, typ)
        self.ui_step()

    def visitMoveCmd(self, ctx):
        """Wykonuje komendę move – przesuwa żółwia o podaną odległość."""
        dist, typ = self.visit(ctx.expr())
        if not self.is_number(typ):
            self.error(ctx.expr(), "Dystans musi być liczbą!")
        self.turtle.move(dist)
        self.ui_step()

    def visitTurnCmd(self, ctx):
        """Wykonuje obrót żółwia wokół wybranej osi (lokalnej lub globalnej)."""
        angle, typ = self.visit(ctx.expr())
        if not self.is_number(typ):
            self.error(ctx.expr(), "Kąt obrotu musi być liczbą!")
        if ctx.TURNX():
            self.turtle.rotate_x(angle)
        elif ctx.TURNY():
            self.turtle.rotate_y(angle)
        elif ctx.TURNZ():
            self.turtle.rotate_z(angle)
        self.ui_step()

    def visitPenCmd(self, ctx):
        """Podnosi lub opuszcza pisak (pen up/down). Niedozwolone wewnątrz face."""
        if self.turtle.in_face:
            self.error(ctx, "Nie można zmieniać pisaka wewnątrz płaszczyzny (face)!")
        if ctx.UP():
            self.turtle.pen_up()
        else:
            self.turtle.pen_down()

    def visitFaceBlock(self, ctx):
        """Rozpoczyna i kończy definiowanie ściany (face)."""
        self.turtle.begin_face()
        self.visitChildren(ctx)
        self.turtle.end_face()

    def visitExportCmd(self, ctx):
        """Eksportuje obecną siatkę do pliku OBJ."""
        self.turtle.export_obj("output.obj")
        print("Wyeksportowano do output.obj")

    def visitPrintStmt(self, ctx):
        """Wypisuje wartości wyrażeń na konsolę (z konwersją bool na true/false)."""
        args = []
        if ctx.expr():
            for expr_ctx in ctx.expr():
                val, typ = self.visit(expr_ctx)
                if typ == Type.BOOL:
                    val = "true" if val else "false"
                args.append(str(val))
        print(" ".join(args))
        self.ui_step()
    
    def visitExprStmt(self, ctx):
        """
        Obsługuje instrukcję będącą samym wyrażeniem (np. 5, a+b, +10).
        Próbuje je obliczyć, ale ignoruje błędy o niezadeklarowanych zmiennych.
        Dzięki temu program nie przerywa działania.
        """
        try:
            self.visit(ctx.expr())
        except RuntimeError as e:
            if "nie została zadeklarowana" in str(e):
                pass
            else:
                raise

    def visitBlock(self, ctx):
        """Wykonuje blok instrukcji (z klamrami lub pojedynczą instrukcję)."""
        if ctx.getChild(0).getText() == '{':
            for stmt in ctx.statement():
                self.visit(stmt)
        else:
            self.visit(ctx.statement(0))

    def visitIfStmt(self, ctx):
        """Obsługuje instrukcję warunkową if-else (tworzy nowe zakresy dla gałęzi)."""
        cond, typ = self.visit(ctx.expr())
        if typ != Type.BOOL:
            self.error(ctx.expr(), "Warunek w IF musi być typu bool!")
        if cond:
            self.turtle.push_scope()
            self.visit(ctx.block(0))
            self.turtle.pop_scope()
        elif ctx.ELSE():
            self.turtle.push_scope()
            self.visit(ctx.block(1))
            self.turtle.pop_scope()

    def visitWhileStmt(self, ctx):
        """Obsługuje pętlę while (tworzy nowy zakres dla każdej iteracji)."""
        old_inside_loop = self._inside_loop
        self._inside_loop = True
        try:
            while True:
                cond, typ = self.visit(ctx.expr())
                if typ != Type.BOOL:
                    self.error(ctx.expr(), "Warunek w WHILE musi być typu bool!")
                if not cond:
                    break
                self.turtle.push_scope()
                try:
                    self.visit(ctx.block())
                except ContinueException:
                    pass
                except BreakException:
                    break
                finally:
                    self.turtle.pop_scope()
        finally:
            self._inside_loop = old_inside_loop

    def visitForStmt(self, ctx):
        """
        Obsługuje pętlę for (inicjalizacja, warunek, aktualizacja).
        Umożliwia break i continue.
        """
        self.turtle.push_scope()
        old_inside_loop = self._inside_loop
        self._inside_loop = True
        try:
            init_assign = None
            update_assign = None
            semicolon_count = 0
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if child.getText() == ';':
                    semicolon_count += 1
                elif type(child).__name__ == 'AssignStmtContext':
                    if semicolon_count == 0:
                        init_assign = child
                    elif semicolon_count == 2:
                        update_assign = child
            if ctx.declaration():
                self.visit(ctx.declaration())
            elif init_assign:
                self.visit(init_assign)

            while True:
                if ctx.expr():
                    cond, typ = self.visit(ctx.expr())
                    if typ != Type.BOOL:
                        self.error(ctx.expr(), "Warunek w FOR musi być typu bool!")
                    if not cond:
                        break

                self.turtle.push_scope()
                try:
                    self.visit(ctx.block())
                except ContinueException:
                    pass
                except BreakException:
                    break
                finally:
                    self.turtle.pop_scope()

                if update_assign:
                    self.visit(update_assign)
        finally:
            self._inside_loop = old_inside_loop
            self.turtle.pop_scope()

    def visitFuncDef(self, ctx):
        """Rejestruje definicję funkcji w słowniku user_functions."""
        name = ctx.ID().getText()
        self.user_functions[name] = ctx

    def visitFuncCall(self, ctx):
        """Wykonuje wywołanie funkcji: sprawdza argumenty, tworzy nowy zakres, obsługuje return."""
        func_name = ctx.ID().getText()
        try:
            func_sym = self.symbol_table.get_function(func_name, ctx.start.line, ctx.start.column)
        except Exception as e:
            self.error(ctx, str(e).split(":", 1)[-1].strip())
        func_ctx = self.user_functions.get(func_name)
        if not func_ctx:
            self.error(ctx, f"Funkcja '{func_name}' nie została zdefiniowana")

        arg_exprs = ctx.expr()
        if len(arg_exprs) != len(func_sym.params):
            self.error(ctx, f"Funkcja {func_name} oczekuje {len(func_sym.params)} argumentów, podano {len(arg_exprs)}")

        arg_values = []
        for i, arg_ctx in enumerate(arg_exprs):
            val, typ = self.visit(arg_ctx)
            param_name, param_type = func_sym.params[i]
            if typ != param_type:
                if typ == Type.INT and param_type == Type.FLOAT:
                    val = float(val)
                elif typ == Type.FLOAT and param_type == Type.INT:
                    val = int(val)
                else:
                    self.error(arg_ctx, f"Typ argumentu {i+1} funkcji {func_name}: oczekiwano {param_type.name}, podano {typ.name}")
            arg_values.append(val)

        self.turtle.push_scope()

        for (param_name, _), val in zip(func_sym.params, arg_values):
            actual_type = self.get_python_type(val)
            self.turtle.scope_stack[-1][param_name] = (val, actual_type)

        old_return = self.current_return_value
        old_in_function = self.in_function
        old_return_encountered = self.return_encountered
        old_inside_loop = self._inside_loop
        self.current_return_value = None
        self.in_function = True
        self.return_encountered = False
        self._inside_loop = False

        try:
            for stmt in func_ctx.statement():
                self.visit(stmt)
        except ReturnException:
            pass
        finally:
            self.turtle.pop_scope()
            return_val = self.current_return_value
            return_type = func_sym.return_type
            self.current_return_value = old_return
            self.in_function = old_in_function
            self.return_encountered = old_return_encountered
            self._inside_loop = old_inside_loop

        if return_type == Type.VOID:
            return None, Type.VOID
        else:
            if return_val is None:
                self.error(ctx, f"Funkcja {func_name} zadeklarowana jako zwracająca {return_type.name} nie zwróciła wartości")
            val_type = self.get_python_type(return_val)
            if val_type != return_type:
                if val_type == Type.INT and return_type == Type.FLOAT:
                    return_val = float(return_val)
                elif val_type == Type.FLOAT and return_type == Type.INT:
                    return_val = int(return_val)
                else:
                    self.error(ctx, f"Funkcja {func_name} zwróciła {val_type.name}, oczekiwano {return_type.name}")
            return return_val, return_type
    def visitReturnStmt(self, ctx):
        """Obsługuje instrukcję return – zapamiętuje wartość zwracaną i ustawia flagę."""
        if not self.in_function:
            self.error(ctx, "return poza funkcją")
        self.return_encountered = True
        if ctx.expr():
            val, typ = self.visit(ctx.expr())
            self.current_return_value = val
        else:
            self.current_return_value = None   # dla void
        raise ReturnException()
    def visitBreakStmt(self, ctx):
        """
        Instrukcja break – przerywa najbliższą pętlę.
        """
        if not self._inside_loop:
            self.error(ctx, "break poza pętlą")
        raise BreakException()

    def visitContinueStmt(self, ctx):
        """
        Instrukcja continue – przechodzi do następnej iteracji najbliższej pętli.
        """
        if not self._inside_loop:
            self.error(ctx, "continue poza pętlą")
        raise ContinueException()


class TurtleVisualization(tk.Tk):
    """
    Główne okno aplikacji z wizualizacją 3D żółwia.
    Zoptymalizowane pod kątem małych ekranów – kompaktowy panel sterowania.
    """

    def __init__(self, interpreter: SpacialTurtleInterpreter):
        super().__init__()
        self.interpreter = interpreter
        self.title("Spacial Turtle 3D Visualization")

        # Dopasowanie rozmiaru okna do ekranu
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        win_w = min(int(screen_w * 0.85), 1200)
        win_h = min(int(screen_h * 0.8), 900)
        self.geometry(f"{win_w}x{win_h}")
        self.minsize(800, 600)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Zmienne kamery
        self.camera_distance = 10.0
        self.camera_angle_x = 30.0
        self.camera_angle_y = 45.0
        self.camera_angle_z = 0.0
        self.pan_x = 0.0
        self.pan_y = 0.0
        self.camera_mode = "world"

        # Zmienne animacji
        self.statement_list = []
        self.current_index = 0
        self.animation_running = False
        self.delay_ms = 200
        self.step_var = tk.IntVar(value=0)
        self.run_mode = "stop"
        self.is_running = False
        self.program_tree = None

        # Główny obszar rysowania
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # --- Panel sterowania (zwarty, bez przewijania) ---
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

        # Styl dla mniejszych przycisków
        style = ttk.Style()
        style.configure("Small.TButton", font=("TkDefaultFont", 8), padding=2)

        # Ramka kamery (przyciski w siatce)
        camera_frame = ttk.LabelFrame(control_frame, text="Camera", padding=5)
        camera_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,5))

        # Przyciski kamery – lista (tekst, komenda)
        camera_buttons = [
            ("Rotate Left", lambda: self.rotate_camera(0, -10)),
            ("Rotate Right", lambda: self.rotate_camera(0, 10)),
            ("Rotate Up", lambda: self.rotate_camera(10, 0)),
            ("Rotate Down", lambda: self.rotate_camera(-10, 0)),
            ("Roll Left", lambda: self.roll_camera(-10)),
            ("Roll Right", lambda: self.roll_camera(10)),
            ("Zoom In", lambda: self.zoom_camera(-0.5)),
            ("Zoom Out", lambda: self.zoom_camera(0.5)),
            ("Pan Left", lambda: self.pan_camera(-20, 0)),
            ("Pan Right", lambda: self.pan_camera(20, 0)),
            ("Pan Up", lambda: self.pan_camera(0, -20)),
            ("Pan Down", lambda: self.pan_camera(0, 20)),
            ("Reset View", self.reset_camera),
            ("Cam: World", self.toggle_camera_mode),
        ]

        # Rozmieszczenie w siatce – 4 kolumny dla większości ekranów
        ncols = 4
        for idx, (text, cmd) in enumerate(camera_buttons):
            row = idx // ncols
            col = idx % ncols
            btn = ttk.Button(camera_frame, text=text, command=cmd, style="Small.TButton")
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="ew")
        for i in range(ncols):
            camera_frame.columnconfigure(i, weight=1)

        # Ramka animacji (prawa strona)
        anim_frame = ttk.LabelFrame(control_frame, text="Animation", padding=5)
        anim_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(5,0))

        # Przyciski Play/Pause/Step w jednym rzędzie
        btn_frame = ttk.Frame(anim_frame)
        btn_frame.pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Play", command=self.start_animation, style="Small.TButton", width=6).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Pause", command=self.stop_animation, style="Small.TButton", width=6).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Step", command=self.step_animation, style="Small.TButton", width=6).pack(side=tk.LEFT, padx=2)

        # Suwak prędkości – krótki
        speed_frame = ttk.Frame(anim_frame)
        speed_frame.pack(fill=tk.X, pady=2)
        ttk.Label(speed_frame, text="Speed (ms):", font=("TkDefaultFont", 8)).pack(side=tk.LEFT)
        self.speed_scale = ttk.Scale(speed_frame, from_=50, to=500, orient=tk.HORIZONTAL,
                                     command=self.set_delay, length=100)
        self.speed_scale.set(200)
        self.speed_scale.pack(side=tk.LEFT, padx=5)

        # Przycisk eksportu
        ttk.Button(anim_frame, text="Export OBJ", command=self.export_obj, style="Small.TButton").pack(fill=tk.X, pady=2)

        # Pasek statusu
        self.status = ttk.Label(self, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        # Inicjalny rysunek
        self.update_visualization(self.interpreter.turtle)

    def toggle_camera_mode(self):
        if self.camera_mode == "world":
            self.camera_mode = "turtle"
            self.camera_angle_x = self.interpreter.turtle.angle_x
            self.camera_angle_y = self.interpreter.turtle.angle_y
            self.camera_angle_z = self.interpreter.turtle.angle_z
            for child in self.children.values():
                if isinstance(child, ttk.Frame):
                    for f in child.winfo_children():
                        if isinstance(f, ttk.LabelFrame) and f.cget("text") == "Camera":
                            for btn in f.winfo_children():
                                if isinstance(btn, ttk.Button) and btn.cget("text") == "Cam: World":
                                    btn.config(text="Cam: Turtle")
                                    break
        else:
            self.camera_mode = "world"
            for child in self.children.values():
                if isinstance(child, ttk.Frame):
                    for f in child.winfo_children():
                        if isinstance(f, ttk.LabelFrame) and f.cget("text") == "Camera":
                            for btn in f.winfo_children():
                                if isinstance(btn, ttk.Button) and btn.cget("text") == "Cam: Turtle":
                                    btn.config(text="Cam: World")
                                    break
        self.update_visualization(self.interpreter.turtle)

    def update_visualization(self, turtle: Turtle3D):
        if self.camera_mode == "turtle":
            self.camera_angle_x = turtle.angle_x
            self.camera_angle_y = turtle.angle_y
            self.camera_angle_z = turtle.angle_z

        self.canvas.delete("all")

        # Siatka pomocnicza
        grid_size = 20
        grid_step = 1.0
        for i in range(-grid_size//2, grid_size//2 + 1):
            x = i * grid_step
            p1 = self.project_3d_to_2d(x, 0, -grid_size//2 * grid_step)
            p2 = self.project_3d_to_2d(x, 0,  grid_size//2 * grid_step)
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill='lightgray', width=1)
            p1 = self.project_3d_to_2d(-grid_size//2 * grid_step, 0, x)
            p2 = self.project_3d_to_2d( grid_size//2 * grid_step, 0, x)
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill='lightgray', width=1)

        # Osie
        ox, oy = self.project_3d_to_2d(0,0,0)
        x_axis = self.project_3d_to_2d(5,0,0)
        self.canvas.create_line(ox, oy, x_axis[0], x_axis[1], fill='red', width=2)
        y_axis = self.project_3d_to_2d(0,5,0)
        self.canvas.create_line(ox, oy, y_axis[0], y_axis[1], fill='green', width=2)
        z_axis = self.project_3d_to_2d(0,0,5)
        self.canvas.create_line(ox, oy, z_axis[0], z_axis[1], fill='blue', width=2)

        # Wierzchołki
        for v in turtle.vertices:
            x, y = self.project_3d_to_2d(v.x, v.y, v.z)
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='blue', outline='')

        # Linie
        for start_pos, end_pos in turtle.lines:
            sx1, sy1 = self.project_3d_to_2d(start_pos.x, start_pos.y, start_pos.z)
            sx2, sy2 = self.project_3d_to_2d(end_pos.x, end_pos.y, end_pos.z)
            self.canvas.create_line(sx1, sy1, sx2, sy2, fill='black', width=2)

        # Rysowanie aktualnej ściany
        pts = turtle.current_face_vertices
        if len(pts) > 1:
            for i in range(1, len(pts)):
                sx1, sy1 = self.project_3d_to_2d(pts[i-1].x, pts[i-1].y, pts[i-1].z)
                sx2, sy2 = self.project_3d_to_2d(pts[i].x, pts[i].y, pts[i].z)
                self.canvas.create_line(sx1, sy1, sx2, sy2, fill='black', width=2)

        # Gotowe ściany
        for face in turtle.faces:
            points = []
            for v in face.vertices:
                sx, sy = self.project_3d_to_2d(v.x, v.y, v.z)
                points.extend([sx, sy])
            if len(points) >= 6:
                self.canvas.create_polygon(points, outline='black', fill='lightblue', stipple='gray50')

        # Pozycja żółwia
        tx, ty = self.project_3d_to_2d(turtle.position.x, turtle.position.y, turtle.position.z)
        self.canvas.create_oval(tx-5, ty-5, tx+5, ty+5, fill='red', outline='black')

        # Kierunki
        fwd = turtle.get_direction_vector()
        up = self.rotate_vector(0, 1, 0, turtle.angle_x, turtle.angle_y, turtle.angle_z)
        right = self.cross(fwd, up)
        length = 0.8
        fx, fy, fz = fwd
        ex, ey, ez = (turtle.position.x + fx*length,
                      turtle.position.y + fy*length,
                      turtle.position.z + fz*length)
        sx, sy = self.project_3d_to_2d(ex, ey, ez)
        self.canvas.create_line(tx, ty, sx, sy, fill='red', width=3)

        ux, uy, uz = up
        ex, ey, ez = (turtle.position.x + ux*length,
                      turtle.position.y + uy*length,
                      turtle.position.z + uz*length)
        sx, sy = self.project_3d_to_2d(ex, ey, ez)
        self.canvas.create_line(tx, ty, sx, sy, fill='green', width=3)

        rx, ry, rz = right
        ex, ey, ez = (turtle.position.x + rx*length,
                      turtle.position.y + ry*length,
                      turtle.position.z + rz*length)
        sx, sy = self.project_3d_to_2d(ex, ey, ez)
        self.canvas.create_line(tx, ty, sx, sy, fill='blue', width=3)

        self.status.config(text=f"Position: ({turtle.position.x:.2f}, {turtle.position.y:.2f}, {turtle.position.z:.2f}) | "
                                f"Angles: ({turtle.angle_x:.1f}, {turtle.angle_y:.1f}, {turtle.angle_z:.1f}) | "
                                f"Pen: {'DOWN' if turtle.is_pen_down else 'UP'} | "
                                f"Vertices: {len(turtle.vertices)} | Faces: {len(turtle.faces)}")

    def project_3d_to_2d(self, x: float, y: float, z: float) -> tuple:
        rad_z = math.radians(self.camera_angle_z)
        cos_z, sin_z = math.cos(rad_z), math.sin(rad_z)
        x1 = x * cos_z - y * sin_z
        y1 = x * sin_z + y * cos_z
        z1 = z

        rad_x = math.radians(self.camera_angle_x)
        cos_x, sin_x = math.cos(rad_x), math.sin(rad_x)
        y2 = y1 * cos_x - z1 * sin_x
        z2 = y1 * sin_x + z1 * cos_x
        x2 = x1

        rad_y = math.radians(self.camera_angle_y)
        cos_y, sin_y = math.cos(rad_y), math.sin(rad_y)
        x3 = x2 * cos_y + z2 * sin_y
        z3 = -x2 * sin_y + z2 * cos_y
        y3 = y2

        denominator = self.camera_distance + z3
        if abs(denominator) < 1e-6:
            denominator = 1e-6 if denominator >= 0 else -1e-6

        scale = 300 / denominator
        screen_x = 400 + x3 * scale + self.pan_x
        screen_y = 300 - y3 * scale + self.pan_y
        return (screen_x, screen_y)

    def rotate_vector(self, x, y, z, ax, ay, az):
        rx, ry, rz = math.radians(ax), math.radians(ay), math.radians(az)
        cosz, sinz = math.cos(rz), math.sin(rz)
        x1 = x * cosz - y * sinz
        y1 = x * sinz + y * cosz
        z1 = z
        cosy, siny = math.cos(ry), math.sin(ry)
        x2 = x1 * cosy + z1 * siny
        z2 = -x1 * siny + z1 * cosy
        y2 = y1
        cosx, sinx = math.cos(rx), math.sin(rx)
        y3 = y2 * cosx - z2 * sinx
        z3 = y2 * sinx + z2 * cosx
        x3 = x2
        return (x3, y3, z3)

    def cross(self, a, b):
        return (a[1]*b[2] - a[2]*b[1],
                a[2]*b[0] - a[0]*b[2],
                a[0]*b[1] - a[1]*b[0])

    def rotate_camera(self, dx, dy):
        self.camera_angle_x += dx
        self.camera_angle_y += dy
        self.update_visualization(self.interpreter.turtle)

    def roll_camera(self, dz):
        self.camera_angle_z += dz
        self.update_visualization(self.interpreter.turtle)

    def zoom_camera(self, delta):
        self.camera_distance += delta
        if self.camera_distance < 2:
            self.camera_distance = 2
        self.update_visualization(self.interpreter.turtle)

    def pan_camera(self, dx, dy):
        self.pan_x += dx
        self.pan_y += dy
        self.update_visualization(self.interpreter.turtle)

    def reset_camera(self):
        self.camera_distance = 10.0
        self.camera_angle_x = 30.0
        self.camera_angle_y = 45.0
        self.camera_angle_z = 0.0
        self.pan_x = 0.0
        self.pan_y = 0.0
        self.update_visualization(self.interpreter.turtle)

    def export_obj(self):
        filename = "output.obj"
        self.interpreter.turtle.export_obj(filename)
        self.status.config(text=f"Exported to {filename}")

    def load_program(self, tree):
        self.program_tree = tree
        self.interpreter.app = self
        self.status.config(text="Loaded program. Press Play or Step.")

    def set_delay(self, val):
        self.delay_ms = int(float(val))


    def start_animation(self):
        if self.is_running:
            self.run_mode = "play"
            self.step_var.set(self.step_var.get() + 1)
            self.status.config(text="Running...")
            return
        if not self.program_tree:
            return
        self.is_running = True
        self.run_mode = "play"
        self.status.config(text="Running...")
        try:
            self.interpreter.execute_program(self.program_tree, self)
            self.status.config(text="Program finished")
        except Exception as e:
            error_msg = str(e)
            self.status.config(text=f"Error: {error_msg}")
            print(f"Runtime error: {error_msg}") 
        finally:
            self.is_running = False
            self.run_mode = "stop"

    def step_animation(self):
        if self.is_running:
            self.run_mode = "step"
            self.step_var.set(self.step_var.get() + 1)
            self.status.config(text="Stepping...")
        else:
            self.is_running = True
            self.run_mode = "step"
            self.status.config(text="Stepping...")
            try:
                self.interpreter.execute_program(self.program_tree, self)
                self.status.config(text="Program finished")
            except Exception as e:
                error_msg = str(e)
                self.status.config(text=f"Error: {error_msg}")
                print(f"Runtime error: {error_msg}") 
            finally:
                self.is_running = False
                self.run_mode = "stop"

    def stop_animation(self):
        if self.is_running:
            self.run_mode = "pause"
            self.status.config(text="Paused. Press Play or Step.")


    def on_closing(self):
        self.is_running = False
        self.run_mode = "stop"
        self.step_var.set(1)
        self.destroy()
        import os
        os._exit(0)