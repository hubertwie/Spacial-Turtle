import math
import tkinter as tk
from tkinter import ttk
from typing import Dict, Any, List
import numpy as np

from turtle3d import Turtle3D, Vertex
from SpacialTurtleVisitor import SpacialTurtleVisitor
from SpacialTurtleParser import SpacialTurtleParser


class SpacialTurtleInterpreter(SpacialTurtleVisitor):
    def __init__(self, turtle: Turtle3D):
        self.turtle = turtle
        self.variables = {}

    def execute_program(self, tree, root_window=None):
        """Execute the entire program (synchronous)"""
        try:
            self.visit(tree)
            if root_window:
                root_window.update_visualization(self.turtle)
        except Exception as e:
            print(f"Runtime error: {e}")
            raise

    def execute_statement(self, ctx):
        """Execute a single statement (używane przez animację kolegi!)"""
        self.visit(ctx)

    def get_value(self, ctx):
        """Pomocnicza funkcja do wyciągania wartości (liczba lub zmienna)"""
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.ID():
            name = ctx.ID().getText()
            if name in self.variables:
                return self.variables[name]
            else:
                raise NameError(f"Zmienna '{name}' nie została zadeklarowana!")
        return 0.0

    def visitMoveCmd(self, ctx):
        dist = self.get_value(ctx.value())
        self.turtle.move(dist)

    def visitTurnCmd(self, ctx):
        angle = self.get_value(ctx.value())

        # 1. Sprawdzamy, jakiej osi chce użyć programista
        if ctx.TURNX():
            current_axis = 'X'
        elif ctx.TURNY():
            current_axis = 'Y'
        elif ctx.TURNZ():
            current_axis = 'Z'

        # --- SMART ANALIZA SEMANTYCZNA ---
        if self.turtle.in_face:
            if self.turtle.locked_face_axis is None:
                # To jest pierwszy obrót w tej ścianie! Zapisujemy tę oś.
                self.turtle.locked_face_axis = current_axis
            elif self.turtle.locked_face_axis != current_axis:
                # Ktoś próbuje użyć INNEJ osi w tej samej ścianie!
                raise RuntimeError(
                    f"Błąd Semantyczny: Rozpoczęto rysowanie ściany w osi {self.turtle.locked_face_axis}, nie można teraz użyć osi {current_axis}! Złamiesz płaszczyznę.")
        # ---------------------------------

        # 2. Jeśli wszystko jest legalne, wykonujemy obrót
        if current_axis == 'X':
            self.turtle.rotate_x(angle)
        elif current_axis == 'Y':
            self.turtle.rotate_y(angle)
        elif current_axis == 'Z':
            self.turtle.rotate_z(angle)

    def visitPenCmd(self, ctx):
        if self.turtle.in_face:
            raise RuntimeError(
                "Błąd Semantyczny: Nie można zmieniać stanu pisaka w trakcie rysowania płaszczyzny (face).")
        if ctx.UP():
            self.turtle.pen_up()
        elif ctx.DOWN():
            self.turtle.pen_down()

    def visitFaceBlock(self, ctx):
        # Wejście w blok
        self.turtle.begin_face()
        # To polecenie automatycznie wykonuje wszystkie instrukcje wewnątrz klamerek!
        self.visitChildren(ctx)
        # Wyjście z bloku
        self.turtle.end_face()

    def visitLetInstr(self, ctx):
        name = ctx.ID().getText()
        val = self.get_value(ctx.value())
        self.variables[name] = val
        self.turtle.set_variable(name, val)

    def visitExportCmd(self, ctx):
        filename = "output.obj"
        self.turtle.export_obj(filename)
        print(f"Siatka wyeksportowana do {filename}")


