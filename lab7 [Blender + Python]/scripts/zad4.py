import bpy
import math

mesh = bpy.data.meshes.new("Egg") # add the new mesh
obj = bpy.data.objects.new(mesh.name, mesh)
col = bpy.data.collections.get("Collection")
col.objects.link(obj)
bpy.context.view_layer.objects.active = obj

start, stop, step = 0, 1.01, 0.01

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += step
        
verts = []
for u in float_range(start, stop, step):
    for v in float_range(start, stop, step):
        x = (-90*u**5 + 225*u**4 - 270*u**3 + 180*u**2 -45*u) * math.cos(math.pi * v)
        y = 160*u**4 - 320*u**3 + 160*u**2
        z = (-90*u**5 + 225*u**4 - 270*u**3 + 180*u**2 - 45*u) * math.sin(math.pi * v)
        verts.append((x, y, z))

vertsLen = len([x for x in float_range(start, stop, step)])

faces = []

for x in range(vertsLen-1):
    for y in range(vertsLen-1):
        faces.append((vertsLen*x + y, vertsLen*x + y + 1, vertsLen*(x+1) + y +1, vertsLen*(x+1) + y))
        
edges = [] # if empty the edges are inferred from the polygons.
mesh.from_pydata(verts, edges, faces)

# post
bpy.context.object.rotation_euler[0] = 1.5708
