import bpy
import math

mesh = bpy.data.meshes.new("Mexican hat") # add the new mesh
obj = bpy.data.objects.new(mesh.name, mesh)
col = bpy.data.collections.get("Collection")
col.objects.link(obj)
bpy.context.view_layer.objects.active = obj

N = 1
start, stop, step = -1, 1, 0.01

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += step
        
verts = []
for x in float_range(start, stop, step):
    for y in float_range(start, stop, step):
        t = (x**2 + y**2)**0.5
        z = (1 - pow(t, 2)) * math.exp(math.pow(t, 2) / -2.0)
        verts.append((x, y, z))

vertsLen = len([x for x in float_range(start, stop, step)])

faces = []

for x in range(vertsLen-1):
    for y in range(vertsLen-1):
        faces.append((vertsLen*x + y, vertsLen*x + y +1, vertsLen*(x+1) + y + 1, vertsLen*(x+1) + y))
        
edges = [] # if empty the edges are inferred from the polygons.
mesh.from_pydata(verts, edges, faces)