class TurtleVisualization(tk.Tk):
    def __init__(self, interpreter: SpacialTurtleInterpreter):
        super().__init__()
        self.interpreter = interpreter
        self.title("Spacial Turtle 3D Visualization")
        self.geometry("900x700")
        
        # Camera parameters
        self.camera_distance = 10.0
        self.camera_angle_x = 30.0    # pitch
        self.camera_angle_y = 45.0    # yaw
        self.camera_angle_z = 0.0     # roll
        self.pan_x = 0.0
        self.pan_y = 0.0
        
        # Animation control
        self.statement_list: List = []
        self.current_index = 0
        self.animation_running = False
        self.delay_ms = 200
        self.program_tree = None
        
        # Create canvas
        self.canvas = tk.Canvas(self, bg='white', width=800, height=550)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Control panel
        control_frame = ttk.Frame(self)
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Row 1: Camera controls
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
        
        # Row 2: Animation controls
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
        
        # Status bar
        self.status = ttk.Label(self, text="Ready", relief=tk.SUNKEN)
        self.status.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.update_visualization(self.interpreter.turtle)
    
    # --- Animation methods -------------------------------------------------
    def load_program(self, tree):
        """Load a program tree for step-by-step execution"""
        self.program_tree = tree
        self.statement_list = []

        # Sprytna funkcja wyciągająca instrukcje z bloków
        def flatten(node):
            name = type(node).__name__
            if name in ['MoveCmdContext', 'TurnCmdContext', 'PenCmdContext', 'LetInstrContext']:
                self.statement_list.append(node)
            elif name == 'FaceBlockContext':
                self.statement_list.append("BEGIN_FACE")
                for child in node.getChildren():
                    flatten(child)
                self.statement_list.append("END_FACE")
            elif hasattr(node, 'getChildren'):
                for child in node.getChildren():
                    flatten(child)

        flatten(tree)
        self.current_index = 0
        self.stop_animation()
        self.status.config(text=f"Loaded {len(self.statement_list)} steps. Press Play.")
    
    def set_delay(self, val):
        self.delay_ms = int(float(val))
    
    def start_animation(self):
        if self.program_tree is None:
            self.status.config(text="No program loaded")
            return
        if self.current_index >= len(self.statement_list):
            self.status.config(text="Program finished")
            return
        self.animation_running = True
        self.next_statement()
    
    def stop_animation(self):
        self.animation_running = False
    
    def step_animation(self):
        self.stop_animation()
        self.next_statement()

    def next_statement(self):
        if self.current_index >= len(self.statement_list):
            self.status.config(text="Program finished")
            self.animation_running = False
            return

        stmt = self.statement_list[self.current_index]
        self.current_index += 1

        try:
            # Jeśli to nasz znacznik, odpalamy akcję w żółwiu
            if stmt == "BEGIN_FACE":
                self.interpreter.turtle.begin_face()
            elif stmt == "END_FACE":
                self.interpreter.turtle.end_face()
            else:
                # W przeciwnym razie puszczamy komendę przez Visitora
                self.interpreter.visit(stmt)

            self.update_visualization(self.interpreter.turtle)
        except Exception as e:
            self.status.config(text=f"Error: {e}")
            self.animation_running = False
            return

        if self.animation_running and self.current_index < len(self.statement_list):
            self.after(self.delay_ms, self.next_statement)
    
    # --- Projection and drawing --------------------------------------------
    def project_3d_to_2d(self, x: float, y: float, z: float) -> tuple:
        """Project 3D point to 2D canvas coordinates with camera roll and pan"""
        # Apply roll (Z rotation)
        rad_z = math.radians(self.camera_angle_z)
        cos_z, sin_z = math.cos(rad_z), math.sin(rad_z)
        x1 = x * cos_z - y * sin_z
        y1 = x * sin_z + y * cos_z
        z1 = z
        
        # Apply pitch (X rotation)
        rad_x = math.radians(self.camera_angle_x)
        cos_x, sin_x = math.cos(rad_x), math.sin(rad_x)
        y2 = y1 * cos_x - z1 * sin_x
        z2 = y1 * sin_x + z1 * cos_x
        x2 = x1
        
        # Apply yaw (Y rotation)
        rad_y = math.radians(self.camera_angle_y)
        cos_y, sin_y = math.cos(rad_y), math.sin(rad_y)
        x3 = x2 * cos_y + z2 * sin_y
        z3 = -x2 * sin_y + z2 * cos_y
        y3 = y2
        
        # Perspective projection
        scale = 300 / (self.camera_distance + z3)
        screen_x = 400 + x3 * scale + self.pan_x
        screen_y = 300 - y3 * scale + self.pan_y
        
        return (screen_x, screen_y)
    
    def rotate_vector(self, x, y, z, ax, ay, az):
        """Rotate vector (x,y,z) by Euler angles (ax,ay,az) in degrees"""
        rx, ry, rz = math.radians(ax), math.radians(ay), math.radians(az)
        
        # Apply Z
        cosz, sinz = math.cos(rz), math.sin(rz)
        x1 = x * cosz - y * sinz
        y1 = x * sinz + y * cosz
        z1 = z
        
        # Apply Y
        cosy, siny = math.cos(ry), math.sin(ry)
        x2 = x1 * cosy + z1 * siny
        z2 = -x1 * siny + z1 * cosy
        y2 = y1
        
        # Apply X
        cosx, sinx = math.cos(rx), math.sin(rx)
        y3 = y2 * cosx - z2 * sinx
        z3 = y2 * sinx + z2 * cosx
        x3 = x2
        
        return (x3, y3, z3)
    
    def cross(self, a, b):
        return (a[1]*b[2] - a[2]*b[1],
                a[2]*b[0] - a[0]*b[2],
                a[0]*b[1] - a[1]*b[0])

    def update_visualization(self, turtle: Turtle3D):
        """Update the canvas with current turtle position"""
        self.canvas.delete("all")

        # Draw all vertices as small circles
        for v in turtle.vertices:
            x, y = self.project_3d_to_2d(v.x, v.y, v.z)
            self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='blue', outline='')

        # --- NOWOŚĆ: Rysowanie czarnych krawędzi aktualnej ściany ---
        pts = turtle.current_face_vertices
        if len(pts) > 1:
            for i in range(1, len(pts)):
                sx1, sy1 = self.project_3d_to_2d(pts[i - 1].x, pts[i - 1].y, pts[i - 1].z)
                sx2, sy2 = self.project_3d_to_2d(pts[i].x, pts[i].y, pts[i].z)
                self.canvas.create_line(sx1, sy1, sx2, sy2, fill='black', width=2)
        
        # Draw faces (filled polygons)
        for face in turtle.faces:
            points = []
            for v in face.vertices:
                sx, sy = self.project_3d_to_2d(v.x, v.y, v.z)
                points.extend([sx, sy])
            if len(points) >= 6:
                self.canvas.create_polygon(points, outline='black', fill='lightblue',
                                           stipple='gray50')
        
        # Draw turtle position and orientation
        tx, ty = self.project_3d_to_2d(turtle.position.x, turtle.position.y, turtle.position.z)
        self.canvas.create_oval(tx-5, ty-5, tx+5, ty+5, fill='red', outline='black')
        
        # Compute forward, up, right vectors
        fwd = turtle.get_direction_vector()
        # Global up is (0,1,0). Rotate it by turtle's angles to get local up
        up = self.rotate_vector(0, 1, 0, turtle.angle_x, turtle.angle_y, turtle.angle_z)
        # Right = forward × up
        right = self.cross(fwd, up)
        
        # Scale for drawing
        length = 0.8
        # Draw forward (red)
        fx, fy, fz = fwd
        ex, ey, ez = (turtle.position.x + fx*length,
                      turtle.position.y + fy*length,
                      turtle.position.z + fz*length)
        sx, sy = self.project_3d_to_2d(ex, ey, ez)
        self.canvas.create_line(tx, ty, sx, sy, fill='red', width=3)
        
        # Draw up (green)
        ux, uy, uz = up
        ex, ey, ez = (turtle.position.x + ux*length,
                      turtle.position.y + uy*length,
                      turtle.position.z + uz*length)
        sx, sy = self.project_3d_to_2d(ex, ey, ez)
        self.canvas.create_line(tx, ty, sx, sy, fill='green', width=3)
        
        # Draw right (blue)
        rx, ry, rz = right
        ex, ey, ez = (turtle.position.x + rx*length,
                      turtle.position.y + ry*length,
                      turtle.position.z + rz*length)
        sx, sy = self.project_3d_to_2d(ex, ey, ez)
        self.canvas.create_line(tx, ty, sx, sy, fill='blue', width=3)
        
        # Update status
        self.status.config(text=f"Position: ({turtle.position.x:.2f}, {turtle.position.y:.2f}, {turtle.position.z:.2f}) | "
                              f"Angles: ({turtle.angle_x:.1f}, {turtle.angle_y:.1f}, {turtle.angle_z:.1f}) | "
                              f"Pen: {'DOWN' if turtle.is_pen_down else 'UP'} | "
                              f"Vertices: {len(turtle.vertices)} | Faces: {len(turtle.faces)}")
    
    # --- Camera controls ---------------------------------------------------
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