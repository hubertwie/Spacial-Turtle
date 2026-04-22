import math
import tkinter as tk
from tkinter import ttk
from typing import Dict, Any, List, Tuple, Union
import numpy as np

from turtle3d import Turtle3D, Vertex
from SpacialTurtleVisitor import SpacialTurtleVisitor
from SpacialTurtleParser import SpacialTurtleParser
from symbols import SymbolTable, Type, FunctionSymbol


class SpacialTurtleInterpreter(SpacialTurtleVisitor):
    def __init__(self, turtle: Turtle3D, symbol_table: SymbolTable):
        self.turtle = turtle
        self.symbol_table = symbol_table
        self.current_return_value = None
        self.in_function = False

    def execute_program(self, tree, root_window=None):
        try:
            self.visit(tree)
            if root_window:
                root_window.update_visualization(self.turtle)
        except Exception as e:
            print(f"Błąd wykonania (Runtime Error): {e}")
            raise

    def execute_statement(self, ctx):
        self.visit(ctx)

    def error(self, ctx, msg):
        line = ctx.start.line
        col = ctx.start.column
        raise RuntimeError(f"Linia {line}, kol. {col}: {msg}")

    def get_variable(self, text: str) -> Tuple[Any, Type]:
        """
        Zwraca (wartość, typ) zmiennej. Obsługuje parent:: i szukanie w górę stosu.
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
            raise RuntimeError(f"Zbyt wiele 'parent::'. Zmienna '{var_name}' nie istnieje na tym poziomie.")
        else:
            for scope in reversed(self.turtle.scope_stack):
                if var_name in scope:
                    return scope[var_name]
            if var_name in self.turtle.global_vars:
                return self.turtle.global_vars[var_name]
            raise RuntimeError(f"Zmienna '{var_name}' nie została zadeklarowana!")

    def set_variable(self, text: str, value: Any, value_type: Type):
        """
        Nadpisuje wartość istniejącej zmiennej (typ musi być zgodny).
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
                        self._check_type_compatibility(value_type, old_type, text, "przypisaniu")
                        if old_type == Type.FLOAT and value_type == Type.INT:
                            value = float(value)
                        scope[var_name] = (value, old_type)
                        return
                elif abs(target_scope_idx) == len(self.turtle.scope_stack) + 1:
                    if var_name in self.turtle.global_vars:
                        old_val, old_type = self.turtle.global_vars[var_name]
                        self._check_type_compatibility(value_type, old_type, text, "przypisaniu")
                        self.turtle.global_vars[var_name] = (value, old_type)
                        return
            raise RuntimeError(f"Zbyt wiele 'parent::' dla zmiennej '{var_name}'")
        else:
            for scope in reversed(self.turtle.scope_stack):
                if var_name in scope:
                    old_val, old_type = scope[var_name]
                    self._check_type_compatibility(value_type, old_type, text, "przypisaniu")
                    if old_type == Type.FLOAT and value_type == Type.INT:
                        value = float(value)
                    scope[var_name] = (value, old_type)
                    return
            if var_name in self.turtle.global_vars:
                old_val, old_type = self.turtle.global_vars[var_name]
                self._check_type_compatibility(value_type, old_type, text, "przypisaniu")
                self.turtle.global_vars[var_name] = (value, old_type)
                return
            raise RuntimeError(f"Przypisanie do niezadeklarowanej zmiennej '{var_name}'")

    def declare_variable(self, name: str, declared_type: Type, initial_value: Any, initial_type: Type, ctx):
        """
        Deklaruje nową zmienną w bieżącym zakresie.
        """
        if initial_value is not None:
            self._check_type_compatibility(initial_type, declared_type, name, "inicjalizacji")
            if declared_type == Type.FLOAT and initial_type == Type.INT:
                initial_value = float(initial_value)

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

    def _check_type_compatibility(self, src_type: Type, dst_type: Type, name: str, operation: str):
        """
        Sprawdza, czy typ źródłowy można przypisać do docelowego.
        Dozwolone: int -> float, oraz identyczne typy.
        Niedozwolone: float -> int, bool <-> numeryczne.
        """
        if src_type == dst_type:
            return
        if src_type == Type.INT and dst_type == Type.FLOAT:
            return
        raise RuntimeError(f"Nie można wykonać {operation} zmiennej '{name}': typ {src_type.name} nie jest zgodny z {dst_type.name}")

    def get_python_type(self, val) -> Type:
        if isinstance(val, bool):
            return Type.BOOL
        if isinstance(val, float):
            return Type.FLOAT
        if isinstance(val, int):
            return Type.INT
        return Type.VOID

    def is_number(self, typ):
        return typ in [Type.INT, Type.FLOAT]

    def visitExpr(self, ctx):
        return self.visit(ctx.logicalExpr())

    def visitLogicalExpr(self, ctx):
        left_val, left_type = self.visit(ctx.comparisonExpr(0))
        for i in range(1, len(ctx.comparisonExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right_val, right_type = self.visit(ctx.comparisonExpr(i))
            if left_type != Type.BOOL or right_type != Type.BOOL:
                self.error(ctx, "Operatory 'and'/'or' wymagają typów bool!")
            if op == 'and':
                left_val = left_val and right_val
            else:
                left_val = left_val or right_val
        return left_val, left_type

    def visitComparisonExpr(self, ctx):
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
        val, typ = self.visit(ctx.unaryExpr(0))
        for i in range(1, len(ctx.unaryExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right_val, right_type = self.visit(ctx.unaryExpr(i))
            if not self.is_number(typ) or not self.is_number(right_type):
                self.error(ctx, "Mnożenie/Dzielenie wymaga liczb.")

            if op == '*':
                val *= right_val
            else:
                if right_val == 0: self.error(ctx, "Dzielenie przez zero!")
                val /= right_val

            if typ == Type.FLOAT or right_type == Type.FLOAT or op == '/':
                typ = Type.FLOAT
            else:
                typ = Type.INT
        return val, typ

    def visitUnaryExpr(self, ctx):
        if ctx.PLUS():
            val, typ = self.visit(ctx.unaryExpr())
            if not self.is_number(typ): self.error(ctx, "Znak '+' wymaga liczby.")
            return val, typ
        if ctx.MINUS():
            val, typ = self.visit(ctx.unaryExpr())
            if not self.is_number(typ): self.error(ctx, "Znak '-' wymaga liczby.")
            return -val, typ
        if ctx.NOT():
            val, typ = self.visit(ctx.unaryExpr())
            if typ != Type.BOOL: self.error(ctx, "NOT wymaga typu bool.")
            return not val, Type.BOOL
        return self.visit(ctx.primaryExpr())

    def visitPrimaryExpr(self, ctx):
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
            val, typ = self.get_variable(ref_name)
            return val, typ
        if ctx.LPAREN():
            return self.visit(ctx.expr())
        if ctx.funcCall():
            return self.visitFuncCall(ctx.funcCall())
        if ctx.varType():
            # Rzutowanie typów
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
        """Wymusza odświeżenie okienka i obsługuje Step/Pause."""
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
        name = ctx.ID().getText()
        type_str = ctx.varType().getText()
        declared_type = {
            'int': Type.INT,
            'float': Type.FLOAT,
            'bool': Type.BOOL
        }[type_str]

        init_val = None
        init_type = None
        if ctx.expr():
            init_val, init_type = self.visit(ctx.expr())
        self.declare_variable(name, declared_type, init_val, init_type, ctx)
        self.ui_step()

    def visitAssignStmt(self, ctx):
        ref_text = ctx.variableRef().getText()
        val, typ = self.visit(ctx.expr())
        self.set_variable(ref_text, val, typ)
        self.ui_step()

    def visitMoveCmd(self, ctx):
        dist, typ = self.visit(ctx.expr())
        if not self.is_number(typ):
            self.error(ctx.expr(), "Dystans musi być liczbą!")
        self.turtle.move(dist)
        self.ui_step()

    def visitTurnCmd(self, ctx):
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
        if self.turtle.in_face:
            self.error(ctx, "Nie można zmieniać pisaka wewnątrz płaszczyzny (face)!")
        if ctx.UP():
            self.turtle.pen_up()
        else:
            self.turtle.pen_down()

    def visitFaceBlock(self, ctx):
        self.turtle.begin_face()
        self.visitChildren(ctx)
        self.turtle.end_face()

    def visitExportCmd(self, ctx):
        self.turtle.export_obj("output.obj")
        print("Wyeksportowano do output.obj")

    def visitPrintStmt(self, ctx):
        val, typ = self.visit(ctx.expr())
        print(val)
        self.ui_step()

    def visitBlock(self, ctx):
        if ctx.getChild(0).getText() == '{':
            for stmt in ctx.statement():
                self.visit(stmt)
        else:
            self.visit(ctx.statement(0))

    def visitIfStmt(self, ctx):
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
        while True:
            cond, typ = self.visit(ctx.expr())
            if typ != Type.BOOL:
                self.error(ctx.expr(), "Warunek w WHILE musi być typu bool!")
            if not cond:
                break
            self.turtle.push_scope()
            self.visit(ctx.block())
            self.turtle.pop_scope()

    def visitForStmt(self, ctx):
        self.turtle.push_scope()

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

            self.visit(ctx.block())

            if update_assign:
                self.visit(update_assign)

        self.turtle.pop_scope()

    def visitFuncDef(self, ctx):
        pass

    def visitReturnStmt(self, ctx):
        if ctx.expr():
            val, typ = self.visit(ctx.expr())
            self.current_return_value = val
        else:
            self.current_return_value = None


class TurtleVisualization(tk.Tk):
    """
    Główne okno aplikacji z wizualizacją 3D żółwia.
    Zapewnia interaktywne sterowanie kamerą, animację krokową i eksport siatki.
    """

    def __init__(self, interpreter: SpacialTurtleInterpreter):
        super().__init__()
        self.interpreter = interpreter
        self.title("Spacial Turtle 3D Visualization")
        self.geometry("900x700")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.camera_distance = 10.0
        self.camera_angle_x = 30.0
        self.camera_angle_y = 45.0
        self.camera_angle_z = 0.0
        self.pan_x = 0.0
        self.pan_y = 0.0

        self.camera_mode = "world"

        self.statement_list: List = []
        self.current_index = 0
        self.animation_running = False
        self.delay_ms = 200
        self.step_var = tk.IntVar(value=0)
        self.run_mode = "stop"
        self.is_running = False
        self.program_tree = None

        self.canvas = tk.Canvas(self, bg='white', width=800, height=550)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        control_frame = ttk.Frame(self)
        control_frame.pack(fill=tk.X, padx=5, pady=5)

        camera_frame = ttk.LabelFrame(control_frame, text="Camera", padding=5)
        camera_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)

        ttk.Button(camera_frame, text="Rotate Left",
                   command=lambda: self.rotate_camera(0, -10)).pack(side=tk.LEFT, padx=2)
        ttk.Button(camera_frame, text="Rotate Right",
                   command=lambda: self.rotate_camera(0, 10)).pack(side=tk.LEFT, padx=2)
        ttk.Button(camera_frame, text="Rotate Up",
                   command=lambda: self.rotate_camera(10, 0)).pack(side=tk.LEFT, padx=2)
        ttk.Button(camera_frame, text="Rotate Down",
                   command=lambda: self.rotate_camera(-10, 0)).pack(side=tk.LEFT, padx=2)

        ttk.Button(camera_frame, text="Roll Left",
                   command=lambda: self.roll_camera(-10)).pack(side=tk.LEFT, padx=2)
        ttk.Button(camera_frame, text="Roll Right",
                   command=lambda: self.roll_camera(10)).pack(side=tk.LEFT, padx=2)

        ttk.Button(camera_frame, text="Zoom In",
                   command=lambda: self.zoom_camera(-0.5)).pack(side=tk.LEFT, padx=2)
        ttk.Button(camera_frame, text="Zoom Out",
                   command=lambda: self.zoom_camera(0.5)).pack(side=tk.LEFT, padx=2)

        ttk.Button(camera_frame, text="Pan Left",
                   command=lambda: self.pan_camera(-20, 0)).pack(side=tk.LEFT, padx=2)
        ttk.Button(camera_frame, text="Pan Right",
                   command=lambda: self.pan_camera(20, 0)).pack(side=tk.LEFT, padx=2)
        ttk.Button(camera_frame, text="Pan Up",
                   command=lambda: self.pan_camera(0, -20)).pack(side=tk.LEFT, padx=2)
        ttk.Button(camera_frame, text="Pan Down",
                   command=lambda: self.pan_camera(0, 20)).pack(side=tk.LEFT, padx=2)

        ttk.Button(camera_frame, text="Reset View",
                   command=self.reset_camera).pack(side=tk.LEFT, padx=2)

        self.cam_mode_btn = ttk.Button(camera_frame, text="Cam: World",
                                        command=self.toggle_camera_mode)
        self.cam_mode_btn.pack(side=tk.LEFT, padx=2)

        anim_frame = ttk.LabelFrame(control_frame, text="Animation", padding=5)
        anim_frame.pack(side=tk.LEFT, fill=tk.X, padx=2)

        ttk.Button(anim_frame, text="▶ Play", command=self.start_animation).pack(side=tk.LEFT, padx=2)
        ttk.Button(anim_frame, text="⏸ Pause", command=self.stop_animation).pack(side=tk.LEFT, padx=2)
        ttk.Button(anim_frame, text="⏩ Step", command=self.step_animation).pack(side=tk.LEFT, padx=2)

        ttk.Label(anim_frame, text="Speed (ms):").pack(side=tk.LEFT, padx=(10,2))
        self.speed_scale = ttk.Scale(anim_frame, from_=50, to=500, orient=tk.HORIZONTAL,
                                      command=self.set_delay, length=100)
        self.speed_scale.set(200)
        self.speed_scale.pack(side=tk.LEFT, padx=2)

        ttk.Button(control_frame, text="Export OBJ",
                   command=self.export_obj).pack(side=tk.RIGHT, padx=2)

        self.status = ttk.Label(self, text="Ready", relief=tk.SUNKEN)
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

        self.update_visualization(self.interpreter.turtle)

    def toggle_camera_mode(self):
        if self.camera_mode == "world":
            self.camera_mode = "turtle"
            self.cam_mode_btn.config(text="Cam: Turtle")
            self.camera_angle_x = self.interpreter.turtle.angle_x
            self.camera_angle_y = self.interpreter.turtle.angle_y
            self.camera_angle_z = self.interpreter.turtle.angle_z
        else:
            self.camera_mode = "world"
            self.cam_mode_btn.config(text="Cam: World")
        self.update_visualization(self.interpreter.turtle)

    def update_visualization(self, turtle: Turtle3D):
        if self.camera_mode == "turtle":
            self.camera_angle_x = turtle.angle_x
            self.camera_angle_y = turtle.angle_y
            self.camera_angle_z = turtle.angle_z

        self.canvas.delete("all")

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

        ox, oy = self.project_3d_to_2d(0,0,0)
        x_axis = self.project_3d_to_2d(5,0,0)
        self.canvas.create_line(ox, oy, x_axis[0], x_axis[1], fill='red', width=2)
        y_axis = self.project_3d_to_2d(0,5,0)
        self.canvas.create_line(ox, oy, y_axis[0], y_axis[1], fill='green', width=2)
        z_axis = self.project_3d_to_2d(0,0,5)
        self.canvas.create_line(ox, oy, z_axis[0], z_axis[1], fill='blue', width=2)

        for v in turtle.vertices:
            x, y = self.project_3d_to_2d(v.x, v.y, v.z)
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='blue', outline='')

        for start_pos, end_pos in turtle.lines:
            sx1, sy1 = self.project_3d_to_2d(start_pos.x, start_pos.y, start_pos.z)
            sx2, sy2 = self.project_3d_to_2d(end_pos.x, end_pos.y, end_pos.z)
            self.canvas.create_line(sx1, sy1, sx2, sy2, fill='black', width=2)

        pts = turtle.current_face_vertices
        if len(pts) > 1:
            for i in range(1, len(pts)):
                sx1, sy1 = self.project_3d_to_2d(pts[i-1].x, pts[i-1].y, pts[i-1].z)
                sx2, sy2 = self.project_3d_to_2d(pts[i].x, pts[i].y, pts[i].z)
                self.canvas.create_line(sx1, sy1, sx2, sy2, fill='black', width=2)

        for face in turtle.faces:
            points = []
            for v in face.vertices:
                sx, sy = self.project_3d_to_2d(v.x, v.y, v.z)
                points.extend([sx, sy])
            if len(points) >= 6:
                self.canvas.create_polygon(points, outline='black', fill='lightblue', stipple='gray50')

        tx, ty = self.project_3d_to_2d(turtle.position.x, turtle.position.y, turtle.position.z)
        self.canvas.create_oval(tx-5, ty-5, tx+5, ty+5, fill='red', outline='black')

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

        scale = 300 / (self.camera_distance + z3)
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

    def rotate_camera(self, dx: float, dy: float):
        self.camera_angle_x += dx
        self.camera_angle_y += dy
        self.update_visualization(self.interpreter.turtle)

    def roll_camera(self, dz: float):
        self.camera_angle_z += dz
        self.update_visualization(self.interpreter.turtle)

    def zoom_camera(self, delta: float):
        self.camera_distance += delta
        if self.camera_distance < 2:
            self.camera_distance = 2
        self.update_visualization(self.interpreter.turtle)

    def pan_camera(self, dx: float, dy: float):
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
        print(f"Mesh exported to {filename}")

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
            self.status.config(text=f"Error: {e}")
        finally:
            self.is_running = False
            self.run_mode = "stop"

    def stop_animation(self):
        if self.is_running:
            self.run_mode = "pause"
            self.status.config(text="Paused. Press Play or Step.")

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
                self.status.config(text=f"Error: {e}")
            finally:
                self.is_running = False
                self.run_mode = "stop"

    def on_closing(self):
        self.is_running = False
        self.run_mode = "stop"
        self.step_var.set(1)
        self.destroy()
        import os
        os._exit(0)