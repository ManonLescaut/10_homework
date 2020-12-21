#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Vector():
    def __init__(self, x = 0, y = 0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def set_vector(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return Vector(self.x, self.y, self.z)
    
    def get_vector(self):
        return [self.x, self.y, self.z]
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def dist(self, other):
        return abs(self-other)
    
    def scalar(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    
    def cos(self, other):
        return self.scalar(other)/(abs(self)*abs(other))


# In[ ]:


# Определяет наиболее удаленную от начала координат точку
def far_dot(dots, N):
    max_distance = float('-inf')
    far_dot = Vector()
    for dot in dots:
        distance = abs(dot)
        if distance > max_distance:
            max_distance = distance
            far_dot = dot
    return (far_dot.get_vector())

N = int(input('Введите количество точек: '))
dots = []
vector = Vector()
for i in range(N):
    a, b, c = tuple(map(int, input('Координаты n-ой точки: ').split()))
    dots.append(vector.set_vector(a, b, c))
    
far_dot(dots, N)


# In[ ]:


# рассчитывает центр масс системы точек
def mass_centre(dots, N):
    x_center, y_center, z_center = 0, 0, 0
    for dot in dots:
        x_center += dot.x
        y_center += dot.y
        z_center += dot.z
    return Vector(x_center/N, y_center/N, z_center/N).get_vector()

N = int(input('Введите количество точек: '))
dots = []
vector = Vector()
for i in range(N):
    a, b, c = tuple(map(int, input('Координаты n-ой точки: ').split()))
    dots.append(vector.set_vector(a, b, c))
    
mass_centre(dots, N)


# In[ ]:


# рассчитывает площадь параллелограмма, построенного на двух векторах
def parallelogramm_square(x, y):
    return abs(x)*abs(y)*(1-x.cos(y)**2)**0.5

a, b, c = tuple(map(int, input('Введите координаты первого вектора: ').split()))
vector_1 = Vector(a, b, c)
e, f, g = tuple(map(int, input('Введите координаты второго вектора: ').split()))
vector_2 = Vector(e, f, g)

parallelogramm_square(vector_1, vector_2)


# In[ ]:


class Graph_Edge(Vector):
        def __init__(self, x = 0, y = 0, z = 0, color = 'green'):
            self.x = x
            self.y = y
            self.z = z
            self.color = color
            
        def set_vector(self, x, y, z, color='green'):
            self.x = x
            self.y = y
            self.z = z
            self.color = color
            return Graph_Edge(self.x, self.y, self.z, self.color)

# вычисляет наибольший из возможных периметров треугольников, построенных на данных точках. 
# использует метод обхода графа в глубину
def max_perimeter(dots, N):
    dot_perimeters = [[0] for i in range(N)]
    for i in range(N):
        first_dot = dots[i]
        for j in range(1, N):
            second_dot = dots[j]
            if second_dot.color == 'red':
                pass
            else:
                for k in range(2, N):
                    third_dot = dots[k]
                    if third_dot.color == 'red':
                        pass
                    else:
                        edge_weight = abs(second_dot - first_dot) + abs(second_dot - third_dot) + abs(third_dot-first_dot)
                        dot_perimeters[i].append(edge_weight)
        first_dot.color = 'red'
    max_p = 0
    for e in range(N):
        max_c = max(dot_perimeters[e])
        if max_c > max_p:
            max_p = max_c
    return max_p
    
N = int(input('Введите количество точек: '))

vertices = []
vertex = Graph_Edge()
for i in range(N):
    a, b, c = tuple(map(int, input('Координаты n-ой точки: ').split()))
    vertices.append(vertex.set_vector(a, b, c))
if N < 3:
    print('Вы хотите, чтобы я сделал треугольник из двух точек. Я так не играю.') 
elif N >= 3:
    max_perimeter(vertices, N)


# In[ ]:




