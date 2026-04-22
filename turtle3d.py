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

        self.forward = np.array([0.0, 0.0, 1.0])
        self.up = np.array([0.0, 1.0, 0.0])
        self.right = np.array([1.0, 0.0, 0.0])

        self.angle_x = 0.0
        self.angle_y = 0.0
        self.angle_z = 0.0

        self.is_pen_down = True
        self.lines = []
        self.vertices: List[Vertex] = []
        self.faces: List[Face] = []
        self.current_face_vertices: List[Vertex] = []
        self.in_face = False
        self.variables: dict = {}

        self.in_face = False
        self.locked_face_axis = None

        self.global_vars = {}
        self.scope_stack = []

    def push_scope(self):
        self.scope_stack.append({})

    def pop_scope(self):
        if self.scope_stack:
            self.scope_stack.pop()

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

    def rotate_global_x(self, angle):
        """Obrót wokół globalnej osi X."""
        rad = math.radians(angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        new_forward = np.array([self.forward[0],
                                self.forward[1]*cos_a - self.forward[2]*sin_a,
                                self.forward[1]*sin_a + self.forward[2]*cos_a])
        new_up = np.array([self.up[0],
                        self.up[1]*cos_a - self.up[2]*sin_a,
                        self.up[1]*sin_a + self.up[2]*cos_a])
        new_right = np.array([self.right[0],
                            self.right[1]*cos_a - self.right[2]*sin_a,
                            self.right[1]*sin_a + self.right[2]*cos_a])
        self.forward, self.up, self.right = new_forward, new_up, new_right
        self.angle_x += angle

    def rotate_global_y(self, angle):
        rad = math.radians(angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        new_forward = np.array([self.forward[0]*cos_a + self.forward[2]*sin_a,
                                self.forward[1],
                                -self.forward[0]*sin_a + self.forward[2]*cos_a])
        new_up = np.array([self.up[0]*cos_a + self.up[2]*sin_a,
                        self.up[1],
                        -self.up[0]*sin_a + self.up[2]*cos_a])
        new_right = np.array([self.right[0]*cos_a + self.right[2]*sin_a,
                            self.right[1],
                            -self.right[0]*sin_a + self.right[2]*cos_a])
        self.forward, self.up, self.right = new_forward, new_up, new_right
        self.angle_y += angle

    def rotate_global_z(self, angle):
        rad = math.radians(angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        new_forward = np.array([self.forward[0]*cos_a - self.forward[1]*sin_a,
                                self.forward[0]*sin_a + self.forward[1]*cos_a,
                                self.forward[2]])
        new_up = np.array([self.up[0]*cos_a - self.up[1]*sin_a,
                        self.up[0]*sin_a + self.up[1]*cos_a,
                        self.up[2]])
        new_right = np.array([self.right[0]*cos_a - self.right[1]*sin_a,
                            self.right[0]*sin_a + self.right[1]*cos_a,
                            self.right[2]])
        self.forward, self.up, self.right = new_forward, new_up, new_right
        self.angle_z += angle

    def get_direction_vector(self) -> Tuple[float, float, float]:
        """Zwraca gotowy, przeliczony wektor kierunku"""
        return tuple(self.forward)

    def move(self, distance: float):
        """Move turtle forward by distance"""
        dx, dy, dz = self.get_direction_vector()
        new_x = self.position.x + dx * distance
        new_y = self.position.y + dy * distance
        new_z = self.position.z + dz * distance

        if self.is_pen_down:
            new_vertex = Vertex(new_x, new_y, new_z)

            self.lines.append((self.position, new_vertex))

            self.vertices.append(new_vertex)

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
        self.current_face_vertices.append(Vertex(self.position.x, self.position.y, self.position.z))
    
    def end_face(self):
        """Finish defining a face"""
        if self.in_face and len(self.current_face_vertices) >= 3:
            self.faces.append(Face(self.current_face_vertices.copy()))
        self.in_face = False
        self.current_face_vertices = []
    
    def export_obj(self, filename: str):
        """Export mesh to OBJ file"""
        with open(filename, 'w') as f:
            f.write("# Generated by SpacialTurtle Interpreter\n")
            f.write("o TurtleMesh\n")
            
            for v in self.vertices:
                f.write(f"v {v.x} {v.y} {v.z}\n")
            
            face_vertices = []
            for face in self.faces:
                face_indices = []
                for v in face.vertices:
                    try:
                        idx = self.vertices.index(v)
                        face_indices.append(idx + 1)
                    except ValueError:
                        pass
                if len(face_indices) >= 3:
                    face_vertices.append(face_indices)
            
            for indices in face_vertices:
                f.write(f"f {' '.join(map(str, indices))}\n")