import math
import numpy as np
from typing import List, Tuple, Optional


class Vertex:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def to_tuple(self) -> Tuple[float, float, float]:
        return (self.x, self.y, self.z)


class Face:
    def __init__(self, vertices: List[Vertex], is_quad: bool = False):
        self.vertices = vertices
        self.is_quad = is_quad


class Turtle3D:
    def __init__(self):
        self.position = Vertex(0.0, 0.0, 0.0)

        # --- ZAAWANSOWANA MATEMATYKA 3D (Zamiast Gimbal Locka) ---
        self.forward = np.array([0.0, 0.0, 1.0])
        self.up = np.array([0.0, 1.0, 0.0])
        self.right = np.array([1.0, 0.0, 0.0])

        # Zmienne tylko dla kompatybilności z UI
        self.angle_x = 0.0
        self.angle_y = 0.0
        self.angle_z = 0.0

        self.is_pen_down = True
        self.vertices: List[Vertex] = []
        self.faces: List[Face] = []
        self.current_face_vertices: List[Vertex] = []
        self.in_face = False
        self.variables: dict = {}
        self.scopes: List[dict] = [{}]

        self.in_face = False
        self.locked_face_axis = None

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def set_variable(self, name: str, value):
        self.scopes[-1][name] = value

    def get_variable(self, name: str):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise NameError(f"Variable '{name}' not defined")

    def rotate_vector(self, vec, axis, angle_degrees):
        """Pomocnicza funkcja: Obrót wektora wokół innej osi (Wzór Rodriguesa)"""
        rad = math.radians(angle_degrees)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        return vec * cos_a + np.cross(axis, vec) * sin_a + axis * np.dot(axis, vec) * (1 - cos_a)

    def rotate_x(self, angle: float):
        """Pitch - obrót nosa w górę/dół (wokół osi Right)"""
        self.forward = self.rotate_vector(self.forward, self.right, angle)
        self.up = self.rotate_vector(self.up, self.right, angle)
        self.angle_x += angle

    def rotate_y(self, angle: float):
        """Yaw - obrót w lewo/prawo (wokół osi Up)"""
        self.forward = self.rotate_vector(self.forward, self.up, angle)
        self.right = self.rotate_vector(self.right, self.up, angle)
        self.angle_y += angle

    def rotate_z(self, angle: float):
        """Roll - beczka (wokół osi Forward)"""
        self.up = self.rotate_vector(self.up, self.forward, angle)
        self.right = self.rotate_vector(self.right, self.forward, angle)
        self.angle_z += angle

    def get_direction_vector(self) -> Tuple[float, float, float]:
        """Zwraca gotowy, przeliczony wektor kierunku"""
        return tuple(self.forward)

        # ... TUTAJ ZOSTAW BEZ ZMIAN RESZTĘ PLIKU (funkcje move, pen_up, itd.) ...
        
        # Start with forward vector (0, 0, 1)
        x, y, z = 0.0, 0.0, 1.0
        
        # Rotate around X
        cos_rx, sin_rx = math.cos(rx), math.sin(rx)
        y, z = y * cos_rx - z * sin_rx, y * sin_rx + z * cos_rx
        
        # Rotate around Y
        cos_ry, sin_ry = math.cos(ry), math.sin(ry)
        x, z = x * cos_ry + z * sin_ry, -x * sin_ry + z * cos_ry
        
        # Rotate around Z
        cos_rz, sin_rz = math.cos(rz), math.sin(rz)
        x, y = x * cos_rz - y * sin_rz, x * sin_rz + y * cos_rz
        
        return (x, y, z)
    
    def move(self, distance: float):
        """Move turtle forward by distance"""
        dx, dy, dz = self.get_direction_vector()
        new_x = self.position.x + dx * distance
        new_y = self.position.y + dy * distance
        new_z = self.position.z + dz * distance
        
        if self.is_pen_down:
            # Add vertex
            new_vertex = Vertex(new_x, new_y, new_z)
            self.vertices.append(new_vertex)
            
            # If we're inside a face definition, add to current face
            if self.in_face:
                self.current_face_vertices.append(new_vertex)
        
        self.position = Vertex(new_x, new_y, new_z)
    
    def pen_up(self):
        """Lift the pen"""
        self.is_pen_down = False
    
    def pen_down(self):
        """Lower the pen"""
        self.is_pen_down = True
    
    def begin_face(self):
        """Start defining a face"""
        self.in_face = True
        self.locked_face_axis = None
        self.current_face_vertices = []
        # Add current position to face vertices
        self.current_face_vertices.append(Vertex(self.position.x, self.position.y, self.position.z))
    
    def end_face(self):
        """Finish defining a face"""
        if self.in_face and len(self.current_face_vertices) >= 3:
            # Create face from vertices
            self.faces.append(Face(self.current_face_vertices.copy()))
        self.in_face = False
        self.current_face_vertices = []
    
    def export_obj(self, filename: str):
        """Export mesh to OBJ file"""
        with open(filename, 'w') as f:
            f.write("# Generated by SpacialTurtle Interpreter\n")
            f.write("o TurtleMesh\n")
            
            # Write vertices
            for v in self.vertices:
                f.write(f"v {v.x} {v.y} {v.z}\n")
            
            # Write faces
            # OBJ uses 1-based indexing, so we need to map vertex indices
            # We need to store which vertices belong to which faces
            face_vertices = []
            for face in self.faces:
                face_indices = []
                for v in face.vertices:
                    # Find index of this vertex in the vertices list
                    try:
                        idx = self.vertices.index(v)
                        face_indices.append(idx + 1)  # +1 for OBJ 1-based indexing
                    except ValueError:
                        # Vertex not found in main list - shouldn't happen
                        pass
                if len(face_indices) >= 3:
                    face_vertices.append(face_indices)
            
            for indices in face_vertices:
                f.write(f"f {' '.join(map(str, indices))}\n")