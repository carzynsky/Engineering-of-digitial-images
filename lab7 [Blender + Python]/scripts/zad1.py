import bpy

bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 0))
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].render_levels = 3
bpy.context.object.modifiers["Subdivision"].levels = 3
